<div align="center">

# -- ! Journal File Operator ! --
### *Interactive Console-Based Personal Journal with File Handling & Exception Management*

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FileIO](https://img.shields.io/badge/File-Read%2FWrite%2FAppend-FF6F00?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Console](https://img.shields.io/badge/Console-Interactive%20CLI-4CAF50?style=for-the-badge&logo=windowsterminal&logoColor=white)](https://www.python.org/)
[![Exceptions](https://img.shields.io/badge/Error-Custom%20Exceptions-9C27B0?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

<br/>

> *"A journal is a record not just of days, but of how you chose to spend them."*

</div>

---

## 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#️-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [⚠️ Custom Exceptions](#️-custom-exceptions)
- [➕ Operation 1 — Create a File](#-operation-1--create-a-file)
- [📝 Operation 2 — Add a New Entry](#-operation-2--add-a-new-entry)
- [📖 Operation 3 — View All Entries](#-operation-3--view-all-entries)
- [🔍 Operation 4 — Search for an Entry](#-operation-4--search-for-an-entry)
- [🗑️ Operation 5 — Delete Entries](#️-operation-5--delete-entries)
- [🚪 Operation 6 — Exit](#-operation-6--exit)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Results & Insights](#-results--insights)
- [🏆 Advantages](#-advantages)
- [📄 License](#-license)
- [👤 Author](#-author)
- [🙏 Acknowledgements](#-acknowledgements)

---

## 📌 Overview

The **Journal File Operator** is a console-based interactive Python application that demonstrates **file handling** (create, read, append, write), **exception handling** with both built-in and custom exceptions, and **match-case** driven menu navigation. The program lets the user maintain a personal journal stored in a text file, with the ability to add, view, search, and delete entries — all through a clean CLI menu.

This project is designed to:
- Strengthen understanding of Python file I/O — `open()` modes `"x"`, `"a"`, `"r"`, `"w"`
- Practice exception handling using both built-in (`FileExistsError`, `FileNotFoundError`) and custom exceptions
- Apply CRUD-style logic (Create, Read, Search, Delete) to persist real data on disk
- Use Python's `match-case` for clean, structured menu control flow

---

## 🎯 Problem Statement

> **Objective:** Build a console-based journal application that persists entries to a text file, allowing the user to create the journal file, add timestamped entries, view all entries, search by date or keyword, and clear all entries — entirely through file operations.

| 📂 Feature | 📄 Type | 🔍 Description |
|------------|---------|----------------|
| Create File | File Creation | Creates a new journal text file if one doesn't exist |
| Add Entry | File Append | Appends a timestamped journal entry to the file |
| View Entries | File Read | Reads and prints the full journal file content |
| Search Entry | File Read + Filter | Searches journal lines by date/time or keyword |
| Delete Entries | File Overwrite | Clears all journal content by overwriting the file |

The goal is to demonstrate **practical file handling and exception management** through a real-world personal journaling tool.

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 🔁 **Infinite Menu Loop** | Program runs continuously until user selects Exit |
| 📁 **File Creation Safety** | Uses `"x"` mode to avoid overwriting an existing journal file |
| 📝 **Timestamped Entries** | Each entry stores a Date/Time stamp alongside the journal text |
| 📖 **Full File Read** | Displays the entire journal content in a readable format |
| 🔍 **Nested Search Menu** | Sub-menu to search entries by date/time or by keyword |
| 🗑️ **Safe Deletion** | Confirms with the user before clearing all journal entries |
| ⚠️ **Custom Exceptions** | `No_Content` and `wrong_choice` exceptions handle edge cases |
| 🖥️ **CLI Interface** | Clean text-based menu for user interaction |

---

## 🏗️ Project Structure

```
📦 journal-file-operator/
│
├── 📄 file_operator.py      ← Main Python script (entry point)
├── 📄 README.md             ← Project documentation
│
└── 📁 assets/               ← Output screenshots
    ├── 🖼️ output_1_create_file.png
    ├── 🖼️ output_2_add_entry.png
    ├── 🖼️ output_3_view_entries.png
    ├── 🖼️ output_4_search_by_date.png
    ├── 🖼️ output_5_search_by_keyword.png
    ├── 🖼️ output_6_search_exit.png
    ├── 🖼️ output_7_delete_entries.png
    └── 🖼️ output_8_exit.png
```

---

## 🔄 Project Workflow

```
Program Start
      │
      ▼
┌─────────────────────────────────┐
│       Display Main Menu         │  ← Options: 1-Create / 2-Add / 3-View
│                                 │     4-Search / 5-Delete / 6-Exit
└──────────────┬──────────────────┘
               │
   ┌───────────┼─────────────────────────────┐
   ▼           ▼              ▼               ▼
┌──────┐   ┌──────┐      ┌────────┐      ┌────────┐
│  1   │   │  2   │      │   3    │      │   4    │
│Create│   │ Add  │      │  View  │      │ Search │
└──┬───┘   └──┬───┘      └───┬────┘      └───┬────┘
   │          │              │               │
   ▼          ▼              ▼               ▼
open(x)    Input Date    open(r) →      Sub-menu:
mode →     + Entry →     read() →       1-Date/Time
create     append to     print          2-Keyword
file       file          content        3-Exit
                                            │
                                       Filter lines
                                       & print matches
               │
        ┌──────┴──────┐
        ▼             ▼
    ┌──────┐      ┌──────┐
    │  5   │      │  6   │
    │Delete│      │ Exit │
    └──┬───┘      └──────┘
       │
   Confirm (yes/no)
   open(w) → clears file
       │
   Loop Back to Menu
       │
  (Choice: 6) Exit ✅
```

---

## ⚠️ Custom Exceptions

The program defines two custom exception classes to handle specific edge cases beyond Python's built-in exceptions:

```python
class No_Content(Exception):
    pass

class wrong_choice(Exception):
    pass
```

| Exception | Raised When | Purpose |
|-----------|-------------|---------|
| `No_Content` | The journal file is read but contains no text | Signals an empty journal distinctly from a missing file |
| `wrong_choice` | The user enters a menu option outside the valid range | Signals invalid menu navigation at any level |

Combined with built-in exceptions like `FileExistsError` and `FileNotFoundError`, the program handles file-related edge cases gracefully without crashing.

---

## ➕ Operation 1 — Create a File

### 📝 What it does

Prompts the user for confirmation, then attempts to create a new journal file in exclusive **`"x"`** mode — which raises `FileExistsError` automatically if the file already exists, preventing accidental data loss.

**Logic:**
```python
def Create_file():
    choice = input("Do want to create a file (Yes/No):").lower()
    if choice == "yes":
        try:
            file = open(File_name, "x")
            file.close
            print("File created successfully.....................")
        except FileExistsError:
            print("There is a file which Exists......")
```

**Output:**

![Create File Output](assets/output_1_create_file.png)

---

## 📝 Operation 2 — Add a New Entry

### ✍️ What it does

Collects a date/time stamp and journal text from the user, then **appends** (`"a"` mode) a formatted entry to the journal file — preserving all previously saved entries.

**Fields Collected:**

| Field | Type | Example |
|-------|------|---------|
| `Date` | str | 27-10-2020 |
| `Entry` | str | hii i am learning python |

**Logic:**
```python
def Add_Entry():
    try:
        Date = input("Enter Date and Time (DD-MM_YY::00:0 am/pm) : ")
        Entry = input("Enter your journal Entry: ")
        file = open(File_name, "a")
        file.write("\n\nDate & Time : " + Date + "\n")
        file.write("Entry       : " + Entry + "\n\n")
        file.close()
        print("Entry Added successfully.....................")
    except FileNotFoundError:
        print("Create a file for Journal")
```

**Output:**

![Add Entry Output](assets/output_2_add_entry.png)

---

## 📖 Operation 3 — View All Entries

### 👁️ What it does

Opens the journal file in **read (`"r"`)** mode and prints its full content. If the file is empty, raises the custom `No_Content` exception (entries exist, so this path isn't shown here, but it guards against a blank journal).

**Logic:**
```python
def Read_file():
    try:
        file = open(File_name, "r")
        content = file.read()
        if content == "":
            raise No_Content()
        else:
            print("FILE CONTEXT:")
            print(content)
            print("END")
        file.close
    except FileNotFoundError:
        print("Create a file for Journal")
```

**Output:**

![View Entries Output](assets/output_3_view_entries.png)

---

## 🔍 Operation 4 — Search for an Entry

### 🔎 What it does

Opens a nested sub-menu with its own `match-case` block, letting the user search journal entries either by **date/time** or by **keyword**. Reads all lines from the file and prints matching lines.

**Sub-Menu Options:**

| Choice | Action |
|--------|--------|
| 1 | Search by Date/Time |
| 2 | Search by Keyword |
| 3 | Exit search sub-menu |

**Logic:**
```python
def Search_Entry():
    while True:
        choice = int(input("Enter your choice:"))
        match choice:
            case 1:
                file = open(File_name, "r")
                lines = file.readlines()
                file.close()
                Date_time = input("Enter Date and Time (DD-MM_YY::00:0 am/pm) : ")
                for line in lines:
                    if Date_time or "Entry" in line:
                        print(line)
            case 2:
                keyword = input("Enter the Keyword:")
                for line in lines:
                    if keyword or "Date & Time" in line:
                        print(line)
            case 3:
                print("Exited from Search Entries....")
                break
```

**Output — Search by Date/Time:**

![Search by Date Output](assets/output_4_search_by_date.png)

**Output — Search by Keyword:**

![Search by Keyword Output](assets/output_5_search_by_keyword.png)

**Output — Exit Search Sub-Menu:**

![Search Exit Output](assets/output_6_search_exit.png)

---

## 🗑️ Operation 5 — Delete Entries

### ❌ What it does

Asks for confirmation, then opens the journal file in **write (`"w"`)** mode — which truncates the file completely, clearing all stored entries.

**Logic:**
```python
def clear_all():
    try:
        choice = input("\nAre you sure you want to delete all entries? (yes/no): ")
        if choice.lower() == "yes":
            file = open(File_name, "w")
            file.close()
            print("\nAll entries deleted successfully!")
        else:
            print("\nDeletion cancelled.")
    except FileNotFoundError:
        print("\nJournal file does not exist.")
```

**Output:**

![Delete Entries Output](assets/output_7_delete_entries.png)

---

## 🚪 Operation 6 — Exit

### 🛑 What it does

Breaks out of the infinite `while True` loop, printing a farewell message and terminating the program cleanly.

**Logic:**
```python
case 6:
    print("HAVE A NICE DAY.....................HAVE A GOOD DAY....................HAVE WONDERFULLL DAY")
    break
```

**Output:**

![Exit Output](assets/output_8_exit.png)

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| 🐍 **Python** | 3.10+ | Core programming language |
| 📁 **File I/O** | Built-in | `open()` with `"x"`, `"a"`, `"r"`, `"w"` modes |
| ⚠️ **Custom Exceptions** | Built-in OOP | `No_Content`, `wrong_choice` classes |
| 🔁 **While Loop** | Built-in | Infinite menu loop control |
| 🔀 **Match-Case** | Python 3.10+ | Structural pattern matching for menu control |
| 🖨️ **print() / input()** | Built-in | Console I/O and user interaction |

---

## 📈 Results & Insights

After running the program, the following operations are demonstrated:

- ✅ **File Created** — Journal text file created safely using exclusive `"x"` mode
- 📝 **Entry Added** — Timestamped entry appended without disturbing existing content
- 📖 **Entries Viewed** — Full journal content read and displayed cleanly
- 🔍 **Entries Searched** — Matching lines found via date/time or keyword lookup
- 🗑️ **Entries Deleted** — Journal file cleared after user confirmation
- 🚪 **Clean Exit** — Program terminates gracefully with a farewell message
- ⚠️ **Error Feedback** — File and menu errors handled via built-in and custom exceptions

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 🎓 **Beginner Friendly** | Covers file handling, exceptions, and menu logic in one project |
| 📁 **Real File Persistence** | Data survives across program runs, unlike in-memory lists |
| ⚠️ **Robust Error Handling** | Combines built-in and custom exceptions for clear feedback |
| 🔄 **Real-World Logic** | Mirrors an actual personal journaling/diary application |
| 🖥️ **No Dependencies** | Runs with pure Python — no external libraries needed |
| ⚡ **Lightweight** | Single-file script, instantly runnable from any terminal |
| 🧪 **Extensible** | Easy to add features like entry editing, sorting, or encryption |
| 📖 **Readable Code** | Clear `match-case` structure makes logic easy to follow |

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

[![GitHub](https://img.shields.io/badge/GitHub-ved--dhameliya-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ved-dhameliya)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ved-dhameliya/)

> *"Every entry starts with a single line — just like every habit starts with a single day."*

**🎓 Role:** Junior Python Developer | Programming Enthusiast \
**📍 Location:** India \
**🛠️ Skills:** Python · File Handling · Exception Handling · CLI Applications

</div>

---

## 🙏 Acknowledgements

Special thanks to the following resources and communities that made this project possible:

- 📚 [Python Official Docs](https://docs.python.org/3/) — Official Python language reference
- 📁 [Real Python — File I/O](https://realpython.com/read-write-files-python/) — In-depth file handling tutorials
- ⚠️ [Python Docs — Exceptions](https://docs.python.org/3/tutorial/errors.html) — Built-in and custom exception handling
- 🔀 [PEP 634 — Match-Case](https://peps.python.org/pep-0634/) — Structural Pattern Matching specification
- 🖥️ [W3Schools Python](https://www.w3schools.com/python/) — Beginner Python reference
- 💬 [Stack Overflow Community](https://stackoverflow.com/) — Problem-solving support

---

<div align="center">

---

*Made with ❤️ and ☕ — Last updated: 18 June, 2026*

</div>
