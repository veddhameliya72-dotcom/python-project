<div align="center">

# -- ! Titanic Survival Analysis ! --
### *Exploratory Data Analysis Of Titanic Passenger Survival With Pandas & Seaborn*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Wrangling-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Viz-4C72B0?style=for-the-badge&logo=plotly&logoColor=white)](https://seaborn.pydata.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)

<br/>

> *"891 passengers, one night, and a dataset that still has lessons to teach."*

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
- [🚻 3. Demographic & Survival Insights](#-3-demographic--survival-insights)
- [🎫 4. Ticket Class & Economic Status](#-4-ticket-class--economic-status)
- [📉 5. Age Distribution & Outlier Analysis](#-5-age-distribution--outlier-analysis)
- [👨‍👩‍👧 6. Family Size & Behavioral Segmentation](#-6-family-size--behavioral-segmentation)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Results & Insights](#-results--insights)
- [🏆 Advantages](#-advantages)
- [📄 License](#-license)
- [👤 Author](#-author)

---

## 📌 Overview

**Titanic Survival Analysis** is a Jupyter Notebook that explores the classic Titanic `train.csv` dataset (891 passengers) to understand who survived and why. It moves through data cleaning, feature engineering (titles, family size), statistical summaries, and six demographic/economic breakdowns of survival.

This project is designed to:
- Practice **missing-value imputation** (median age, mode embarkation port, dropped cabin column)
- Extract a **new feature from free text** (passenger title from the `Name` column)
- Compute **survival rates by gender, class, age, and family size**
- Build a **correlation matrix** connecting survival to other numeric features
- Segment passengers into **Solo / Small Family / Large Family** groups and compare outcomes

---

## 🎯 Problem Statement

> **Objective:** Analyze the Titanic passenger manifest to understand which demographic and economic factors were associated with survival.

Given 891 passenger records with class, sex, age, fare, family relations, and survival outcome, the notebook must clean the data (handling missing ages, embarkation ports, and the mostly-empty cabin column), then answer: did gender or class predict survival, how did age factor in, and did traveling with family help or hurt your odds?

| 📂 Section | 📄 Type | 🔍 Description |
|------------|---------|-----------------|
| Data Cleaning | Pandas | Median-fill Age, mode-fill Embarked, drop Cabin |
| Title Extraction | Regex | Pulls Mr/Mrs/Miss/Master/etc. from the Name field |
| Summary Statistics | Pandas | `describe()` and mode for Age/Fare/SibSp/Parch |
| Correlation Matrix | Seaborn Heatmap | Survived vs. Pclass, Age, SibSp, Parch, Fare |
| Gender Analysis | groupby + Count Plot | Survival rate and counts by sex |
| Class Analysis | groupby + Count Plot | Survival rate and average fare by passenger class |
| Age Analysis | Histogram | Age distribution split by survival outcome |
| Family Segmentation | Custom Function + Bar | Solo / Small Family / Large Family survival probability |

The goal is to demonstrate a **complete, narrated EDA** on one of the most iconic tabular datasets in data science.

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 🧹 **Targeted Imputation** | Age filled with median, Embarked with mode, Cabin dropped (77% missing) |
| 🏷️ **Regex Feature Extraction** | Passenger titles (Mr, Mrs, Miss, Master, Dr, Rev, etc.) pulled from names |
| 📝 **Inline Markdown Findings** | Each analytical step is followed by a plain-language summary cell |
| 📊 **Correlation-Backed Claims** | Survival correlations with class and fare are quoted with actual coefficients |
| 🚻 **Gender Survival Gap** | Female survival rate (74.2%) vs. male (18.9%) computed directly |
| 🎫 **Class Economics** | Survival rate paired with average fare per passenger class |
| 📉 **Layered Histogram** | KDE-smoothed age distribution split by survival outcome |
| 👨‍👩‍👧 **Custom Family Segmentation** | `FamilySize`/`FamilyType` engineered via a user-defined function |

---

## 🏗️ Project Structure

```
📦 titanic-survival-analysis/
│
├── 📄 titanic_train_analysis.ipynb   ← Main analysis notebook
├── 📄 train.csv                      ← Source data (891 passengers)
│
└── 📄 README.md                      ← Project documentation
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
│ 1. Clean, Impute & Extract    │  ← fillna, drop Cabin, extract Title, dedupe
└──────────────┬────────────────┘
               │
               ▼
┌─────────────────────────────┐
│ 2. Stats & Correlation Matrix │  ← describe(), heatmap
└──────────────┬────────────────┘
               │
   ┌───────────┼────────────┬─────────────┬──────────────┐
   ▼           ▼             ▼             ▼
Gender      Class &       Age           Family Size
Survival    Fare        Distribution    Segmentation
  (3)        (4)           (5)             (6)
```

---

## 🧹 1. Data Cleaning & Preparation

Fills missing `Age` with the median, `Embarked` with the mode, drops the mostly-empty `Cabin` column, and extracts a `Title` feature from each passenger's name.

**Logic:**
```python
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
df = df.drop(columns=['Cabin'])

df['Title'] = df['Name'].str.extract(r',\s*([^\.]*)\.')
```

**Sample Output:**
```
Missing values before cleaning:
Age      177
Cabin    687
Embarked   2

Missing values after cleaning: 0 across all remaining columns

Title counts (top 4):
Mr       517
Miss     182
Mrs      125
Master    40

Number of duplicate rows found: 0
Dataset shape after removing duplicates: (891, 12)
```

---

## 📊 2. Summary Statistics & Correlation

Describes Age, Fare, SibSp, and Parch, then builds a correlation matrix linking `Survived` to Pclass, Age, SibSp, Parch, and Fare.

**Sample Output:**
```
              Age        Fare       SibSp       Parch
mean    29.361582   32.204208    0.523008    0.381594
std     13.019697   49.693429    1.102743    0.806057
min      0.420000    0.000000    0.000000    0.000000
max     80.000000  512.329200    8.000000    6.000000
```

> **Finding:** `Survived` has a moderate negative correlation with `Pclass` (-0.34) — passengers in lower classes were less likely to survive. `Fare` correlates positively with survival (0.26), reinforcing that wealthier passengers had better odds. `Age` shows only a weak negative correlation with survival.

---

## 🚻 3. Demographic & Survival Insights

Groups by sex to compute both raw survival counts and survival rate.

**Sample Output:**
```
Survived      0     1
Sex
female       81   233
male        468   109

Survival rate by gender:
female    0.742038
male      0.188908
```

---

## 🎫 4. Ticket Class & Economic Status

Groups by passenger class to compare survival rate against average fare paid.

**Sample Output:**
```
Pclass   Survival Rate   Average Fare
1            0.6296         84.15
2            0.4728         20.66
3            0.2424         13.68
```

---

## 📉 5. Age Distribution & Outlier Analysis

A KDE-smoothed histogram of age, split by survival outcome, plus a boxplot of fare by class to visualize the well-known first-class fare outliers.

**Logic:**
```python
sns.histplot(data=df, x='Age', hue='Survived', kde=True, bins=30, palette='coolwarm', element='step')
sns.boxplot(data=df, x='Pclass', y='Fare', palette='Set3')
```

---

## 👨‍👩‍👧 6. Family Size & Behavioral Segmentation

Engineers a `FamilySize` and categorical `FamilyType` (Solo / Small Family / Large Family), then compares survival probability across the three groups.

**Logic:**
```python
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1

def categorize_family(size):
    if size == 1:
        return 'Solo'
    elif 2 <= size <= 4:
        return 'Small Family'
    else:
        return 'Large Family'

df['FamilyType'] = df['FamilySize'].apply(categorize_family)
```

**Sample Output:**
```
Passenger count by family type:
Solo             537
Small Family     292
Large Family      62
```

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| 🐍 **Python** | 3.8+ | Core language |
| 📓 **Jupyter Notebook** | Any recent | Interactive analysis environment |
| 🐼 **Pandas** | Any recent | Cleaning, feature extraction, grouping |
| 🔢 **NumPy** | Any recent | Underlying numeric operations |
| 📊 **Matplotlib** | Any recent | Plot rendering and layout |
| 🎨 **Seaborn** | Any recent | Heatmap, count plots, histogram, boxplot, bar chart |
| 🔤 **Regex (`str.extract`)** | Built-in | Passenger title extraction from names |

---

## 📈 Results & Insights

- ✅ **891 Passengers Retained** after imputing Age/Embarked and dropping Cabin
- 🚻 **Gender Was The Strongest Signal** — women survived at 74.2% vs. men at 18.9%
- 🎫 **Class Mattered** — 1st class survival (62.96%) vs. 3rd class (24.24%), tracking average fare
- 📉 **Younger Passengers Skewed Toward Survival** in the age-distribution histogram
- 👨‍👩‍👧 **Small Families Fared Best** — traveling with 1–3 others outperformed both solo travelers and large families
- 🔥 **Correlation Confirms Intuition** — Pclass (-0.34) and Fare (+0.26) both correlate meaningfully with survival

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 📝 **Narrated Analysis** | Markdown "Finding" cells turn raw output into plain-language takeaways |
| 🏷️ **Feature Engineering** | Title extraction and family segmentation go beyond the raw columns |
| 🎯 **Targeted Imputation** | Each missing-value strategy is chosen per-column rather than blanket-dropped |
| 📊 **Multi-Angle Coverage** | Gender, class, age, and family size are each examined independently |
| 📚 **Educational** | A well-known dataset made an excellent template for demographic EDA |
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

> *"Even the most-analyzed dataset in data science still rewards asking one more question."*

**🎓 Role:** Junior Python Developer | Programming Enthusiast \
**📍 Location:** India\
**🛠️ Skills:** Python · Pandas · NumPy · Seaborn · Exploratory Data Analysis

</div>

---

<div align="center">

---

*Made with ❤️ and ☕ — Last updated: 22 July, 2026*

</div>
