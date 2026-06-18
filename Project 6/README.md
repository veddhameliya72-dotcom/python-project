<div align="center">

# -- ! Journal File Operator ! --
### *Interactive Console-Based Personal Journal & File Management System*

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![File I/O](https://img.shields.io/badge/File-Read%20%2F%20Write%20%2F%20Append-FF6F00?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Console](https://img.shields.io/badge/Console-Interactive%20CLI-4CAF50?style=for-the-badge&logo=windowsterminal&logoColor=white)](https://www.python.org/)
[![Exception](https://img.shields.io/badge/Exceptions-Custom%20%26%20Built--in-9C27B0?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

<br/>

> *"A journal is not just a file — it's a record of every thought you dared to write down."*

</div>

---

## 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#️-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [📂 Operation 1 — Create File](#-operation-1--create-file)
- [✍️ Operation 2 — Add Entry](#️-operation-2--add-entry)
- [👁️ Operation 3 — View All Entries](#️-operation-3--view-all-entries)
- [🔍 Operation 4 — Search for an Entry](#-operation-4--search-for-an-entry)
- [🗑️ Operation 5 — Delete All Entries](#️-operation-5--delete-all-entries)
- [🚪 Operation 6 — Exit](#-operation-6--exit)
- [⚠️ Custom Exception Handling](#️-custom-exception-handling)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Results & Insights](#-results--insights)
- [🏆 Advantages](#-advantages)
- [📄 License](#-license)
- [👤 Author](#-author)
- [🙏 Acknowledgements](#-acknowledgements)

---

## 📌 Overview

The **Journal File Operator** is an intermediate-level, interactive Python console application that demonstrates core **File Handling** and **Exception Handling** concepts including **file creation**, **reading**, **writing**, **appending**, **searching**, and **clearing** file content. The program presents a clean menu-driven interface that runs continuously until the user chooses to exit.

This project is designed to:
- Demonstrate Python's built-in file I/O modes (`x`, `a`, `r`, `w`)
- Practice **custom exception classes** and built-in exception handling (`FileNotFoundError`, `FileExistsError`)
- Apply **function-based modular design** — each operation is a separate function
- Use Python's `match-case` for clean, structured control flow
- Build a real-world mini application — a **personal journal manager**

---

## 🎯 Problem Statement

> **Objective:** Build a console-based file management tool that acts as a personal journal — create, write, read, search, and delete journal entries stored in a `.txt` file.

You are building a file-backed journal utility for students learning Python file handling. The program must allow users to create a journal file, write timestamped entries to it, read all entries, search entries by date or keyword, and wipe entries when needed.

| 📂 Operation | 📄 Mode | 🔍 Description |
|-------------|---------|----------------|
| Create File | `"x"` | Creates a new file; raises error if already exists |
| Add Entry | `"a"` | Appends a dated journal entry to the file |
| View Entries | `"r"` | Reads and displays full file content |
| Search by Date | `"r"` | Reads lines and filters by date/time input |
| Search by Keyword | `"r"` | Reads lines and filters by keyword input |
| Delete All Entries | `"w"` | Opens file in write mode to clear all content |

The goal is to demonstrate **Python file handling and exception management** through a practical, menu-driven journal application.

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 🔁 **Infinite Menu Loop** | Program runs continuously until user selects Exit |
| 📂 **File Creation** | Creates `Jornal.txt` with `"x"` mode; handles existing file gracefully |
| ✍️ **Append Entries** | Writes date-stamped journal entries using `"a"` mode |
| 👁️ **Read All Entries** | Displays full file content using `"r"` mode |
| 🔍 **Search by Date/Time** | Filters and displays lines matching entered date |
| 🔑 **Search by Keyword** | Filters and displays lines matching entered keyword |
| 🗑️ **Clear All Entries** | Wipes all content using `"w"` mode with confirmation prompt |
| ⚠️ **Custom Exceptions** | `No_Content` and `wrong_choice` as user-defined exception classes |
| 🛡️ **Built-in Exception Handling** | `FileNotFoundError` and `FileExistsError` handled per function |
| 🧩 **Modular Functions** | Each operation isolated in its own function for clean structure |

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

> 📝 **Note:** The journal data is stored in `Jornal.txt`, which is auto-created by the program in the same directory.

---

## 🔄 Project Workflow

```
Program Start → "Welcome.................."
      │
      ▼
┌─────────────────────────────────────┐
│          Display Main Menu          │
│  1-Create / 2-Add / 3-View          │
│  4-Search / 5-Delete / 6-Exit       │
└──────────────┬──────────────────────┘
               │
   ┌───────────┼──────────────────────┐
   ▼           ▼           ▼          ▼
┌──────┐   ┌──────┐   ┌────────┐  ┌──────┐
│  1   │   │  2   │   │   3    │  │  4   │
│Create│   │ Add  │   │  View  │  │Search│
│ File │   │Entry │   │  All   │  │Entry │
└──┬───┘   └──┬───┘   └───┬────┘  └──┬───┘
   │          │            │          │
   ▼          ▼            ▼          ▼
open("x")  open("a")   open("r")  Inner Loop
Create     Write date  Read &     1-By Date
new file   + entry     display    2-By Keyword
           to file     content    3-Back
   │          │            │          │
   └──────────┴────────────┴──────────┘
               │
       ┌───────┴──────────┐
       ▼                  ▼
   ┌──────┐           ┌──────┐
   │  5   │           │  6   │
   │Delete│           │ Exit │
   └──┬───┘           └──┬───┘
      │                  │
  Confirm?           Break loop
  open("w")          Farewell msg
  Clear file              ✅
```

---

## 📂 Operation 1 — Create File

### 📝 What it does

Prompts the user for confirmation, then creates `Jornal.txt` using Python's `"x"` (exclusive creation) file mode. If the file already exists, `FileExistsError` is caught and a friendly message is displayed.

**File Mode Used:** `"x"` — Creates a new file; fails if file already exists.

**Logic:**
```python
def Create_file():
    choice = input("Do want to create a file (Yes/No):").lower()
    if choice == "yes":
        try:
            file = open(File_name, "x")
            file.close()
            print("File created successfully.....................")
        except FileExistsError:
            print("There is a file which Exists......")
```

**Output:**

![Create File Output](assets/output_1_create_file.png)

---

## ✍️ Operation 2 — Add Entry

### 📝 What it does

Collects a date/time string and a journal entry from the user, then appends both to `Jornal.txt` using `"a"` (append) mode. Each entry is formatted with clear labels and line spacing. If the file doesn't exist, `FileNotFoundError` is caught with a helpful prompt.

**File Mode Used:** `"a"` — Opens file for appending; creates if not found (but here we handle the error).

**Entry Format Written to File:**
```
Date & Time : 27-10-2020
Entry       : hii i am learning python
```

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

## 👁️ Operation 3 — View All Entries

### 📝 What it does

Opens `Jornal.txt` in `"r"` (read) mode and displays the full content to the console. If the file is empty, the custom `No_Content` exception is raised. If the file doesn't exist, `FileNotFoundError` is caught gracefully.

**File Mode Used:** `"r"` — Opens file for reading only.

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
            print("-" * 10)
            print(content)
            print("-" * 10)
            print("END")
        file.close()
    except FileNotFoundError:
        print("Create a file for Journal")
```

**Sample Output:**
```
FILE CONTEXT:
----------

Date & Time : 27-10-2020
Entry       : hii i am learning python

----------
END
```

**Output:**

![View Entries Output](assets/output_3_view_entries.png)

---

## 🔍 Operation 4 — Search for an Entry

### 📝 What it does

Enters a **nested inner loop** with a sub-menu offering two search modes. The file is read line-by-line using `readlines()`, and matching lines are printed to the console. The user can exit the search menu back to the main menu at any time.

**File Mode Used:** `"r"` — Opens file and reads all lines into a list.

**Sub-Menu Options:**

| Option | Search Type | Input |
|--------|-------------|-------|
| 1 | By Date/Time | `DD-MM_YY::00:0 am/pm` format |
| 2 | By Keyword | Any word present in an entry |
| 3 | Exit | Returns to main menu |

**Logic:**
```python
def Search_Entry():
    while True:
        # Inner search sub-menu
        match choice:
            case 1:
                file = open(File_name, "r")
                lines = file.readlines()
                Date_time = input("Enter Date and Time : ")
                for line in lines:
                    if Date_time or "Entry" in line:
                        print(line)
            case 2:
                file = open(File_name, "r")
                lines = file.readlines()
                keyword = input("Enter the Keyword:")
                for line in lines:
                    if keyword or "Date & Time" in line:
                        print(line)
            case 3:
                break
```

**Search by Date/Time Output:**

![Search by Date Output](assets/output_4_search_by_date.png)

**Search by Keyword Output:**

![Search by Keyword Output](assets/output_5_search_by_keyword.png)

**Exit Search Menu Output:**

![Search Exit Output](assets/output_6_search_exit.png)

---

## 🗑️ Operation 5 — Delete All Entries

### 📝 What it does

Asks the user for confirmation before clearing all journal content. If confirmed, opens `Jornal.txt` in `"w"` (write) mode — which truncates the file to zero bytes — effectively wiping all entries while keeping the file intact.

**File Mode Used:** `"w"` — Opens file for writing; clears all existing content.

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

Breaks out of the outer `while True` loop, printing a cheerful farewell message and cleanly terminating the program.

**Logic:**
```python
case 6:
    print("HAVE A NICE DAY.....................HAVE A GOOD DAY....................HAVE WONDERFULLL DAY")
    break
```

**Output:**

![Exit Output](assets/output_8_exit.png)

---

## ⚠️ Custom Exception Handling

### 🛡️ User-Defined Exceptions

Two custom exception classes are defined at the top of the program to handle application-specific error cases cleanly.

```python
class No_Content(Exception):
    pass

class wrong_choice(Exception):
    pass
```

| Exception | Raised When | Where |
|-----------|-------------|-------|
| `No_Content` | File exists but has no journal entries | `Read_file()` |
| `wrong_choice` | User enters an invalid menu number | Main menu & Search sub-menu |

### Built-in Exceptions Handled

| Exception | Raised When | Where Caught |
|-----------|-------------|--------------|
| `FileExistsError` | File already exists on create | `Create_file()` |
| `FileNotFoundError` | File missing on read/add/delete | `Add_Entry()`, `Read_file()`, `clear_all()` |

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| 🐍 **Python** | 3.10+ | Core programming language |
| 📂 **File I/O** | Built-in | `open()` with modes `x`, `a`, `r`, `w` |
| ⚠️ **Exception Handling** | Built-in | `try / except / else` blocks |
| 🧱 **Custom Exceptions** | Built-in OOP | `No_Content`, `wrong_choice` classes |
| 🔀 **Match-Case** | Python 3.10+ | Structural pattern matching for menus |
| 🔁 **While Loop** | Built-in | Outer & inner infinite menu loops |
| 🧩 **Functions** | Built-in | Modular design — one function per operation |
| 🖨️ **print() / input()** | Built-in | Console I/O and user interaction |

---

## 📈 Results & Insights

After running the program, the following operations are demonstrated:

- ✅ **File Created** — `Jornal.txt` successfully created using exclusive `"x"` mode
- ✍️ **Entry Added** — Date and journal text appended with `"a"` mode
- 👁️ **Entries Viewed** — Full file content read and displayed via `"r"` mode
- 🔍 **Date Search** — Lines filtered and displayed by matching date/time string
- 🔑 **Keyword Search** — Lines filtered and displayed by matching keyword
- 🗑️ **Entries Cleared** — All content wiped using `"w"` mode after confirmation
- 🚪 **Clean Exit** — Program terminates with a cheerful farewell message
- ⚠️ **Error Handling** — Custom and built-in exceptions caught at every operation

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 🎓 **Beginner Friendly** | Covers all four file modes in one practical project |
| 📂 **Real File Persistence** | Data saved to disk — survives program restarts |
| 🧱 **Custom Exceptions** | Shows how to define and raise user-defined exception classes |
| 🧩 **Modular Design** | Each operation in its own function — easy to read and extend |
| 🔍 **Search Capability** | Dual search by date and keyword adds real utility |
| 🖥️ **No Dependencies** | Runs with pure Python — no external libraries needed |
| ⚡ **Lightweight** | Single-file script, instantly runnable from any terminal |
| 🧪 **Extensible** | Easy to add features like edit entry, export to PDF, or encrypt journal |

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

[![GitHub](https://img.shields.io/badge/GitHub-isamaliya16-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/isamaliya16)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ayush-isamaliya-686533312/)

> *"Every journal entry is a line of code — write it with intention, and it will outlast the moment."*

**🎓 Role:** Junior Python Developer | Programming Enthusiast \
**📍 Location:** India \
**🛠️ Skills:** Python · File Handling · Exception Handling · CLI Applications · Modular Design

</div>

---

## 🙏 Acknowledgements

Special thanks to the following resources and communities that made this project possible:

- 📚 [Python Official Docs — File I/O](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files) — Official file handling reference
- 📂 [Real Python — File Handling](https://realpython.com/read-write-files-python/) — In-depth file I/O tutorials
- ⚠️ [Real Python — Exception Handling](https://realpython.com/python-exceptions/) — Custom and built-in exceptions guide
- 🔀 [PEP 634 — Match-Case](https://peps.python.org/pep-0634/) — Structural Pattern Matching specification
- 🖥️ [W3Schools Python](https://www.w3schools.com/python/) — Beginner Python reference
- 🧮 [GeeksForGeeks — File Handling](https://www.geeksforgeeks.org/file-handling-python/) — Python file operations guide
- 💬 [Stack Overflow Community](https://stackoverflow.com/) — Problem-solving support
- 📖 [Kaggle Learn](https://www.kaggle.com/learn) — Python and programming courses

---

<div align="center">

---

*Made with ❤️ and ☕ — Last updated: 18 June, 2026*

</div>
