# 🐍 Complete Python Beginner Setup & Roadmap Guide

This guide covers everything a beginner needs after installing Python:

1. Python + VS Code Setup
2. Virtual Environment Setup
3. Python Project Folder Structure
4. Beginner Python Roadmap

---

# 1️⃣ Python + VS Code Setup Guide

VS Code (Visual Studio Code) is a free and powerful code editor.

---

## 🔹 Step 1: Download VS Code

🔗 Official Website:
[https://code.visualstudio.com/](https://code.visualstudio.com/)

1. Click **Download for Windows / Mac / Linux**
2. Install using default settings.

---

## 🔹 Step 2: Install Python Extension in VS Code

1. Open VS Code.
2. Click **Extensions icon** (left sidebar).
3. Search for: `Python`
4. Install the extension published by **Microsoft**.

Why this extension?

* Syntax highlighting
* Code suggestions (IntelliSense)
* Debugging support
* Virtual environment detection

---

## 🔹 Step 3: Select Python Interpreter

1. Press:

   * Windows/Linux: `Ctrl + Shift + P`
   * macOS: `Cmd + Shift + P`
2. Type: `Python: Select Interpreter`
3. Choose the installed Python version (example: Python 3.x.x)

---

## 🔹 Step 4: Create and Run a Python File

1. Create a new file: `main.py`
2. Add:

```python
print("Hello from VS Code!")
```

3. Right-click → Run Python File
   OR
   Use terminal:

```
python main.py
```

(macOS/Linux: `python3 main.py`)

---

# 2️⃣ Virtual Environment Setup Guide

A Virtual Environment allows you to isolate project dependencies.

Why use it?

* Avoid version conflicts
* Keep projects independent
* Professional practice

---

## 🔹 Step 1: Create a Project Folder

```
mkdir my_project
cd my_project
```

---

## 🔹 Step 2: Create Virtual Environment

Windows:

```
python -m venv venv
```

macOS/Linux:

```
python3 -m venv venv
```

This creates a folder named `venv`.

---

## 🔹 Step 3: Activate Virtual Environment

Windows:

```
venv\Scripts\activate
```

macOS/Linux:

```
source venv/bin/activate
```

You will see:

```
(venv)
```

at the beginning of the terminal.

---

## 🔹 Step 4: Install Packages

Example:

```
pip install requests
```

---

## 🔹 Step 5: Deactivate Environment

```
deactivate
```

---

# 3️⃣ Python Project Folder Structure Guide

A professional beginner-friendly structure:

```
my_project/
│
├── venv/                # Virtual Environment (not uploaded to Git)
├── src/                 # Source code folder
│   ├── __init__.py
│   └── main.py
│
├── tests/               # Test files
│   └── test_main.py
│
├── requirements.txt     # Project dependencies
├── .gitignore
└── README.md
```

---

## 🔹 Explanation

### 📁 venv/

Virtual environment (never push to GitHub)

---

### 📁 src/

Main application code goes here.

---

### 📁 tests/

Unit test files using pytest or unittest.

---

### 📄 requirements.txt

Generate using:

```
pip freeze > requirements.txt
```

Install using:

```
pip install -r requirements.txt
```

---

### 📄 .gitignore

Example:

```
venv/
__pycache__/
*.pyc
```

---

# 4️⃣ Beginner Python Roadmap

This roadmap helps you become confident in Python.

---

## 🟢 Phase 1: Python Basics (2–3 Weeks)

Learn:

* Variables
* Data Types (int, float, string, list, tuple, dict)
* Input/Output
* Operators
* If-else
* Loops (for, while)
* Functions
* Basic error handling

Practice:

* Number guessing game
* Calculator program
* Pattern printing

---

## 🟡 Phase 2: Intermediate Python (3–4 Weeks)

Learn:

* OOP (Classes & Objects)
* File handling
* Modules & Packages
* Virtual environments
* List comprehensions
* Exception handling
* Lambda functions

Projects:

* Student management system
* File organizer
* To-do app (CLI)

---

## 🟠 Phase 3: Advanced Concepts

Learn:

* Decorators
* Generators
* Iterators
* Context managers
* Logging
* Unit testing (pytest)
* API handling (requests)

---

## 🔵 Phase 4: Choose a Career Path

### 🔹 Web Development

* Flask or Django
* REST APIs
* Database (PostgreSQL, MySQL)

### 🔹 Automation / Testing

* Selenium
* Playwright
* PyTest
* API automation

### 🔹 Data Science

* NumPy
* Pandas
* Matplotlib
* Scikit-Learn

### 🔹 DevOps / Scripting

* Linux commands
* Bash + Python
* Automation scripts

---

# 🎯 Recommended Learning Resources

Official Docs:
[https://docs.python.org/3/](https://docs.python.org/3/)

Interactive Practice:
[https://www.w3schools.com/python/](https://www.w3schools.com/python/)
[https://www.programiz.com/python-programming](https://www.programiz.com/python-programming)
[https://leetcode.com/](https://leetcode.com/)

---

# 🚀 Final Advice for Beginners

* Practice daily (minimum 1 hour)
* Build small projects
* Push code to GitHub
* Learn debugging
* Read official documentation

Consistency > Speed

---

# 🎉 Congratulations!

You now have:

✔ Professional Python setup
✔ Virtual environment knowledge
✔ Project structure understanding
✔ Clear learning roadmap

---
