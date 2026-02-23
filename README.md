# 📈 Financial Dashboard — Multi-Stock Analysis (2023–2026)

An interactive financial dashboard built with **Python**, **Plotly**, and **yfinance** to analyze and visualize stock performance, technical indicators, and financial fundamentals for 8 major companies.

---

## 🎯 Project Overview

This dashboard was built to answer one key question: **How have major US stocks performed across different sectors from January 2023 to February 2026?**

The goal is to give investors and analysts a clear, interactive view of price history, momentum indicators, and financial fundamentals — all in one place. The 8 stocks were selected to represent a cross-section of sectors: technology (NVDA, MSFT, AAPL, GOOGL), EV (TSLA), financials (JPM), energy (XOM), and healthcare (JNJ).

---

## 🗄️ Data Source

All data was fetched using the **yfinance** Python library, which pulls from Yahoo Finance.

- **Financial data**: Quarterly and annual income statements (Revenue, Net Income)
- **Tickers covered**: NVDA, TSLA, GOOGL, JPM, AAPL, MSFT, XOM, JNJ

---

## 🔬 Steps & Methodology

1. **Data Collection** — Pulled historical price and financial data via `yfinance` for 8 tickers
2. **Data Validation** — Verified data completeness, checked for nulls, and confirmed column consistency across all tickers
3. **Feature Engineering** — Calculated cumulative returns, daily % change, and RSI (14-day window)
4. **Visualization** — Built interactive charts using Plotly (candlestick, line, bar)
5. **Dashboard Design** — Assembled all views in Streamlit with sidebar ticker selection and tab navigation

---

## 🖥️ Dashboard Preview

![Full Dashboard](screenshots/full.png)

---

## 🚀 Live Demo

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://financial-dashboard-n3pz9keepeijy9txbjws9p.streamlit.app/)

👆 Click the badge to open the live dashboard

---

## 📸 Screenshots

| View | Preview |
|------|---------|
| Cumulative Returns | ![Cumulative](screenshots/cumulative.png) |
| Candlestick Chart | ![Candlestick](screenshots/candle.png) |
| RSI Indicator | ![RSI](screenshots/rsi.png) |
| Financials (Revenue & Net Income) | ![Financials](screenshots/financials.png) |
| Ticker View | ![Ticker](screenshots/ticker.png) |

---

## 📊 Key Findings (Jan 2023 – Feb 2026)

| Ticker | Company | Total Return % |
|--------|---------|---------------|
| NVDA | NVIDIA | +1213.92% |
| TSLA | Tesla | +280.86% |
| GOOGL | Alphabet | +242.39% |
| JPM | JPMorgan Chase | +146.58% |
| AAPL | Apple | +111.69% |
| MSFT | Microsoft | +70.68% |
| XOM | ExxonMobil | +58.19% |
| JNJ | Johnson & Johnson | +51.80% |

> NVIDIA was the standout performer with a return of over **1,200%**, driven by the AI chip demand surge.

---

## 💡 Key Insights

- **NVDA dominated all sectors** with a +1,213% return, driven by explosive AI chip demand from 2023 onward
- **TSLA and GOOGL** were the second and third best performers at +280% and +242%, both benefiting from AI tailwinds
- **Defensive stocks (JNJ, XOM)** delivered modest but stable returns (+51–58%), suitable for risk-averse portfolios
- **Recommendation**: A tech-heavy allocation toward NVDA, GOOGL, and JPM would have significantly outperformed the broader market over this period

---

## ⚠️ Assumptions & Limitations

- Data is pulled from Yahoo Finance via `yfinance` and may not always be 100% accurate
- The dashboard covers Jan 2023 – Feb 2026 only and does not reflect real-time prices
- Returns shown are price returns only — dividends are not included

---

## ⚙️ Features

- 📉 **Cumulative Returns** — Compare all 8 stocks on a single chart over the full period
- 🕯️ **Candlestick Charts** — OHLC price history per stock with volume overlay
- 📐 **RSI Indicator** — Relative Strength Index to identify overbought/oversold conditions
- 💰 **Financials** — Quarterly and annual revenue and net income per company
- 🔍 **Ticker View** — Deep dive into any individual stock

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| `Python` | Core language |
| `yfinance` | Fetch historical stock & financial data |
| `Pandas` | Data manipulation and transformation |
| `Plotly` | Interactive charts and visualizations |
| `Streamlit` | Web app framework for the dashboard UI |
| `Jupyter Notebook` | Exploratory analysis |

---

## 🏁 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/brhosul02/financial-dashboard.git
cd financial-dashboard
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the dashboard
```bash
streamlit run dashboard.py
```

---

## 📁 Project Structure

```
financial-dashboard/
│
├── dashboard.py              # Main dashboard script
├── requirements.txt          # Project dependencies
├── README.md
│
├── data/
│   ├── stock_data_raw.csv    # Raw data fetched from yfinance
│   └── stock_data_clean.csv  # Cleaned and processed data
│
├── data_preprocessing.ipynb
│
│
└── screenshots/
    ├── full.png
    ├── cumulative.png
    ├── candle.png
    ├── rsi.png
    ├── ticker.png
    └── financials.png
```

---

## 👨‍💻 Author

**Ibrahim Alsaeed**  
[GitHub](https://github.com/brhosul02)

[Linkedin](https://www.linkedin.com/in/ibrahim-alsaeed)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
