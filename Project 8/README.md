<div align="center">

# -- ! NumPy Analyzer ! --
### *Interactive Console-Based NumPy Array Toolkit*

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Array%20Operations-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![Console](https://img.shields.io/badge/Console-Interactive%20CLI-4CAF50?style=for-the-badge&logo=windowsterminal&logoColor=white)](https://www.python.org/)
[![OOP](https://img.shields.io/badge/Design-Class%20Based-9C27B0?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

<br/>

> *"An array is just numbers until you know how to slice, combine, and question it."*

</div>

---

## 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#️-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [🧱 Module 1 — Array Creation](#-module-1--array-creation)
- [🔍 Module 2 — Indexing & Slicing](#-module-2--indexing--slicing)
- [➕ Module 3 — Mathematical Operations](#-module-3--mathematical-operations)
- [🔗 Module 4 — Combine & Split](#-module-4--combine--split)
- [🔎 Module 5 — Search, Sort & Filter](#-module-5--search-sort--filter)
- [📊 Module 6 — Aggregates & Statistics](#-module-6--aggregates--statistics)
- [🖥️ Sample Run](#️-sample-run)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Results & Insights](#-results--insights)
- [🏆 Advantages](#-advantages)
- [📄 License](#-license)
- [👤 Author](#-author)

---

## 📌 Overview

The **NumPy Analyzer** is an interactive, menu-driven Python console application built around a single `DataAnalytic` class. It wraps core **NumPy** functionality — array creation, indexing/slicing, arithmetic, combining/splitting, searching/sorting/filtering, and statistical aggregation — behind one unified, class-based CLI.

This project is designed to:
- Practice **object-oriented design** with a stateful class holding one working array
- Explore **NumPy fundamentals**: creation, reshaping, indexing, and broadcasting
- Apply `match/case` for clean, readable menu routing
- Reinforce guard-clause patterns (`message_array()`) before operating on missing data

---

## 🎯 Problem Statement

> **Objective:** Build a console-based interactive tool for creating and analyzing NumPy arrays.

You are building a hands-on utility for exploring NumPy without writing a new script for every operation. A user should be able to create a 1D, 2D, or 3D array, then index it, slice it, run arithmetic against a second array, combine or split it, search/sort/filter its values, and compute statistics — all through one persistent menu.

| 📂 Feature | 📄 Type | 🔍 Description |
|------------|---------|-----------------|
| Array Creation | Sub-menu | Builds 1D, 2D, or 3D `np.array` from user input |
| Indexing & Slicing | Sub-menu | Access elements by index or 2D slice ranges |
| Mathematical Operations | Sub-menu | Elementwise add/sub/mul/div plus matrix multiplication |
| Combine & Split | Sub-menu | Vertical stacking and array splitting |
| Search, Sort & Filter | Sub-menu | `np.where`, `np.sort`, boolean filtering |
| Aggregates & Statistics | Sub-menu | Sum, mean, median, std deviation, variance |

The goal is to demonstrate **practical NumPy fluency** through a clean, class-based, menu-driven program.

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 🔁 **Infinite Main Menu Loop** | Program runs continuously until user selects Exit |
| 🧱 **Class-Based State** | A single `DataAnalytic` instance holds the current `_array` across all operations |
| 🧩 **6 Independent Sub-Menus** | Creation, Indexing/Slicing, Math, Combine/Split, Search/Sort/Filter, Stats |
| 🛡️ **Guard Clause Pattern** | `message_array()` blocks any operation until an array actually exists |
| 🔀 **`match/case` Control Flow** | Modern Python pattern matching for every menu level |
| 📐 **1D / 2D / 3D Support** | Arrays built and reshaped to any dimensionality via `.reshape()` |
| ➕ **Elementwise & Matrix Math** | Addition, subtraction, multiplication, division, and `np.dot` |
| 🔎 **Search/Sort/Filter** | `np.where`, ascending/descending `np.sort`, boolean masking |
| ⚠️ **Invalid Input Handling** | Every sub-menu reports invalid choices without crashing |

---

## 🏗️ Project Structure

```
📦 numpy-analyzer/
│
├── 📄 Analyzer.py            ← Main script: DataAnalytic class + entry point
│
└── 📄 README.md              ← Project documentation
```

---

## 🔄 Project Workflow

```
Program Start
      │
      ▼
┌─────────────────────────────┐
│      Display Main Menu       │  ← Options 1–7
└───────────────┬───────────────┘
                │
   ┌──────┬─────┼─────┬──────┬──────┐
   ▼      ▼     ▼     ▼      ▼      ▼
 Create Index  Math Combine Search Stats
 Array  /Slice  Ops  /Split /Sort  Aggr.
  (1)    (2)    (3)   (4)    (5)    (6)
   │      │      │     │      │      │
   ▼      ▼      ▼     ▼      ▼      ▼
        Guarded by message_array()
     (blocks 2–6 until array is created)
                │
                ▼
        Loop Back to Main Menu
                │
         (Choice: 7) Exit ✅
```

---

## 🧱 Module 1 — Array Creation

> Builds a 1D, 2D, or 3D NumPy array from space-separated input, reshaped to the requested dimensions.

**Logic:**
```python
data = input("Enter the Elements (Separated By Space): ")
self._array = np.array(data.split(), dtype=float)
```

**Sample Output (1D array):**
```
Enter the Elements (Separated By Space): 1 2 3 4 5

Array Created Successfully:
 [1. 2. 3. 4. 5.]
```

---

## 🔍 Module 2 — Indexing & Slicing

> Retrieves individual elements by index tuple, or extracts row/column ranges for 2D arrays.

**Logic:**
```python
idx = input("Enter Indices Separated By Space (e.g., '0 1'): ")
index = tuple(map(int, idx.split()))
print(f"Value At Index {index}: {self._array[index]}")
```

**Key Concepts Used:**

| Concept | Detail |
|---------|--------|
| 🔢 Tuple Indexing | `array[(row, col)]` style access for any dimension |
| ✂️ Range Slicing | `array[r_start:r_end, c_start:c_end]` for 2D arrays |
| 🛡️ Dimension Guard | Slicing path is gated to 2D arrays in this version |

---

## ➕ Module 3 — Mathematical Operations

> Performs elementwise addition, subtraction, multiplication, division against a second array of matching shape, plus true matrix multiplication via `np.dot`.

**Logic:**
```python
second_array = np.array(data.split(), dtype=float).reshape(self._array.shape)
print("\nResult Of Addition:\n", self._array + second_array)
```

**Key Concepts Used:**

| Concept | Detail |
|---------|--------|
| ➕➖✖️➗ Elementwise Ops | Broadcasting between two same-shaped arrays |
| 🔢 Matrix Multiplication | `np.dot(A, B)` with shape-compatibility checks |
| 📐 Reshape-on-Input | Second array reshaped to match the first automatically |

---

## 🔗 Module 4 — Combine & Split

> Vertically stacks two arrays together, or splits one array into equal parts.

**Logic:**
```python
print("\nCombined Array (Vertical Stack):\n", np.vstack((self._array, second_array)))
...
print("\nSplit Array:\n", np.array_split(self._array, splits))
```

**Key Concepts Used:**

| Concept | Detail |
|---------|--------|
| 🧱 `np.vstack` | Stacks arrays vertically into one combined array |
| ✂️ `np.array_split` | Divides an array into N (possibly uneven) parts |

---

## 🔎 Module 5 — Search, Sort & Filter

> Locates a value's indices, sorts ascending or descending, or filters values above a threshold.

**Logic:**
```python
indices = np.where(self._array == val)
sorted_arr = np.sort(self._array)
filtered = self._array[self._array > val]
```

**Key Concepts Used:**

| Concept | Detail |
|---------|--------|
| 🔎 `np.where` | Returns indices where a condition is true |
| ↕️ `np.sort` / `np.flip` | Ascending by default, flipped for descending |
| 🧮 Boolean Masking | `array[array > val]` filters values matching a condition |

---

## 📊 Module 6 — Aggregates & Statistics

> Computes core descriptive statistics — sum, mean, median, standard deviation, and variance — over the current array.

**Logic:**
```python
print(f"\nSum Of Array: {np.sum(self._array)}")
print(f"\nMean Of Array: {np.mean(self._array)}")
print(f"\nMedian Of Array: {np.median(self._array)}")
print(f"\nStandard Deviation Of Array: {np.std(self._array)}")
print(f"\nVariance Of Array: {np.var(self._array)}")
```

**Sample Output:**
```
Original Array:
 [1. 2. 3. 4. 5.]

Mean Of Array: 3.0
```

---

## 🖥️ Sample Run

A trimmed end-to-end session — creating a 1D array, computing its mean, then exiting:

```
Welcome To The NumPy Analyzer!
========================================

Choose An Option:
1. Create A Numpy Array
2. Slicing & Indexing Options
3. Perform Mathematical Operations
4. Combine Or Split Arrays
5. Search, Sort, Or Filter Arrays
6. Compute Aggregates And Statistics
7. Exit
Enter Your Choice: 1

Type Of Array To Create:
1. 1D Array
2. 2D Array
3. 3D Array
0. Exit
Enter Your Choice: 1
Enter the Elements (Separated By Space): 1 2 3 4 5

Array Created Successfully:
 [1. 2. 3. 4. 5.]

Choose An Option:
1. Create A Numpy Array
2. Slicing & Indexing Options
3. Perform Mathematical Operations
4. Combine Or Split Arrays
5. Search, Sort, Or Filter Arrays
6. Compute Aggregates And Statistics
7. Exit
Enter Your Choice: 6

Choose An Aggregate/Statistical Operation:
1. Sum
2. Mean
3. Median
4. Standard Deviation
5. Variance
6. Exit
Enter Your Choice: 2

Original Array:
 [1. 2. 3. 4. 5.]

Mean Of Array: 3.0

Choose An Option:
1. Create A Numpy Array
2. Slicing & Indexing Options
3. Perform Mathematical Operations
4. Combine Or Split Arrays
5. Search, Sort, Or Filter Arrays
6. Compute Aggregates And Statistics
7. Exit
Enter Your Choice: 7

Dhanyavad tamaro bav abhar che. 🙏
```

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| 🐍 **Python** | 3.10+ | Core language (`match/case` requires 3.10+) |
| 🔢 **NumPy** | Any recent | Array creation, reshaping, math, stats |
| 🧱 **OOP (Class-Based)** | Built-in | `DataAnalytic` class holds shared array state |
| 🔀 **match/case** | Built-in | Menu routing at every level |
| 🔁 **While Loop** | Built-in | Main menu and all sub-menu loops |
| 🖨️ **print() / input()** | Built-in | Console I/O and user interaction |

---

## 📈 Results & Insights

After running the program, the following outputs are produced:

- ✅ **1D/2D/3D Array Creation** — flexible shape via `.reshape()`
- 🔍 **Indexing & Slicing** — direct element access and 2D range slicing
- ➕ **Full Arithmetic Suite** — elementwise ops plus real matrix multiplication
- 🔗 **Combine/Split** — vertical stacking and equal-part splitting
- 🔎 **Search/Sort/Filter** — condition-based lookups, sorting, and masking
- 📊 **Descriptive Statistics** — sum, mean, median, std deviation, variance
- ⚠️ **Guarded Operations** — every module past creation checks `message_array()` first

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 🧱 **Stateful Design** | One array persists across every operation until replaced |
| 🎓 **Educational** | Touches nearly every core NumPy operation in one place |
| 🔄 **Reusable** | `DataAnalytic` class can be imported and extended independently |
| 🖥️ **Single Dependency** | Only requires NumPy — no other external libraries |
| ⚡ **Single-File Script** | Runs instantly from any terminal with NumPy installed |
| 🧪 **Extensible** | New operations can be added as new class methods and menu cases |
| 🛡️ **Guarded Access** | `message_array()` prevents operating on a non-existent array |
| 📖 **Readable Code** | Clear class methods, each scoped to one category of operations |

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


> *"NumPy turns loops into one-liners — this toolkit turns those one-liners into a menu."*

**🎓 Role:** Junior Python Developer | Programming Enthusiast \
**📍 Location:** India\
**🛠️ Skills:** Python · NumPy · OOP · CLI Applications · Data Analysis Fundamentals

</div>

---

<div align="center">

---

*Made with ❤️ and ☕ — Last updated: 14 July, 2026*

</div>
