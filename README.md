# 🐍 Python with Frits

> A hands-on Python learning journey — from basic data types and control flow to OOP, files, Excel, logging, context managers, automation, and AI APIs.

This repository contains the lessons, experiments, and practical notes collected while learning Python. The goal is not just to memorize syntax, but to **write code, test ideas, make mistakes, and gradually build useful programs**.

---

## 🚀 What This Lesson Covers

The lesson grows from simple Python expressions into more practical programming concepts:

| Stage | Topics |
|---|---|
| 🧮 01 | Input, type conversion & arithmetic |
| 📦 02 | Lists, tuples, sets & dictionaries |
| 🔎 03 | Membership operators & string operations |
| 🧠 04 | Conditions and logical decisions |
| 🔁 05 | `for`, `while`, nested loops & `range()` |
| 🎮 06 | Small interactive programs and guessing games |
| 🧩 07 | Functions, parameters & return values |
| 🛠️ 08 | Built-in functions such as `dir()`, `isinstance()`, `round()` & `sorted()` |
| 🔗 09 | `zip()` and `filter()` |
| ✍️ 10 | String formatting and common string methods |
| 📚 11 | List methods and list comprehensions |
| 📄 12 | Text, CSV & JSON file handling |
| 🪵 13 | Logging and writing logs to files |
| 📊 14 | Excel workbooks with `openpyxl` |
| 🐼 15 | Creating DataFrames and exporting data with Pandas |
| ⏱️ 16 | Context managers and measuring execution time |
| 🧯 17 | Exception handling |
| 🏗️ 18 | Object-Oriented Programming |
| 🗂️ 19 | File-system automation with `pathlib` and `os` |
| 🤖 20 | Connecting Python to an AI API |

---

## 🗺️ The Learning Journey

```text
                 🐍 PYTHON
                     │
        ┌────────────┴────────────┐
        ▼                         ▼
   🧱 FUNDAMENTALS             🧰 TOOLS
        │                         │
   Variables                    Files
   Input / Output               CSV / JSON
   Arithmetic                   Excel
   Strings                      Pandas
        │                       Logging
        ▼
   🧠 CONTROL FLOW
        │
   if / elif / else
   for / while
   break / continue
        │
        ▼
   🧩 FUNCTIONS
        │
   Parameters
   Arguments
   Return values
        │
        ▼
   🏗️ OOP
        │
   Classes
   Objects
   Attributes
   Methods
        │
        ├──────────────► 🗂️ AUTOMATION
        │                    │
        │                 pathlib
        │                 os
        │                 File sorting
        │
        └──────────────► 🤖 AI
                             │
                         API client
                         Environment variables
                         .env
```

---

## 🧮 1. Start With Data

The lesson begins with simple user input and converts the received strings into numbers before performing calculations.

```python
str_num_a = input("Enter Your First: ")
str_num_b = input("Enter Your Second: ")

str_num_a = int(str_num_a)
str_num_b = int(str_num_b)

overall_result = str_num_a + str_num_b
print(overall_result)
```

### Important idea

`input()` returns text, so numerical calculations require conversion such as:

```python
int(...)
float(...)
```

The lesson also explores:

```text
+     addition
-     subtraction
*     multiplication
/     division
//    floor division
%     remainder
**    exponentiation
```

---

## 📦 2. Python Collections

One major section focuses on Python's collection data types.

```text
List       → mutable, ordered collection
Tuple      → immutable, ordered collection
Set        → unique values
Dictionary → key/value mapping
```

### Lists

The lesson practices:

```python
items = ["Xiao Yan", "Chhanun", "Lin Tong", "Tang Sang"]

items[1] = "Navizcy"
items.append("Sorona")
items.insert(2, "Hello")
items.remove("Lin Tong")
items.pop(1)
```

It also explores slicing:

```python
items[:2]
items[2:]
items[1:2]
```

and useful operations such as:

```python
len(items)
10 in numbers
sum(numbers)
sorted(numbers)
min(numbers)
max(numbers)
```

### Dictionaries

The lesson also works with dictionary access:

```python
data = {
    "int": "A count",
    "Subject": "Math, English, Biology",
    "Book": "1, 2, 3, 4, 5"
}

data.get("Book")
data.setdefault("Book")
"Subject" in data
```

And later:

```python
data.items()
data.keys()
data.values()
```

---

## 🔎 3. Membership Operators

Python can ask whether something exists inside a collection or string:

```python
"boy" in messenger
"girl" not in messenger
```

This becomes useful when validating input and making decisions.

---

## 🧠 4. Add Logic With Conditions

The lesson moves from storing data to **making decisions**.

```python
if condition:
    ...
elif another_condition:
    ...
else:
    ...
```

The examples use combinations of values and logical operators such as:

```text
and
or
not
```

This is where Python starts behaving less like a calculator and more like a program that can **choose what to do**.

---

## 🎮 5. Loops & Small Games

The lesson includes an interactive number-guessing game.

The player gets three attempts to guess a hidden number:

```text
        🎯 Guess the number
                │
                ▼
        Is the input valid?
           /          \
         Yes           No
          │             │
          ▼             ▼
      Compare       Ask again
      the guess
       /  |  \
      /   |   \
   lower equal higher
     │     │     │
   retry  🎉    retry
```

It also practices:

```python
for k in range(3):
    ...
```

and:

```python
while True:
    ...
    break
    continue
```

Another example models a ticket system where the program continues selling tickets until the available tickets reach zero.

---

## 🧩 6. Functions

The lesson introduces functions gradually.

### Function without parameters

```python
def speak_something():
    print("Hello world of coding")
```

### Function with a parameter

```python
def fullName(name):
    print("hello {}".format(name))
```

### Function with a return value

```python
def sumNumber(a, b):
    total = a + b
    return total
```

The important distinction explored here is:

```text
print()  → displays a value

return   → sends a value back from the function
```

---

## 🔗 7. `zip()` and `filter()`

The lesson introduces useful built-in tools for working with collections.

### `zip()`

Two lists can be paired together:

```python
container = ["Food", "drink", "vegetable"]
amounts = ["20", "60", "90"]

for container, amount in zip(container, amounts):
    print(container, amount)
```

Conceptually:

```text
Food       ↔ 20
drink      ↔ 60
vegetable  ↔ 90
```

### `filter()`

The lesson uses a function to keep values that satisfy a condition:

```python
def call_list(number):
    return number % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = filter(call_list, numbers)
print(list(even_numbers))
```

---

## ✍️ 8. Strings

A large section is dedicated to manipulating text.

Examples include:

```python
text.upper()
text.lower()
text.index("o")
text.replace("old", "new")
text.split()
text.strip()
```

Joining collections:

```python
items = ["A", "B", "C", "D"]

"".join(items)
"-".join(items)
```

Formatting:

```python
"Hello {} Hackers.".format("python")
```

These small operations become extremely useful when processing real-world data.

---

## 📚 9. List Comprehensions

The lesson shows how a normal loop can sometimes become a compact list comprehension.

### Traditional approach

```python
items_upper = []

for item in items:
    items_upper.append(item.upper())
```

### Comprehension

```python
items_upper = [item.upper() for item in items]
```

It also demonstrates filtering:

```python
items_upper = [
    item.upper()
    for item in items
    if "item_" in item
]
```

And numerical transformations:

```python
numbers = [1, 2, 3, 4, 5]

num_sq = [num**2 for num in numbers]
num_cube = [num**3 for num in numbers]
```

---

## 📄 10. Working With Files

The lesson begins moving beyond memory-only programs and into persistent data.

### Text files

```python
with open(filename, "r") as file:
    content = file.read()
```

Writing:

```python
with open(filename, "w") as file:
    file.write("Hello world!\n")
```

Using `with` is important because it manages the file resource automatically.

The lesson also explores:

- Text files
- CSV
- JSON
- `os`
- File existence checks

---

## 🪵 11. Logging

Instead of relying only on `print()`, the lesson introduces Python logging.

The main levels explored are:

```text
DEBUG    = 10
INFO     = 20
WARNING  = 30
ERROR    = 40
CRITICAL = 50
```

Example:

```python
import logging

logging.debug("Debug message")
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical message")
```

The lesson also explores sending logs to a file and configuring handlers and formatters.

---

## 📊 12. Excel With `openpyxl`

The lesson moves into spreadsheet automation.

It practices:

```python
load_workbook(...)
Workbook()
wb.save(...)
```

and working with worksheets:

```python
wb.active
wb["Sheet2"]
wb.worksheets
wb.sheetnames
```

It also covers:

- Reading cells
- Writing cells
- Appending rows
- Inserting rows/columns
- Deleting rows/columns
- Moving ranges
- Working with cell ranges
- Styling cells
- Merging cells
- Resizing rows and columns
- Adding comments
- Adding hyperlinks

This turns Python into a practical tool for manipulating Excel data.

---

## 🐼 13. Pandas

The lesson introduces DataFrames using Pandas.

Example:

```python
import pandas as pd

data = {
    "Project Name": ["Phnom Penh City", "Shanghai Tower"],
    "Height(m)": [546, 345],
    "Country": ["Cambodia", "China"]
}

df = pd.DataFrame(data)
print(df)
```

The lesson also exports DataFrames to Excel:

```python
df.to_excel("Pandas.xlsx", index=False)
```

This creates a bridge from basic Python programming toward **data processing**.

---

## ⏱️ 14. Context Managers

The lesson experiments with `contextlib.contextmanager`.

One example measures execution time:

```python
@contextlib.contextmanager
def time_it():
    start = time.time()
    yield
    end = time.time()

    timer = end - start
    print(f"Time Taken: {timer}s")
```

This is then used around code that needs to be measured.

The lesson also experiments with a context manager for exception handling.

---

## 🧯 15. Exception Handling

Python programs can encounter errors while running.

The lesson introduces:

```python
try:
    print(1 / 0)
except ZeroDivisionError:
    print("Dividing by 0 is not allowed")
```

The key idea:

```text
try
 │
 ├── code succeeds ───────► continue
 │
 └── error occurs ────────► except
```

This helps programs handle expected problems instead of stopping immediately.

---

## 🏗️ 16. Object-Oriented Programming

The lesson eventually reaches OOP.

A class acts as a template for objects.

Example concept:

```python
class Element:
    count_id = 1

    def __init__(self, w, h, loc, mat):
        self.width = 12
        self.height = 20
        self.location = loc
        self.material = mat
        self.id = self.new_gen()
```

Objects are then created from the class:

```python
elem_a = Element(12, 20, (9, 9), "wood")
elem_b = Element(15, 34, (6, 6), "Concrete")
```

The lesson practices:

```text
Class
  ↓
Object
  ↓
Attributes
  ↓
Methods
  ↓
Object behavior
```

It also includes a `student_info` example with attributes, generated student numbers, schedules, and methods for modifying and displaying information.

---

## 🗂️ 17. Automating a Downloads Folder

One of the most practical ideas in the lesson is a file-organizing script.

The concept is:

```text
Downloads
   │
   ├── image.png
   ├── movie.mp4
   ├── report.pdf
   ├── project.py
   ├── archive.zip
   └── setup.exe
          │
          ▼
     Check extension
          │
          ▼
      Sorting rules
          │
     ┌────┼────┬────┬─────┐
     ▼    ▼    ▼    ▼     ▼
  Images Videos Docs Code Data
```

The lesson uses `pathlib` and `os`, then defines categories based on file extensions.

This is an important step because Python is no longer only calculating values — it is **interacting with the computer's file system**.

---

## 🤖 18. Python + AI API

The final section connects Python to an AI API.

The lesson emphasizes an important security rule:

> **Never hardcode API keys in your code or comments.**

Instead, the lesson uses a `.env` file and environment variables.

```text
.env
 │
 └── OPENAI_API_KEY=...
          │
          ▼
     load_dotenv()
          │
          ▼
     os.getenv(...)
          │
          ▼
     API Client
          │
          ▼
        AI API
```

The lesson prepares a message containing a requested style and question, sends it through the API client, and prints the returned response.

---

## 🔐 Security Note

If you use an API key locally:

```text
.env
```

should be kept out of Git.

Add it to:

```text
.gitignore
```

For example:

```gitignore
.env
```

**Never commit a real API key to GitHub.**

---

## 🧪 Learning Philosophy

This lesson is intentionally experimental.

It contains:

- Small code experiments
- Repeated examples
- Different approaches to the same idea
- Notes about what each method does
- Practical mini-programs
- Explorations of libraries
- Experiments with automation and APIs

The purpose is to move through the following progression:

```text
"I can write Python syntax."
            ↓
"I understand what the syntax does."
            ↓
"I can combine concepts."
            ↓
"I can solve small problems."
            ↓
"I can automate tasks."
            ↓
"I can work with data."
            ↓
"I can build larger Python programs."
```

---

## 🛠️ Technologies & Modules Practiced

```text
Python
├── Built-in data structures
├── Functions
├── Loops
├── Conditions
├── Exceptions
├── OOP
├── String processing
├── File handling
├── os
├── pathlib
├── csv
├── json
├── logging
├── contextlib
├── openpyxl
├── pandas
├── python-dotenv
└── OpenAI API client
```

---

## 📌 Notes

This README describes the material present in the lesson file and follows its learning progression. Some code snippets in the original lesson are experiments, commented examples, or incomplete drafts rather than production-ready programs.

The lesson is best viewed as a **personal Python notebook of experiments and discoveries**, not as a polished software package.

---

## 🎯 Final Goal

The most important lesson is not any single function, library, or code snippet.

It is learning how to go from:

**data → logic → functions → files → automation → objects → external services**

using Python.

> 🐍 **Keep coding. Keep breaking things. Keep fixing them. That's how Python becomes a skill.**

---

### ⭐ Learning Status

```text
Python Fundamentals       ████████████████████
Collections               ████████████████████
Control Flow              ████████████████████
Functions                 ████████████████████
File Handling             ████████████████████
Logging                   ████████████████████
Excel / Data              ████████████████████
Context Managers          ████████████████████
OOP                       ████████████████████
Automation                ████████████████████
AI API                    ████████████████████
```

**End of lesson — but not the end of the journey. 🚀**
