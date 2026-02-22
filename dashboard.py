import streamlit as st
import altair as alt
import plotly.graph_objects as go
import plotly.express as px         
import yfinance as yf
import pandas as pd

st.title("📈 Stock Market Dashboard")
st.subheader("Market Overview — S&P 500 Major Stocks")

@st.cache_data
def load_price_data():
    return pd.read_csv('data/stock_data_clean.csv', 
                        index_col=0, parse_dates=True)

prices = load_price_data()

cumulative = (1 + prices.pct_change().dropna()).cumprod() - 1

fig = px.line(
    cumulative * 100,
    title="Cumulative Returns % Since January 2023",
    labels={'value': 'Return (%)', 'variable': 'Stock'}
)
fig.add_hline(y=0, line_dash="dash", line_color="white", opacity=0.4)
fig.update_layout(height=400, hovermode='x unified')
st.plotly_chart(fig, use_container_width=True)

st.divider()

@st.cache_data
def fetch_stock_info(symbol):
    stock = yf.Ticker(symbol)
    return stock.info

@st.cache_data
def fetch_quarter(symbol):
    stock = yf.Ticker(symbol)
    return stock.quarterly_financials.T

@st.cache_data
def fetch_annual(symbol):
    stock = yf.Ticker(symbol)
    return stock.financials.T

@st.cache_data
def fetch_weekly(symbol):
    stock = yf.Ticker(symbol)
    return stock.history(period='3y', interval='1wk')

st.title('Stock dashboard')
symbol = st.text_input('Enter a stock symbol', 'AAPL')

info = fetch_stock_info(symbol)

st.header('Company Inforamation')

st.subheader(f'Name: {info["longName"]}')
st.subheader(f'Market Cap: ${info["marketCap"]/1000000:,.0f}M')
st.subheader(f'Sector: {info["sector"]}')

price_history = fetch_weekly(symbol)
st.header('Chart')
price_history = price_history.rename_axis('Date').reset_index()
candlechart = go.Figure(data=[go.Candlestick(x=price_history['Date'],
                                             low = price_history['Low'],
                                             high = price_history['High'],
                                             open= price_history['Open'],
                                             close=price_history['Close'])])

candlechart.update_layout(xaxis_rangeslider_visible=False)
st.plotly_chart(candlechart,use_container_width=True)

def calculate_rsi(data, window=14):
    delta = data['Close'].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.rolling(window).mean()
    avg_loss = loss.rolling(window).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

hist = fetch_weekly(symbol)   
rsi = calculate_rsi(hist)

fig_rsi = go.Figure()

fig_rsi.add_trace(go.Scatter(
    x=hist.index, y=rsi,
    name='RSI', line=dict(color='orange', width=1.5)
))

fig_rsi.add_hline(y=70, line_dash="dash", 
                   line_color="red", opacity=0.7,
                   annotation_text="Overbought (70)")
fig_rsi.add_hline(y=30, line_dash="dash", 
                   line_color="green", opacity=0.7,
                   annotation_text="Oversold (30)")

fig_rsi.update_layout(
    title=f"{symbol} — RSI (14-day)",
    yaxis_title="RSI",
    yaxis=dict(range=[0, 100]),
    height=300,
    xaxis_rangeslider_visible=False
)
st.plotly_chart(fig_rsi, use_container_width=True)

quarter = fetch_quarter(symbol)
annual = fetch_annual(symbol)

st.header('Financials')

viewprefrence = st.radio(label='Period',options=['Quarterly', 'Annual'],index=1,horizontal=True)

if viewprefrence == 'Quarterly':
    df = quarter.rename_axis('Quarter').reset_index()
    df = df.sort_values('Quarter',ascending=True).reset_index(drop=True)
    df['Quarter'] = pd.to_datetime(df['Quarter']).dt.to_period('Q').astype(str) 
    df['Quarter'] = df['Quarter'].apply(lambda x: f"Q{x[-1]} {x[:4]}")

    fig_revenue = go.Figure(go.Bar(
        x=df['Quarter'],
        y=df['Total Revenue'],
        name='Total Revenue'
    ))
    fig_revenue.update_layout(
        title='Quarterly Revenue',
        xaxis_title='Quarter',
        yaxis_title='Revenue (USD)',
        height=350
    )

    fig_income = go.Figure(go.Bar(
        x=df['Quarter'],
        y=df['Net Income'],
        name='Net Income',
        marker_color=df['Net Income'].apply(
            lambda x: 'green' if x >= 0 else 'red'
        )
    ))
    fig_income.update_layout(
        title='Quarterly Net Income',
        xaxis_title='Quarter',
        yaxis_title='Net Income (USD)',
        height=350
    )

    st.plotly_chart(fig_revenue, use_container_width=True)
    st.plotly_chart(fig_income, use_container_width=True)


if viewprefrence == 'Annual':
    df = annual.rename_axis('Year').reset_index()
    df['Year'] = df['Year'].astype(str) 

    fig_revenue = go.Figure(go.Bar(
        x=df['Year'],
        y=df['Total Revenue'],
        name='Total Revenue'
    ))
    fig_revenue.update_layout(
        title='Annual Revenue',
        xaxis_title='Year',
        yaxis_title='Revenue (USD)',
        height=350
    )

    fig_income = go.Figure(go.Bar(
        x=df['Year'],
        y=df['Net Income'],
        name='Net Income',
        marker_color=df['Year'].apply(
            lambda x: 'green' if df.loc[df['Year']==x, 'Net Income'].values[0] >= 0 else 'red'
        )
    ))
    fig_income.update_layout(
        title='Annual Net Income',
        xaxis_title='Year',
        yaxis_title='Net Income (USD)',
        height=350
    )

    st.plotly_chart(fig_revenue, use_container_width=True)
    st.plotly_chart(fig_income, use_container_width=True)



