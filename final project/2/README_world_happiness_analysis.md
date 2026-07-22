<div align="center">

# -- ! World Happiness Analysis ! --
### *Exploring The 2015 World Happiness Report With Pandas, NumPy & Seaborn*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Wrangling-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Viz-4C72B0?style=for-the-badge&logo=plotly&logoColor=white)](https://seaborn.pydata.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)

<br/>

> *"Happiness, it turns out, leaves a very readable dataset."*

</div>

---

## 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#️-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [🧹 1. Data Cleaning & Preparation](#-1-data-cleaning--preparation)
- [📊 2. Summary Statistics & Correlation](#-2-summary-statistics--correlation)
- [🏆 3. Top & Bottom Performing Countries](#-3-top--bottom-performing-countries)
- [🌍 4. Regional Happiness Distribution](#-4-regional-happiness-distribution)
- [💰 5. Factor Impact Analysis](#-5-factor-impact-analysis)
- [⚖️ 6. Corruption vs. Freedom Segmentation](#️-6-corruption-vs-freedom-segmentation)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Results & Insights](#-results--insights)
- [🏆 Advantages](#-advantages)
- [📄 License](#-license)
- [👤 Author](#-author)

---

## 📌 Overview

**World Happiness Analysis** is a Jupyter Notebook exploring the **2015 World Happiness Report** (`2015.csv`, 158 countries). It walks through cleaning and standardizing the raw survey data, then digs into what actually correlates with happiness — GDP, family, health, freedom, trust, and generosity — through statistics and six focused visualizations.

This project is designed to:
- Practice **column standardization** (snake_case renaming via regex)
- Compute **summary statistics and correlations** across seven happiness-related metrics
- Identify **top and bottom performing countries**
- Compare **regional happiness distributions**
- Visualize the **relationship between GDP and happiness** with a regression trendline
- Explore the **corruption-vs-freedom** relationship across regions

---

## 🎯 Problem Statement

> **Objective:** Determine which factors are most associated with national happiness and how happiness varies by country and region.

Given the 2015 World Happiness Report — happiness score, GDP per capita, family, health, freedom, trust in government, generosity, and dystopia residual for 158 countries — the notebook must clean the data, then answer: which countries are happiest and least happy, how do regions compare, does wealth predict happiness, and how do corruption perceptions relate to freedom?

| 📂 Section | 📄 Type | 🔍 Description |
|------------|---------|-----------------|
| Data Cleaning | Pandas | Missing-value check, column renaming, duplicate removal |
| Summary Statistics | Pandas/NumPy | `describe()` and mode for 7 numerical columns |
| Correlation Matrix | Seaborn Heatmap | Correlation across all 8 numerical features |
| Top/Bottom Countries | Pandas + Bar Chart | 5 happiest and 5 least happy countries |
| Regional Distribution | groupby + Bar Chart | Average happiness & GDP by region |
| Factor Impact | Scatter + Regression | GDP per capita vs. happiness score, colored by region |
| Corruption vs. Freedom | Scatter Plot | Trust in government vs. freedom to make life choices |

The goal is to demonstrate a **complete exploratory data analysis** on a well-known social-science dataset.

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 🧹 **Column Standardization** | Regex-based lowercase/underscore renaming of all 12 columns |
| 🔍 **Missing & Duplicate Checks** | Explicit `isnull().sum()` and `duplicated().sum()` before analysis |
| 📊 **7-Column Statistical Summary** | `describe()` plus mode values for every key metric |
| 🔥 **Correlation Heatmap** | All 8 numerical features cross-correlated and annotated |
| 🏆 **Top/Bottom-5 Comparison** | Side-by-side green/red bar charts for happiest and least happy nations |
| 🌍 **Regional Aggregation** | `groupby('region')` with sorted average happiness and GDP |
| 📈 **Regression Trendline** | `sns.regplot` overlays a fitted trend on the GDP-vs-happiness scatter |
| ⚖️ **Segmentation Scatter** | Corruption vs. freedom colored by region to reveal regional clusters |

---

## 🏗️ Project Structure

```
📦 world-happiness-analysis/
│
├── 📄 world_happiness_analysis.ipynb   ← Main analysis notebook
├── 📄 2015.csv                         ← Source data (158 countries)
│
└── 📄 README.md                        ← Project documentation
```

---

## 🔄 Project Workflow

```
Notebook Start
      │
      ▼
┌─────────────────────────────┐
│ Load Dataset & Inspect        │  ← df.head(), df.info()
└──────────────┬────────────────┘
               │
               ▼
┌─────────────────────────────┐
│ 1. Clean & Standardize        │  ← missing check, rename cols, dedupe
└──────────────┬────────────────┘
               │
               ▼
┌─────────────────────────────┐
│ 2. Stats & Correlation Matrix │  ← describe(), mode(), heatmap
└──────────────┬────────────────┘
               │
   ┌───────────┼───────────┬────────────┬─────────────┐
   ▼           ▼           ▼            ▼             ▼
Top/Bottom  Regional   GDP vs.     Corruption vs.
 Countries Distribution Happiness    Freedom
   (3)         (4)        (5)          (6)
```

---

## 🧹 1. Data Cleaning & Preparation

Checks for missing values, standardizes all column names to snake_case, and removes duplicate rows/countries.

**Logic:**
```python
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(r'[^a-z0-9]+', '_', regex=True)
    .str.strip('_')
)
df = df.drop_duplicates()
```

**Sample Output:**
```
Missing values per column: 0 across all 12 columns

['country', 'region', 'happiness_rank', 'happiness_score', 'standard_error',
 'economy_gdp_per_capita', 'family', 'health_life_expectancy', 'freedom',
 'trust_government_corruption', 'generosity', 'dystopia_residual']

Number of duplicate rows found: 0
Number of duplicate country entries found: 0
Dataset shape after removing duplicates: (158, 12)
```

---

## 📊 2. Summary Statistics & Correlation

Computes `describe()` and mode for 7 core numerical columns, then builds a correlation heatmap across all 8 numerical features (including `dystopia_residual`).

**Sample Output (mode values):**
```
happiness_score                5.19200
economy_gdp_per_capita         0.00000
family                         0.00000
health_life_expectancy         0.92356
freedom                        0.00000
trust_government_corruption    0.32524
generosity                     0.00000
```

**Logic (Heatmap):**
```python
corr_matrix = df[corr_cols].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
```

---

## 🏆 3. Top & Bottom Performing Countries

Uses `nlargest`/`nsmallest` to isolate the 5 happiest and 5 least happy countries, then plots them as side-by-side bar charts.

**Sample Output:**
```
Top 5 Happiest:
Switzerland  7.587
Iceland      7.561
Denmark      7.527
Norway       7.522
Canada       7.427

Bottom 5 Least Happy:
Togo      2.839
Burundi   2.905
Syria     3.006
Benin     3.340
Rwanda    3.465
```

---

## 🌍 4. Regional Happiness Distribution

Groups by `region`, computing average happiness score and average GDP per capita, sorted descending.

**Sample Output:**
```
Region                             Avg Happiness   Avg GDP/Capita
Australia and New Zealand              7.285           1.292
North America                          7.273           1.360
Western Europe                         6.690           1.299
Latin America and Caribbean            6.145           0.877
Eastern Asia                           5.626           1.152
Middle East and Northern Africa        5.407           1.067
Central and Eastern Europe             5.333           0.942
Southeastern Asia                      5.317           0.789
Southern Asia                          4.581           0.560
Sub-Saharan Africa                     4.203           0.380
```

---

## 💰 5. Factor Impact Analysis

A scatter plot of GDP per capita vs. happiness score, colored by region, with an overlaid regression trendline showing the overall positive relationship.

**Logic:**
```python
sns.scatterplot(data=df, x='economy_gdp_per_capita', y='happiness_score', hue='region', s=70)
sns.regplot(data=df, x='economy_gdp_per_capita', y='happiness_score', scatter=False,
            color='black', line_kws={'linestyle': '--', 'label': 'Trendline'})
```

---

## ⚖️ 6. Corruption vs. Freedom Segmentation

A second scatter plot examines how perceptions of government corruption relate to freedom to make life choices, again colored by region to reveal clustering patterns.

**Logic:**
```python
sns.scatterplot(data=df, x='trust_government_corruption', y='freedom', hue='region', s=70)
```

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| 🐍 **Python** | 3.8+ | Core language |
| 📓 **Jupyter Notebook** | Any recent | Interactive analysis environment |
| 🐼 **Pandas** | Any recent | Cleaning, grouping, aggregation |
| 🔢 **NumPy** | Any recent | Underlying numeric operations |
| 📊 **Matplotlib** | Any recent | Plot rendering and layout |
| 🎨 **Seaborn** | Any recent | Heatmaps, bar charts, scatter + regression plots |

---

## 📈 Results & Insights

- ✅ **158 Countries, Zero Cleaning Issues** — no missing values or duplicates in this dataset
- 🥇 **Happiest Country** — Switzerland (7.587)
- 🥉 **Least Happy Country** — Togo (2.839)
- 🌏 **Happiest Region** — Australia and New Zealand (avg. 7.285)
- 🌍 **Least Happy Region** — Sub-Saharan Africa (avg. 4.203)
- 💰 **GDP Correlation** — higher GDP per capita trends with higher happiness, visualized with a regression line
- ⚖️ **Corruption/Freedom Pattern** — regional clustering visible when plotting trust vs. freedom

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 🧹 **Clean Column Pipeline** | Regex-based renaming keeps all downstream code consistent |
| 📊 **Comprehensive Stats** | Covers both central tendency (mean, mode) and spread (std) |
| 🌍 **Multi-Level Comparison** | Country-level and region-level views side by side |
| 📈 **Regression-Backed Insight** | Trendline turns a scatter plot into an actual claim about GDP's effect |
| 🎨 **Consistent Styling** | `sns.set_theme(style="whitegrid")` applied throughout |
| 📚 **Educational** | Good template for any "explore a scored/ranked dataset" analysis |

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

> *"Numbers can't measure happiness perfectly — but they can point at what tends to help."*

**🎓 Role:** Junior Python Developer | Programming Enthusiast \
**📍 Location:** India\
**🛠️ Skills:** Python · Pandas · NumPy · Seaborn · Exploratory Data Analysis

</div>

---

<div align="center">

---

*Made with ❤️ and ☕ — Last updated: 22 July, 2026*

</div>
