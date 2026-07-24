<div align="center">

# -- ! Stock Price Analysis ! --
### *January 2017 Trading Data Explored With Pandas, NumPy & Seaborn*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Wrangling-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Viz-4C72B0?style=for-the-badge&logo=plotly&logoColor=white)](https://seaborn.pydata.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)

<br/>

> *"Twenty trading days, six columns, and a whole month of market mood swings."*

</div>

---

## 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#️-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [🧹 1. Data Cleaning](#-1-data-cleaning)
- [📊 2. Summary Statistics](#-2-summary-statistics)
- [📈 3. Closing Price Trend](#-3-closing-price-trend)
- [📉 4. Daily Price Volatility](#-4-daily-price-volatility)
- [📦 5. Trading Volume](#-5-trading-volume)
- [🐂 6. Open vs. Close & Bullish/Bearish Days](#-6-open-vs-close--bullishbearish-days)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Results & Insights](#-results--insights)
- [🏆 Advantages](#-advantages)
- [📄 License](#-license)
- [👤 Author](#-author)

---

## 📌 Overview

**Stock Price Analysis** is a Jupyter Notebook that analyzes 20 trading days of OHLC (Open/High/Low/Close) and volume data from January 2017 (`Stock_Price_Test.csv`). It cleans and type-corrects the raw data, engineers daily return and price-range metrics, then visualizes price trends, volatility, volume, and bullish/bearish day counts.

This project is designed to:
- Practice **type correction** (string dates and comma-formatted volume figures)
- Engineer **derived trading metrics**: Daily Return (%) and Price Range
- Compute **descriptive statistics** across all OHLCV columns
- Visualize the **closing price trend** with highest/lowest points marked
- Compare **daily volatility and trading volume** across the month
- Classify each day as **Bullish or Bearish** and compare counts

---

## 🎯 Problem Statement

> **Objective:** Clean and analyze a month of daily stock trading data to characterize price trend, volatility, and volume patterns.

Given 20 rows of daily Open/High/Low/Close/Volume data, the notebook must fix data types (dates stored as strings, volume stored with thousands separators), engineer return and range metrics, then answer: how did the closing price trend over the month, which days were most volatile, how did volume behave, and how many days closed up versus down?

| 📂 Section | 📄 Type | 🔍 Description |
|------------|---------|-----------------|
| Data Cleaning | Pandas | Parse dates, strip commas from Volume, dedupe, engineer metrics |
| Summary Statistics | Pandas | `describe()` across Open/High/Low/Close/Volume |
| Correlation | Seaborn Heatmap | Price vs. volume correlation |
| Closing Price Trend | Line Chart | Close price over time with high/low markers |
| Daily Volatility | Bar Chart | Price Range (High − Low) per day |
| Trading Volume | Bar Chart | Daily volume per day |
| Bullish/Bearish Days | Grouped Bar + Count Plot | Open vs. Close per day, and day-type counts |

The goal is to demonstrate a **compact but complete financial time-series EDA**.

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 🧹 **Type Correction** | `Date` parsed to datetime, `Volume` commas stripped and cast to int |
| 🧮 **Engineered Metrics** | `Daily Return (%)` and `Price Range` computed per row |
| 📊 **Full OHLCV Statistics** | `describe()` across all five price/volume columns |
| 🔥 **Price/Volume Correlation** | Heatmap shows prices move together while volume is more independent |
| 📈 **Annotated Trend Line** | Closing price chart marks the month's highest and lowest closes |
| 📉 **Volatility Bar Chart** | Daily High−Low range highlights the most turbulent trading days |
| 📦 **Volume Bar Chart** | Daily volume plotted alongside price-move days |
| 🐂🐻 **Bullish/Bearish Classification** | `np.where` labels each day, compared via grouped bar + count plot |

---

## 🏗️ Project Structure

```
📦 stock-price-analysis/
│
├── 📄 stock_price_analysis.ipynb   ← Main analysis notebook
├── 📄 Stock_Price_Test.csv         ← Source data (20 trading days, Jan 2017)
│
└── 📄 README.md                    ← Project documentation
```

---

## 🔄 Project Workflow

```
Notebook Start
      │
      ▼
┌─────────────────────────────┐
│ Load Dataset                  │  ← df.head()
└──────────────┬────────────────┘
               │
               ▼
┌─────────────────────────────┐
│ 1. Clean, Type-Fix & Engineer │  ← parse dates, fix volume, add
└──────────────┬────────────────┘     Daily Return & Price Range
               │
               ▼
┌─────────────────────────────┐
│ 2. Summary Statistics         │  ← describe(), correlation heatmap
└──────────────┬────────────────┘
               │
   ┌───────────┼────────────┬─────────────┬──────────────┐
   ▼           ▼             ▼             ▼
Closing     Daily         Trading      Bullish vs.
 Price     Volatility     Volume        Bearish
 Trend                                   Days
  (3)         (4)            (5)          (6)
```

---

## 🧹 1. Data Cleaning

Parses the `Date` column to proper datetime, strips comma separators from `Volume` and casts to int, sorts chronologically, and engineers two new trading metrics.

**Logic:**
```python
df['Date'] = pd.to_datetime(df['Date'])
df['Volume'] = df['Volume'].str.replace(',', '').astype(int)

df = df.dropna().drop_duplicates(subset=['Date']).sort_values('Date').reset_index(drop=True)

df['Daily Return (%)'] = (df['Close'] - df['Open']) / df['Open'] * 100
df['Price Range'] = df['High'] - df['Low']
```

**Sample Output:**
```
Final shape: (20, 8)

Date         Open    High    Low     Close   Volume    Daily Return (%)  Price Range
2017-01-03  778.81  789.63  775.80  786.14  1657300         0.941179        13.83
2017-01-04  788.36  791.34  783.16  786.90  1073000        -0.185195         8.18
2017-01-05  786.08  794.48  785.02  794.02  1335200         1.010075         9.46
```

---

## 📊 2. Summary Statistics

Describes Open, High, Low, Close, and Volume, then a correlation heatmap shows how price columns relate to each other and to volume.

**Sample Output:**
```
             Open        High         Low       Close        Volume
mean    807.526     811.9265     801.9495     807.9045   1,659,895
std      15.125       14.381       13.279       13.210     677,475
min     778.810      789.630      775.800      786.140     919,300
max     837.810      841.950      827.010      835.670   3,246,600
```

> **Finding:** Prices are strongly correlated with each other, while volume moves fairly independently.

---

## 📈 3. Closing Price Trend

Plots the closing price across all 20 trading days, marking the month's highest and lowest closes.

**Logic:**
```python
plt.plot(df['Date'], df['Close'], marker='o', color='steelblue')
plt.scatter(df.loc[df['Close'].idxmax(), 'Date'], df['Close'].max(), color='green', label='Highest')
plt.scatter(df.loc[df['Close'].idxmin(), 'Date'], df['Close'].min(), color='red', label='Lowest')
```

> **Finding:** The stock trends upward over the month, closing at its highest near the end and lowest near the start.

---

## 📉 4. Daily Price Volatility

A bar chart of daily `Price Range` (High − Low) shows which days had the widest intraday price swings.

> **Finding:** Volatility rises later in the month, with the widest price swing seen in late January.

---

## 📦 5. Trading Volume

A bar chart of daily trading volume, compared visually against the volatility chart above.

> **Finding:** Volume spikes coincide with the days that had the largest price moves, both up and down.

---

## 🐂 6. Open vs. Close & Bullish/Bearish Days

Each day is classified as Bullish (`Close > Open`) or Bearish otherwise; a grouped bar chart shows daily open-vs-close, paired with a count plot of bullish vs. bearish day totals.

**Logic:**
```python
df['Trend'] = np.where(df['Close'] > df['Open'], 'Bullish', 'Bearish')

axes[0].bar(x - 0.2, df['Open'], width=0.4, label='Open', color='slategray')
axes[0].bar(x + 0.2, df['Close'], width=0.4, label='Close', color='seagreen')

sns.countplot(x='Trend', data=df, palette={'Bullish': 'seagreen', 'Bearish': 'indianred'}, ax=axes[1])
```

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| 🐍 **Python** | 3.8+ | Core language |
| 📓 **Jupyter Notebook** | Any recent | Interactive analysis environment |
| 🐼 **Pandas** | Any recent | Type correction, cleaning, aggregation |
| 🔢 **NumPy** | Any recent | `np.where` classification, numeric ops |
| 📊 **Matplotlib** | Any recent | Line, bar, and grouped-bar charts |
| 🎨 **Seaborn** | Any recent | Heatmap, styled bar chart, count plot |

---

## 📈 Results & Insights

- ✅ **20 Clean Trading Days** — no missing values or duplicate dates after cleaning
- 📈 **Upward Monthly Trend** — closing price ends the month higher than it started
- 📉 **Rising Late-Month Volatility** — the widest daily price range occurs in late January
- 📦 **Volume Tracks Volatility** — the biggest volume days line up with the biggest price moves
- 🐂🐻 **Bullish/Bearish Split** — day-type counts reveal the balance of up vs. down trading days
- 🔥 **Price Columns Move Together** — Open/High/Low/Close are tightly correlated; Volume is more independent

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 🧮 **Purpose-Built Metrics** | Daily Return and Price Range turn raw OHLC into analysis-ready columns |
| 🧹 **Real-World Type Fixes** | Handles the common "volume has commas" and "date is a string" pitfalls |
| 📈 **Annotated Visuals** | High/low markers and bullish/bearish coloring make charts self-explanatory |
| 📝 **Narrated Findings** | Each visualization is followed by a plain-language takeaway |
| 📚 **Educational** | A compact template for any short-window OHLCV time-series analysis |
| 🖥️ **Standard Stack** | Built entirely on Pandas, NumPy, Matplotlib, and Seaborn |

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for full details.

```
MIT License — Free to use, modify, and distribute with attribution.
```

---

## 👤 Author

<div align="center">

### Ved Dhameliya

[![GitHub](https://img.shields.io/badge/GitHub-yourhandle-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/isamaliya16)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ayush-isamaliya-686533312/)

> *"The market writes a new sentence every trading day — this notebook just reads it back."*

**🎓 Role:** Junior Python Developer | Programming Enthusiast \
**📍 Location:** India\
**🛠️ Skills:** Python · Pandas · NumPy · Seaborn · Exploratory Data Analysis

</div>

---

<div align="center">

---

*Made with ❤️ and ☕ — Last updated: 22 July, 2026*

</div>
