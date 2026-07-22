<div align="center">

# -- ! NYC Air Quality Analysis ! --
### *Borough-Level & Temporal Pollution Trends With Pandas & Seaborn*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Wrangling-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Viz-4C72B0?style=for-the-badge&logo=plotly&logoColor=white)](https://seaborn.pydata.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)

<br/>

> *"The air over five boroughs tells five different stories — this notebook separates them."*

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
- [🧪 3. Pollutant Concentration Breakdown](#-3-pollutant-concentration-breakdown)
- [🗽 4. Borough-Level Comparison](#-4-borough-level-comparison)
- [📆 5. Temporal Trends Analysis](#-5-temporal-trends-analysis)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Results & Insights](#-results--insights)
- [🏆 Advantages](#-advantages)
- [📄 License](#-license)
- [👤 Author](#-author)

---

## 📌 Overview

**NYC Air Quality Analysis** is a Jupyter Notebook exploring New York City's public air-quality indicator dataset (`air-quality-1.csv`, 2,769 raw records across boroughs and neighborhoods). It cleans a genuinely messy real-world dataset — misaligned rows, duplicate indicator entries, mixed measures — then breaks pollution down by pollutant type, borough, and time.

This project is designed to:
- Practice cleaning a dataset with **structurally misaligned rows** (shifted fields)
- Handle **heavy duplication** (over a third of rows removed as duplicate indicator records)
- Compute **per-indicator statistics** across 18+ different air-quality measures
- Compare **pollutant concentrations** for key toxics and emissions
- Rank **NYC boroughs** by average pollution level
- Track **temporal trends** in neighborhood-level pollution

---

## 🎯 Problem Statement

> **Objective:** Clean a large, messy municipal air-quality dataset and determine which pollutants, boroughs, and time periods show the highest pollution levels.

Given NYC's public air-quality indicator data — covering air toxics, boiler emissions, and neighborhood pollutant concentrations across multiple geographic levels and years — the notebook must first repair structural issues (shifted fields, duplicated indicator rows) before it can answer: which pollutants are most concentrated, which borough is most polluted, and how has pollution changed over time?

| 📂 Section | 📄 Type | 🔍 Description |
|------------|---------|-----------------|
| Column Renaming & Typing | Pandas | Renames misleading column, coerces to numeric |
| Misaligned Record Removal | Regex Filter | Drops rows where year field doesn't contain digits |
| Missing/Duplicate Cleanup | Pandas | Drops missing key fields and duplicate indicator IDs |
| Summary Statistics | Pandas | Per-indicator `describe()` and mode across 18+ measures |
| Correlation & Pollutant Breakdown | Bar Chart | Average concentration for 3 key pollutants |
| Borough Comparison | groupby + Bar Chart | Average pollution value by NYC borough |
| Temporal Trend | Line Chart | Neighborhood-level pollution trend with peak/low markers |

The goal is to demonstrate cleaning and analyzing a **realistically messy open-government dataset**.

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 🏷️ **Column Rename & Coercion** | `data_valuemessage` → `data_value`, coerced to numeric with `errors='coerce'` |
| 🧹 **Structural Row Repair** | Filters out Traffic Density rows where neighborhood text leaked into the year field |
| 🔁 **Heavy Deduplication** | 960 duplicate `indicator_data_id` rows removed — over a third of the dataset |
| 📊 **Per-Indicator Statistics** | `groupby('name')` stats across 18+ distinct air-quality measures |
| 🧪 **Key Pollutant Focus** | Benzene, formaldehyde, and boiler NOx compared directly |
| 🗽 **Borough Ranking** | Bronx, Manhattan, Brooklyn, Queens, Staten Island ranked by average pollution |
| 📆 **Trend + Peak/Low Markers** | Line chart highlights the highest and lowest pollution years |
| 🎯 **Geo-Level Filtering** | Analysis scoped to `Borough` and `UHF42` neighborhood geography types |

---

## 🏗️ Project Structure

```
📦 nyc-air-quality-analysis/
│
├── 📄 nyc_air_quality_analysis.ipynb   ← Main analysis notebook
├── 📄 air-quality-1.csv                ← Source data (2,769 raw records)
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
│ 1. Rename, Repair & Dedupe    │  ← rename col, drop misaligned rows,
└──────────────┬────────────────┘     drop missing, drop 960 duplicates
               │
               ▼
┌─────────────────────────────┐
│ 2. Per-Indicator Statistics   │  ← groupby('name').describe()
└──────────────┬────────────────┘
               │
   ┌───────────┼────────────┬─────────────┐
   ▼           ▼             ▼
Pollutant   Borough       Temporal
Breakdown  Comparison       Trend
   (3)         (4)            (5)
```

---

## 🧹 1. Data Cleaning & Preparation

Renames the misleadingly-named `data_valuemessage` column, coerces it to numeric, filters out structurally misaligned Traffic Density rows, drops missing key fields, and removes duplicate indicator records.

**Logic:**
```python
df = df.rename(columns={'data_valuemessage': 'data_value'})
df['data_value'] = pd.to_numeric(df['data_value'], errors='coerce')

# A few CD-level Traffic Density rows have shifted fields
df = df[df['year_description'].str.contains(r'\d')]

df = df.dropna(subset=['geo_entity_name', 'Measure', 'data_value'])
df = df.drop_duplicates(subset=['indicator_data_id'])
```

**Sample Output:**
```
Dataset shape after removing misaligned rows: (2616, 9)
Missing values per column (key fields): 0
Number of duplicate rows found: 960
Dataset shape after removing duplicates: (1656, 9)
```

---

## 📊 2. Summary Statistics & Correlation

Groups by indicator `name` and computes `describe()` and mode across all 18+ air-quality measures — from air toxics concentrations to asthma-attributable hospitalizations.

**Sample Output (mode values, selected indicators):**
```
Air Toxics- Average Benzene Concentrations           2.8
Air Toxics- Average Formaldehyde Concentrations      3.2
Boiler Emissions- Total NOx Emissions                2.0
Neighborhood AQ- Fine Particulate Matter (PM2.5)     9.7
Neighborhood AQ- Nitrogen Dioxide (NO2)             20.9
Neighborhood AQ- Ozone (O3)                         27.1
PM2.5-Attributable Deaths                           40.5
```

---

## 🧪 3. Pollutant Concentration Breakdown

Filters to three key pollutants and compares their average concentration in a horizontal bar chart.

**Sample Output:**
```
Air Toxics- Average Benzene Concentrations          2.910417
Air Toxics- Average Formaldehyde Concentrations     3.195833
Boiler Emissions- Total NOx Emissions              56.300000
```

---

## 🗽 4. Borough-Level Comparison

Filters to borough-level geography and ranks all five NYC boroughs by average pollution value.

**Sample Output:**
```
Borough           Average Data Value
Bronx                  46.376471
Manhattan              41.344118
Brooklyn               30.023529
Queens                 22.832353
Staten Island          20.482353
```

---

## 📆 5. Temporal Trends Analysis

Filters to neighborhood-level (`UHF42`) fine-particulate and air-toxics measures, then plots the yearly average trend with the peak and lowest years marked directly on the line chart.

**Logic:**
```python
yearly_trend = neighborhood_air.groupby('year_description')['data_value'].mean()

peak = yearly_trend.idxmax()
low = yearly_trend.idxmin()
plt.scatter(peak, yearly_trend[peak], color='red', label=f'Peak: {peak}')
plt.scatter(low, yearly_trend[low], color='green', label=f'Lowest: {low}')
```

**Sample Output:**
```
2005                          3.066667
Annual Average 2009-2010     10.642857
```

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| 🐍 **Python** | 3.8+ | Core language |
| 📓 **Jupyter Notebook** | Any recent | Interactive analysis environment |
| 🐼 **Pandas** | Any recent | Cleaning, regex filtering, grouping |
| 🔢 **NumPy** | Any recent | Underlying numeric operations |
| 📊 **Matplotlib** | Any recent | Line and bar chart rendering |
| 🎨 **Seaborn** | Any recent | Styled bar charts |

---

## 📈 Results & Insights

- ✅ **1,656 Clean Records** — down from 2,769 raw rows after repairing misaligned data and removing 960 duplicates
- 🧪 **NOx Emissions Dominate** — boiler NOx (56.3 avg) far exceeds benzene (2.9) and formaldehyde (3.2) among the compared pollutants
- 🗽 **Bronx Has The Highest Average Pollution** (46.4), followed by Manhattan (41.3); Staten Island is lowest (20.5)
- 📆 **Pollution Rose Over Time** in the sampled neighborhood window — from a 2005 average of 3.07 to a 2009–2010 average of 10.64
- 🧹 **Duplication Was The Biggest Cleaning Issue** — over a third of raw rows were exact duplicate indicator entries

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 🧹 **Realistic Cleaning Challenge** | Handles shifted fields and heavy duplication, not just simple NaNs |
| 📊 **Indicator-Level Granularity** | Per-`name` statistics respect that this dataset mixes many different measures |
| 🗽 **Actionable Geography** | Borough-level ranking translates directly to policy-relevant insight |
| 📆 **Trend Highlighting** | Peak/low markers make the temporal chart interpretable at a glance |
| 📚 **Educational** | A strong example of cleaning a genuinely messy open-data CSV |
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

> *"Clean air starts with clean data — this notebook works on both."*

**🎓 Role:** Junior Python Developer | Programming Enthusiast \
**📍 Location:** India\
**🛠️ Skills:** Python · Pandas · NumPy · Seaborn · Exploratory Data Analysis

</div>

---

<div align="center">

---

*Made with ❤️ and ☕ — Last updated: 22 July, 2026*

</div>
