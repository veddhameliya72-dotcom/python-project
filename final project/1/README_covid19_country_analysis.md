<div align="center">

# -- ! COVID-19 Country Analysis ! --
### *Country-Wise Pandemic Impact Analysis With Pandas & Seaborn*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Wrangling-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Viz-4C72B0?style=for-the-badge&logo=plotly&logoColor=white)](https://seaborn.pydata.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)

<br/>

> *"Behind every case count is a country's story — this notebook reads 187 of them."*

</div>

---

## 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#️-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [🧹 1. Data Cleaning](#-1-data-cleaning)
- [📊 2. Summary Statistics & Correlation](#-2-summary-statistics--correlation)
- [🌐 3. Top 5 Impacted Countries](#-3-top-5-impacted-countries)
- [🗺️ 4. WHO Regional Insights](#️-4-who-regional-insights)
- [⚰️ 5. Case Fatality Rate Distribution](#️-5-case-fatality-rate-distribution)
- [📈 6. Active vs. New Cases](#-6-active-vs-new-cases)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Results & Insights](#-results--insights)
- [🏆 Advantages](#-advantages)
- [📄 License](#-license)
- [👤 Author](#-author)

---

## 📌 Overview

**COVID-19 Country Analysis** is a Jupyter Notebook that examines country-wise pandemic data (`country_wise_latest.csv`, 187 countries) — confirmed cases, deaths, recoveries, and WHO regional breakdowns — to surface the most-impacted countries, regional disparities, and fatality-rate outliers.

This project is designed to:
- Practice cleaning and **engineering a derived metric** (Active Cases Ratio)
- Compute **summary statistics and correlations** across core pandemic metrics
- Identify **top-impacted countries** by confirmed case count
- Aggregate case/death/recovery totals **by WHO region**
- Detect **fatality-rate outliers** using a boxplot and a 95th-percentile cutoff
- Visualize the **relationship between active and new cases** across regions

---

## 🎯 Problem Statement

> **Objective:** Analyze country-level COVID-19 statistics to identify the most-affected countries, regional disparities, and unusual fatality-rate patterns.

Given a snapshot of confirmed, death, recovered, and active case counts per country (plus WHO region), the notebook must clean the data, then answer: which countries have the most confirmed cases, how do WHO regions compare, which countries have unusually high fatality rates, and how do active and new cases relate?

| 📂 Section | 📄 Type | 🔍 Description |
|------------|---------|-----------------|
| Data Cleaning | Pandas | Drop missing/duplicate rows, engineer Active Cases Ratio |
| Summary Statistics | Pandas | `describe()` on Confirmed/Deaths/Recovered/Active |
| Correlation Heatmap | Seaborn | Correlations among 7 key pandemic metrics |
| Top 5 Countries | Bar Chart | 5 countries with the most confirmed cases |
| WHO Regional Insights | groupby + Bar Chart | Confirmed vs. recovered totals by region |
| Fatality Rate Distribution | Boxplot + Outliers | Countries above the 95th percentile fatality rate |
| Active vs. New Cases | Scatter Plot | Relationship colored by WHO region |

The goal is to demonstrate a **country-level epidemiological data analysis** from raw CSV to actionable insight.

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 🧹 **Missing/Duplicate Handling** | `dropna()` and `drop_duplicates()` before any analysis |
| 🧮 **Engineered Metric** | `Active Cases Ratio (%)` derived as `Active / Confirmed * 100` |
| 📊 **Descriptive Statistics** | `describe()` and mode across the four core case metrics |
| 🔥 **Correlation Heatmap** | 7-metric correlation matrix including case-fatality ratios |
| 🌐 **Top-Impacted Ranking** | `nlargest()` isolates the 5 hardest-hit countries |
| 🗺️ **Regional Aggregation** | `groupby('WHO Region')` sums cases/deaths/recovered, stacked bar chart |
| 📦 **Outlier Detection** | Boxplot + 95th-percentile filter surfaces high-fatality countries |
| 📈 **Regional Scatter** | Active vs. new cases colored by WHO region |

---

## 🏗️ Project Structure

```
📦 covid19-country-analysis/
│
├── 📄 covid19_country_analysis.ipynb   ← Main analysis notebook
├── 📄 country_wise_latest.csv          ← Source data (187 countries)
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
│ Load Dataset                  │  ← df.head()
└──────────────┬────────────────┘
               │
               ▼
┌─────────────────────────────┐
│ 1. Clean & Engineer Metric     │  ← dropna, drop_duplicates, Active Ratio
└──────────────┬────────────────┘
               │
               ▼
┌─────────────────────────────┐
│ 2. Stats & Correlation Matrix │  ← describe(), heatmap
└──────────────┬────────────────┘
               │
   ┌───────────┼────────────┬─────────────┬──────────────┐
   ▼           ▼             ▼             ▼
Top 5      WHO Regional   Fatality     Active vs.
Countries    Insights       Outliers    New Cases
  (3)          (4)            (5)          (6)
```

---

## 🧹 1. Data Cleaning

Drops any missing/duplicate rows and engineers a new `Active Cases Ratio (%)` column.

**Logic:**
```python
df = df.dropna().drop_duplicates()
df['Active Cases Ratio (%)'] = (df['Active'] / df['Confirmed']) * 100
```

**Sample Output:**
```
Missing values: 0
Final shape: (187, 16)
```

---

## 📊 2. Summary Statistics & Correlation

Describes the four core metrics and builds a correlation heatmap across confirmed cases, deaths, recovered, active, new cases, and both fatality/recovery percentage columns.

**Sample Output:**
```
          Confirmed        Deaths     Recovered       Active
mean    88130.94        3497.52      50631.48      34001.94
std    383318.70       14100.00     190188.20     213326.20
min        10.00           0.00          0.00          0.00
max   4290259.00      148011.00    1846641.00    2816444.00
```

**Logic (Heatmap):**
```python
num_cols = ['Confirmed', 'Deaths', 'Recovered', 'Active', 'New cases',
            'Deaths / 100 Cases', 'Recovered / 100 Cases']
sns.heatmap(df[num_cols].corr(), annot=True, cmap='coolwarm', fmt='.2f')
```

---

## 🌐 3. Top 5 Impacted Countries

Ranks countries by confirmed case count and plots the top 5 as a horizontal bar chart.

**Logic:**
```python
top5 = df.nlargest(5, 'Confirmed')[['Country/Region', 'Confirmed']]
sns.barplot(x='Confirmed', y='Country/Region', data=top5, color='indianred')
```

---

## 🗺️ 4. WHO Regional Insights

Sums confirmed, deaths, and recovered by WHO region, then plots confirmed vs. recovered side by side.

**Sample Output:**
```
WHO Region              Confirmed    Deaths    Recovered
Americas                 8839286     342732     4468616
Europe                   3299523     211144     1993723
South-East Asia          1835297      41349     1156933
Eastern Mediterranean    1490744      38339     1201400
Africa                    723207      12223      440645
Western Pacific           292428       8249      206770
```

---

## ⚰️ 5. Case Fatality Rate Distribution

A boxplot shows the spread of `Deaths / 100 Cases` across all countries; countries above the 95th percentile are pulled out as outliers.

**Sample Output (top fatality-rate outliers):**
```
Country            Deaths / 100 Cases
Yemen                       28.56
United Kingdom               15.19
Belgium                      14.79
Italy                        14.26
France                       13.71
Hungary                      13.40
Netherlands                  11.53
Mexico                       11.13
Spain                        10.44
Western Sahara                10.00
```

---

## 📈 6. Active vs. New Cases

A scatter plot of active cases against new cases, colored by WHO region, to see how ongoing case load relates to daily new-case volume across regions.

**Logic:**
```python
sns.scatterplot(x='Active', y='New cases', hue='WHO Region', data=df, s=60)
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
| 🎨 **Seaborn** | Any recent | Heatmap, bar charts, boxplot, scatter plot |

---

## 📈 Results & Insights

- ✅ **187 Countries Analyzed** after dropping missing/duplicate rows
- 🌐 **Highest Confirmed-Case Countries** highlighted via the Top-5 bar chart
- 🗺️ **Americas Leads All Regions** — highest confirmed, deaths, and recovered totals
- ⚰️ **Yemen Has The Highest Fatality Rate** at 28.56 deaths per 100 cases, well above the 95th-percentile cutoff
- 📈 **Active/New Case Relationship** varies meaningfully by WHO region
- 🔥 **Strong Metric Correlations** visible in the heatmap among confirmed, deaths, and recovered

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 🧮 **Derived Metric** | Active Cases Ratio adds analytical value beyond the raw columns |
| 📦 **Statistical Outlier Detection** | Percentile-based filtering avoids arbitrary fatality-rate thresholds |
| 🗺️ **Regional Rollups** | WHO region grouping puts country-level data in global context |
| 📊 **Multi-Chart Coverage** | Bar, heatmap, boxplot, and scatter each answer a different question |
| 📚 **Educational** | A clean template for any country/region epidemiological dataset |
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

### Ayush Isamaliya

[![GitHub](https://img.shields.io/badge/GitHub-yourhandle-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/isamaliya16)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ayush-isamaliya-686533312/)

> *"A pandemic dataset is really a map of resilience, told in numbers."*

**🎓 Role:** Junior Python Developer | Programming Enthusiast \
**📍 Location:** India\
**🛠️ Skills:** Python · Pandas · NumPy · Seaborn · Exploratory Data Analysis

</div>

---

<div align="center">

---

*Made with ❤️ and ☕ — Last updated: 22 July, 2026*

</div>
