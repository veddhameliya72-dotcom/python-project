<div align="center">

# 📊 Sales Data Analyzer
### *Interactive Python Console Application for Data Manipulation and Visualization*

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Library-Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Library-Matplotlib-11557c?style=for-the-badge)
![Seaborn](https://img.shields.io/badge/Library-Seaborn-4C72B0?style=for-the-badge)
![OOP](https://img.shields.io/badge/Concept-OOP-orange?style=for-the-badge)

</div>

---

# 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [📁 Load Dataset](#-load-dataset)
- [🔍 Explore Data](#-explore-data)
- [🧮 DataFrame Operations](#-dataframe-operations)
- [🛠️ Handle Missing Data](#️-handle-missing-data)
- [📊 Generate Statistics](#-generate-statistics)
- [📈 Data Visualization](#-data-visualization)
- [💾 Save Visualization](#-save-visualization)
- [🚫 Error Handling](#-error-handling)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Results & Insights](#-results--insights)
- [🏆 Advantages](#-advantages)
- [👤 Author](#-author)

---

# 📌 Overview

**Sales Data Analyzer** is a menu-driven Python application developed using **Pandas**, **Matplotlib**, **Seaborn**, and **Object-Oriented Programming (OOP)**. It allows users to load CSV datasets, explore data structures, manipulate specific fields, handle missing values, and generate comprehensive visual insights through an interactive console interface.

---

# 🎯 Problem Statement

Build a console-based application that demonstrates practical data science workflows—from data ingestion and cleaning to statistical analysis and visualization—while applying robust OOP principles such as encapsulation, state management, and reusable class methods.

---

# ✨ Key Features

| Feature | Description |
|---------|-------------|
| 📁 Load Data | Read CSV datasets safely into Pandas DataFrames |
| 🔍 Explore Data | View head/tail, schema, datatypes, and column details |
| 🧮 Data Operations | Search, sort by sales, filter by region, and aggregate |
| 🛠️ Missing Data | Detect, drop, or fill null values (mean or custom) |
| 📊 Statistics | Generate descriptive stats, variance, std dev, and quantiles |
| 📈 Visualization | Create Bar, Line, Scatter, Histograms, and Pie Charts |
| 💾 Save Plots | Export the most recently generated plot to an image file |
| 🛡️ Error Handling | Gracefully handles invalid inputs and missing columns |

---

# 🏗️ Project Structure

```text
📦 Project_9/
│── 📂 sales_dataset.csv
│── 📷 piechart.png
│── 📄 sales_analyzer.py
└── 📄 README.md
```

---

# 🔄 Project Workflow

```text
Start
  │
  ▼
Welcome Screen
  │
  ├── 1. Load Dataset
  ├── 2. Explore Data
  ├── 3. Perform DataFrame Operations
  ├── 4. Handle Missing Data
  ├── 5. Generate Descriptive Statistics
  ├── 6. Data Visualization
  ├── 7. Save Visualization
  └── 0. Exit
```

---

# 📁 Load Dataset

- Securely parse `.csv` files
- Error handling for missing or unreadable files
- Initialize the state for DataFrame operations

---

# 🔍 Explore Data

- Display First 5 Rows (`df.head()`)
- Display Last 5 Rows (`df.tail()`)
- View Column Names
- Check Data Types
- Display Basic Info (`df.info()`)

---

# 🧮 DataFrame Operations

- Search for specific Product Names using string contains
- Sort datasets based on highest Sales
- Filter datasets by specific Region queries
- Aggregate data (Sum, Mean, Count) grouped by Region


---

# 🛠️ Handle Missing Data

- Identify and count total missing values (`isna().sum()`)
- Fill numerical missing values with column averages
- Drop rows containing any missing data
- Replace missing data with custom user input

---

# 📊 Generate Statistics

- Basic Descriptive Statistics (`df.describe()`)
- Calculate Standard Deviation and Variance
- Calculate 25th and 75th Percentile Quantiles

### Output


---

# 📈 Data Visualization

- **Bar Plot**: Total Sales by Region
- **Line Plot**: Sales trends over Years
- **Scatter Plot**: Custom X and Y axis correlations (e.g., Seaborn plots)
- **Histogram**: Sales spread and frequency
- **Pie Chart**: Regional Sales Share percentage

### Output


---

# 💾 Save Visualization

- Automatically tracks the last generated Matplotlib figure
- Allows users to export and save plots directly to `.png` or `.jpg` formats

---

# 🚫 Error Handling

- Missing dataset restrictions (prompts user to load data first)
- Invalid menu or submenu numerical selections
- Handled `ValueError` for string inputs in numeric prompts
- Safely checks for column existence (e.g., verifying 'Sales' or 'Region' exist before plotting)

---

# 🛠️ Tech Stack

| Technology | Purpose |
|-----------|---------|
| 🐍 Python | Core Programming Language |
| 🐼 Pandas | DataFrame Management & Analysis |
| 🔢 NumPy | Numerical computations |
| 📉 Matplotlib | Base Plotting & Charting |
| 📊 Seaborn | Advanced Statistical Graphics |
| 🧱 OOP | Program Architecture & State Management |

---

# 📈 Results & Insights

- ✅ End-to-end data processing lifecycle inside a single application
- ✅ Highly modular OOP-based implementation
- ✅ Intuitive and robust interactive terminal interface
- ✅ Deep integration of Pandas manipulation and Seaborn visualization
- ✅ Secure exception handling for unpredictable user inputs

---

# 🏆 Advantages

| Advantage | Description |
|----------|-------------|
| 🎓 Educational | Great demonstration of Data Science fundamentals |
| ⚡ Efficient | Leverages vectorized Pandas/NumPy operations |
| 🛡️ Safe | Comprehensive fallback conditions and data checks |
| 🔄 Reusable | The `SalesDataAnalyzer` class can be imported elsewhere |
| 🖼️ Visual | Connects terminal commands directly to rich GUI charts |

---

# 👤 Author

<div align="center">

**Ved Dhameliya**

🎓 Python Sales Data Analyzer Project

---

### ⭐ Thank You For Visiting This Project ⭐

Made with ❤️ using Python, Pandas & Matplotlib

</div>
