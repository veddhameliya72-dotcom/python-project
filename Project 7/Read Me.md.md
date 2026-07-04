<div align="center">

# -- ! Multi-Utility Toolkit ! --
### *A Menu-Driven Python Toolkit for Date-Time, Math, Randomization, UUIDs & File Ops*

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Modules](https://img.shields.io/badge/Modules-Custom%20Package-FF6F00?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Console](https://img.shields.io/badge/Console-Interactive%20CLI-4CAF50?style=for-the-badge&logo=windowsterminal&logoColor=white)](https://www.python.org/)
[![Match](https://img.shields.io/badge/Control%20Flow-match%2Fcase-9C27B0?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

<br/>

> *"One toolkit, many tools — from timestamps to passwords, all behind a single menu."*

</div>

---

## 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#️-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [🕒 Module 1 — Date & Time Operations](#-module-1--date--time-operations)
- [🔢 Module 2 — Mathematical Operations](#-module-2--mathematical-operations)
- [🎲 Module 3 — Random Data Generation](#-module-3--random-data-generation)
- [🆔 Module 4 — UUID Generator](#-module-4--uuid-generator)
- [📁 Module 5 — File Operations](#-module-5--file-operations)
- [🔍 Module 6 — Explore Module Attributes](#-module-6--explore-module-attributes)
- [🖥️ Full Sample Run](#️-full-sample-run)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Results & Insights](#-results--insights)
- [🏆 Advantages](#-advantages)
- [📄 License](#-license)
- [👤 Author](#-author)

---

## 📌 Overview

The **Multi-Utility Toolkit** is an interactive, menu-driven Python console application built as a custom package of reusable modules. It brings together six independent utilities — date/time tools, math operations, random data generation, UUID creation, file handling, and module introspection — behind one unified `match/case` driven menu.

This project is designed to:
- Demonstrate **modular Python package design** (`__init__.py` + submodules)
- Practice **nested menu loops** using `while True` and `match/case`
- Apply the standard library across real tasks — `datetime`, `math`, `random`, `uuid`, file I/O
- Show **introspection** in action using `dir()` to list a module's public functions

---

## 🎯 Problem Statement

> **Objective:** Build a single console-based toolkit that consolidates several everyday utility operations behind one interactive menu.

You are building a personal utility package that a user can launch once and use for many unrelated tasks — checking the time, doing quick math, generating random values, creating unique IDs, or reading/writing files — without leaving the program.

| 📂 Module | 📄 Type | 🔍 Description |
|-----------|---------|-----------------|
| Date-Time Operations | Sub-menu | Current time, date difference, formatting, stopwatch, countdown |
| Mathematical Operations | Sub-menu | Factorial, compound interest, trigonometry, area calculation |
| Random Data Generation | Sub-menu | Random integer, random list, password, OTP |
| UUID Generator | Direct action | Generates a UUID4 identifier |
| File Operations | Sub-menu | Create, write, read, append files |
| Module Explorer | Direct action | Lists public functions of every module via `dir()` |

The goal is to demonstrate **modular design, nested control flow, and standard-library fluency** through one cohesive interactive program.

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 🔁 **Infinite Main Menu Loop** | Program runs continuously until user selects Exit |
| 🧩 **6 Independent Modules** | Each utility lives in its own file, imported as a package |
| 🔂 **Nested Sub-Menus** | Every major option opens its own `while True` sub-menu |
| 🖥️ **CLI Interface** | Clean, numbered text menus at every level |
| 🧠 **`match/case` Control Flow** | Modern Python pattern matching instead of long `if-elif` chains |
| ⚠️ **Input Validation** | Invalid menu and numeric-input errors are caught and reported |
| 🔍 **Self-Introspection** | `dir()`-based explorer lists every callable function per module |
| 📦 **Reusable Package Layout** | `__init__.py` re-exports all submodules for clean imports |

---

## 🏗️ Project Structure

```
📦 multi-utility-toolkit/
│
├── 📄 Moduler_And_Packager.py   ← Main entry point / menu driver
│
├── 📦 Modules/
│   ├── 📄 __init__.py           ← Package initializer, re-exports submodules
│   ├── 📄 date_time.py          ← Date & time operations
│   ├── 📄 mathemetic.py         ← Mathematical operations
│   ├── 📄 random_num.py         ← Random data generation
│   ├── 📄 uuid_gene.py          ← UUID generation
│   ├── 📄 file_op.py            ← File create/write/read/append
│   └── 📄 dir_modul.py          ← Module attribute explorer
│
└── 📄 README.md                 ← Project documentation
```

---

## 🔄 Project Workflow

```
Program Start
      │
      ▼
┌───────────────────────────────┐
│      Display Main Menu        │  ← Options 1–7
└───────────────┬────────────────┘
                │
   ┌─────┬──────┼──────┬─────┬─────┐
   ▼     ▼      ▼      ▼     ▼     ▼
 Date  Math   Random  UUID  File  Dir
 Time  Ops    Data    Gen   Ops   Explore
 (1)   (2)    (3)     (4)   (5)   (6)
   │     │      │             │
   ▼     ▼      ▼             ▼
 Sub-menu loops for 1, 2, 3, and 5
 (each runs until "Back To Main Menu")
                │
                ▼
        Loop Back to Main Menu
                │
         (Choice: 7) Exit ✅
```

---

## 🕒 Module 1 — Date & Time Operations

Handles everything time-related: current timestamp, date-difference calculation, format switching, a live stopwatch, and a countdown timer.

**Sample interaction:**
```
Current Date = 04/07/2026
Current Time = 11:21:52
```

```
Enter The First Date (DD/MM/YYYY): ...
Enter The Second Date (DD/MM/YYYY): ...
Difference is: 549
```

```
choosen format: 2026/07/04
```

---

## 🔢 Module 2 — Mathematical Operations

Covers factorials, compound interest, trigonometric ratios, and area calculations for rectangles/triangles.

**Sample interaction:**
```
Factorial Of '5' is: 120

The Total Amount After 2.0 Years Is: 1102.5
The Total Interest Earned Is: 102.5

Sine of 30°: 0.49999999999999994
Cosine of 30°: 0.8660254037844387
Tangent of 30°: 0.5773502691896257

The area of the rectangle is: 50.0
```

---

## 🎲 Module 3 — Random Data Generation

Generates random integers, random lists, passwords, and OTPs using the `random` module.

**Sample interaction:**
```
Random Integer is: 41

Generated List: [49, 21, 3, 11, 34]

Your random password is: mDYHS65ybN

Your Generated OTP is: 517728
```

---

## 🆔 Module 4 — UUID Generator

A single-action option that generates a version-4 UUID using Python's built-in `uuid` module.

**Sample interaction:**
```
Generated UUID is: 4a922965-67cc-47e6-a13e-bac2c10c1b3f
```

---

## 📁 Module 5 — File Operations

Basic file handling: create, write, read, and append — each wrapped in its own sub-menu option.

**Sample interaction:**
```
File sample.txt Created Successfully...............

Content is been uploaded successfully...............

Hello from the toolkit demo

Content Appended Successfully.................................
```

---

## 🔍 Module 6 — Explore Module Attributes

Uses Python's built-in `dir()` to introspect every module in the package and print its public (non-dunder) functions — a handy way to see the whole toolkit's API surface at a glance.

**Sample interaction:**
```
--- Available Module Attributes ---

Functions In 'date_time':
 - count_down
 - current_time
 - date_difference
 - formate_date
 - stop_watch

Functions In 'mathemetic':
 - Trigonometri
 - cal_factorial
 - calculate_area
 - compound_interest

Functions In 'random_num':
 - generate_otp
 - generate_password
 - random_list
 - random_num

Functions In 'file_op':
 - append_file
 - create_file
 - read_file
 - write_file

Functions In 'uuid':
 - generate_uuid
```

---

## 🖥️ Full Sample Run

A complete end-to-end run touching every module, straight from `sample_run_output.txt`:

```
========================================
Welcome To Multi-Utility Toolkit
========================================
Choose An Option:
1. Date-Time And Time Operation
2. Mathemetical Operation
3. Random Data Generation
4. Generate Unique Identifiers (UUID)
5. File Operations (Custome Module)
6. Explore Module Atrribute dir()
7. Exit
========================================
Enter Your Choice:
...
Choose An Option:
1. Date-Time And Time Operation
2. Mathemetical Operation
3. Random Data Generation
4. Generate Unique Identifiers (UUID)
5. File Operations (Custome Module)
6. Explore Module Atrribute dir()
7. Exit
========================================
Enter Your Choice: Thanks for using this program 😊
You can give 10 marks if are satisfied with this program 😁
```

> 📄 See `sample_run_output.txt` in the repo for the unabridged transcript covering all six modules in one session.

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| 🐍 **Python** | 3.10+ | Core language (`match/case` requires 3.10+) |
| 🔁 **While Loop** | Built-in | Main menu and every sub-menu loop |
| 🔀 **match/case** | Built-in | Menu routing instead of `if-elif` chains |
| 📅 **datetime / time** | Built-in | Timestamps, date math, stopwatch, countdown |
| 🧮 **math** | Built-in | Factorial, trig functions, `pow()` |
| 🎲 **random** | Built-in | Integers, lists, passwords, OTPs |
| 🆔 **uuid** | Built-in | UUID4 generation |
| 📁 **open() / file I/O** | Built-in | Create, write, read, append |
| 🔍 **dir()** | Built-in | Module introspection |

---

## 📈 Results & Insights

After running the program, the following outputs are produced:

- ✅ **6 Independent Utilities** accessible from one main menu
- 🕒 **Date/Time Tools** — timestamps, differences, formats, stopwatch, countdown
- 🔢 **Math Tools** — factorials, compound interest, trig ratios, shape areas
- 🎲 **Random Tools** — integers, lists, passwords, OTPs on demand
- 🆔 **Instant UUIDs** generated with a single menu choice
- 📁 **File I/O** — create, write, read, append, all from the console
- 🔍 **Live Module Map** — `dir()` explorer prints every public function per module
- ⚠️ **Error Feedback** — invalid menu choices are caught and reported at every level

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 🧩 **Modular** | Each utility is a separate file, imported cleanly via `__init__.py` |
| 🔄 **Reusable** | Any module can be imported independently in other projects |
| 📚 **Educational** | Demonstrates package structure, `match/case`, and nested loops together |
| 🖥️ **No External Dependencies** | Built entirely on the Python standard library |
| ⚡ **Single Entry Point** | One script (`Moduler_And_Packager.py`) drives the whole toolkit |
| 🧪 **Extensible** | New modules can be added and wired into the menu with minimal changes |
| 🔍 **Self-Documenting** | The `dir()` explorer doubles as built-in API documentation |
| 🛡️ **Input Safety** | Invalid choices are caught with `try/except` and `case _` fallbacks |

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

> *"A good toolkit doesn't do one thing well — it does many things simply."*

**🎓 Role:** Junior Python Developer | Programming Enthusiast \
**📍 Location:** India\
**🛠️ Skills:** Python · Modular Packages · CLI Applications · Standard Library · match/case

</div>

---

<div align="center">

---

*Made with ❤️ and ☕ — Last updated: 04 July, 2026*

</div>
