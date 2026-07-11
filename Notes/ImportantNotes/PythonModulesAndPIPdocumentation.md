# Python Modules, Packages, and pip — The Complete Guide

**From your first `import` to publishing your own package on PyPI.**

This guide is written so that a complete beginner can follow it from the top down, while still being detailed enough to serve as a reference for experienced developers. If you already know the basics, use the Table of Contents to jump straight to the advanced sections.

---

## Table of Contents

1. [Before You Start: What is Python?](#1-before-you-start-what-is-python)
2. [What is a Module? (Beginner)](#2-what-is-a-module-beginner)
3. [Why Use Modules?](#3-why-use-modules)
4. [The Three Types of Modules](#4-the-three-types-of-modules)
5. [Every Way to Import a Module](#5-every-way-to-import-a-module)
6. [What is a Package?](#6-what-is-a-package)
7. [How Python Actually Finds Your Imports](#7-how-python-actually-finds-your-imports-intermediate)
8. [What is pip?](#8-what-is-pip)
9. [Setting Up: Checking Python and pip](#9-setting-up-checking-python-and-pip)
10. [Installing, Upgrading, and Removing Packages](#10-installing-upgrading-and-removing-packages)
11. [Managing Dependencies with requirements.txt](#11-managing-dependencies-with-requirementstxt)
12. [Virtual Environments (Essential)](#12-virtual-environments-essential)
13. [Running Python Programs on Every OS](#13-running-python-programs-on-every-os)
14. [Building Your Own Package (Intermediate/Advanced)](#14-building-your-own-package-intermediateadvanced)
15. [Publishing a Package to PyPI (Advanced)](#15-publishing-a-package-to-pypi-advanced)
16. [Modern Dependency Tools (Advanced)](#16-modern-dependency-tools-advanced)
17. [How pip Resolves Dependencies](#17-how-pip-resolves-dependencies-advanced)
18. [Security Best Practices](#18-security-best-practices)
19. [Troubleshooting Common Errors](#19-troubleshooting-common-errors)
20. [Complete pip Command Reference](#20-complete-pip-command-reference)
21. [Best Practices Checklist](#21-best-practices-checklist)
22. [Summary](#22-summary)

---

## 1. Before You Start: What is Python?

Python is a high-level, interpreted, object-oriented programming language known for readable syntax and a huge standard library. "Interpreted" means you don't need to compile your code into a separate executable before running it — you just run the `.py` file directly and Python executes it line by line.

Python source files always end in the **`.py`** extension.

**hello.py**
```python
print("Hello, World!")
```

Run it:
```bash
python hello.py     # Windows
python3 hello.py    # Linux / macOS
```

Output:
```
Hello, World!
```

That's it — no separate compile step, no build tool required to get started.

---

## 2. What is a Module? (Beginner)

A **module** is simply a single `.py` file containing reusable code — variables, functions, classes, or constants. Instead of copy-pasting the same code into every project, you write it once in a module and `import` it wherever you need it.

**Analogy:** Think of a module like a toolbox. You don't rebuild a hammer every time you need one — you keep it in a toolbox (a `.py` file) and pull it out (`import`) whenever a job needs it.

**math_operations.py**
```python
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

PI = 3.14159   # modules can hold constants too
```

**Using the module (must be in the same folder, or on Python's search path):**
```python
import math_operations

print(math_operations.add(10, 20))       # 30
print(math_operations.multiply(5, 6))    # 30
print(math_operations.PI)                # 3.14159
```

A key beginner concept: **the module name is just the filename without `.py`.** `math_operations.py` becomes `math_operations` when imported.

### What happens the first time you import a module?

1. Python locates the file.
2. Python **executes the entire file top to bottom**, once.
3. Any variables, functions, or classes defined become attributes you can access with `module_name.thing`.
4. Python caches the result in memory (`sys.modules`), so importing the same module again elsewhere in your program does **not** re-run it — it reuses the cached version.

This is why placing "loud" code (like `print()` statements or network calls) at the top level of a module is usually a bad idea: it runs immediately on import, which surprises whoever imports your module.

### The `if __name__ == "__main__":` pattern

Every Python file has a built-in variable called `__name__`. When you *run* a file directly, `__name__` is set to `"__main__"`. When the same file is *imported* by another file, `__name__` is set to the module's name instead. This lets you write code that only runs when the file is executed directly, not when it's imported:

```python
def add(a, b):
    return a + b

if __name__ == "__main__":
    # Only runs when you do: python math_operations.py
    # Does NOT run when someone does: import math_operations
    print(add(2, 3))
```

This pattern is extremely common and worth memorizing early — it's how Python files can act as both a reusable library and a standalone script.

---

## 3. Why Use Modules?

| Benefit | Explanation |
|---|---|
| **Code Reusability** | Write logic once, use it in many scripts or projects. |
| **Better Organization** | Related functionality lives together instead of one giant file. |
| **Easier Maintenance** | Fix a bug in one place, and every file that imports it benefits. |
| **Reduced Duplication** | No more copy-pasting the same function across files. |
| **Better Testing** | You can test a module's functions in isolation. |
| **Cleaner Projects** | Large codebases stay navigable when split into logical modules. |
| **Namespacing** | `module_name.function()` avoids naming collisions between files. |

---

## 4. The Three Types of Modules

### 4.1 Built-in (Standard Library) Modules

These ship with every Python installation — no `pip install` required.

```python
import math       # mathematical functions
import random      # random number generation
import os          # operating system interaction (files, paths, env vars)
import sys         # interpreter internals, command-line args
import datetime    # dates and times
import json        # reading/writing JSON data
import csv         # reading/writing CSV files
import re          # regular expressions
import time        # time-related functions
import collections # specialized container datatypes (Counter, deque, etc.)
```

**Example:**
```python
import math
print(math.sqrt(25))   # 5.0
```

The full list of standard library modules is documented at [docs.python.org/3/library](https://docs.python.org/3/library/).

### 4.2 User-defined Modules

Modules **you** create for your own project.

**calculator.py**
```python
def subtraction(a, b):
    return a - b
```

**main.py**
```python
import calculator
print(calculator.subtraction(10, 4))   # 6
```

### 4.3 Third-party Modules (installed via pip)

Written by the broader Python community and published on **PyPI** (Python Package Index). You must install these with `pip` before you can import them.

| Package | Common Use |
|---|---|
| `requests` | Making HTTP requests |
| `numpy` | Numerical computing, arrays |
| `pandas` | Data analysis, tabular data |
| `flask` | Lightweight web framework |
| `django` | Full-featured web framework |
| `selenium` | Browser automation |
| `playwright` | Modern browser automation |
| `pytest` | Testing framework |
| `beautifulsoup4` | HTML/XML parsing |

**Example:**
```python
import requests

response = requests.get("https://example.com")
print(response.status_code)   # 200
```

> **Beginner tip:** If you see `ModuleNotFoundError: No module named 'requests'`, it means the package isn't installed yet. Run `pip install requests` first — see [Section 10](#10-installing-upgrading-and-removing-packages).

---

## 5. Every Way to Import a Module

### Import the entire module
```python
import math
print(math.sqrt(16))
```
You must prefix everything with `math.`.

### Import a specific function
```python
from math import sqrt
print(sqrt(16))
```
No prefix needed, but it's less clear where `sqrt` came from when reading the code later.

### Import multiple names at once
```python
from math import sqrt, factorial, pi
```

### Import everything (`*`)
```python
from math import *
```
⚠️ **Not recommended.** It pollutes your namespace and can silently overwrite names you already defined, causing hard-to-trace bugs. Only acceptable in small interactive scripts.

### Import using an alias
```python
import numpy as np
array = np.array([1, 2, 3])
```
Aliasing is a strong convention for certain packages (`numpy as np`, `pandas as pd`, `matplotlib.pyplot as plt`) — following the convention makes your code instantly readable to others.

### Relative imports (inside a package)
```python
# Inside package/module_b.py, importing from module_a.py in the same package
from . import module_a
from .module_a import some_function
from ..sibling_package import other_module   # go up one level
```
Relative imports only work **inside a package** (a folder with `__init__.py`), never in a standalone script you run directly.

### Conditional / lazy imports
```python
def load_optional_feature():
    import optional_heavy_library   # only imported when this function runs
    return optional_heavy_library.do_something()
```
Useful when a dependency is expensive to load or only needed occasionally.

---

## 6. What is a Package?

A **package** is a folder containing multiple related modules, organized so Python recognizes it as an importable unit. Traditionally, a package folder contains an `__init__.py` file (it can be empty) marking it as a package.

```
MyProject/
│
├── main.py
└── utilities/
    ├── __init__.py
    ├── math_utils.py
    ├── string_utils.py
    └── file_utils.py
```

**Importing from a package:**
```python
from utilities.math_utils import add
from utilities import string_utils

string_utils.capitalize_words("hello world")
```

### What goes in `__init__.py`?

It can be empty, or it can control what's exposed when someone imports the package itself:

```python
# utilities/__init__.py
from .math_utils import add, multiply
from .string_utils import capitalize_words

__all__ = ["add", "multiply", "capitalize_words"]
```

This lets users write `from utilities import add` directly, instead of `from utilities.math_utils import add` — a common convenience pattern for package authors.

### Package vs. Module — quick comparison

| | Module | Package |
|---|---|---|
| **What it is** | A single `.py` file | A folder of modules |
| **Example** | `math_utils.py` | `utilities/` |
| **Import** | `import math_utils` | `import utilities` |
| **Contains** | Functions, classes, variables | Modules, sub-packages |

---

## 7. How Python Actually Finds Your Imports (Intermediate)

When you write `import something`, Python searches these locations **in order**:

1. **The directory of the script being run** (or the current directory in interactive mode).
2. **`PYTHONPATH`** — an optional environment variable listing extra directories to search.
3. **The standard library directories** (where `math`, `os`, `json`, etc. live).
4. **`site-packages`** — where `pip`-installed third-party packages are placed.

You can inspect this search path yourself:
```python
import sys
print(sys.path)
```

This is why a module you wrote in one folder can't be imported from a script in a completely different folder unless it's on this path — a very common source of `ModuleNotFoundError` for beginners.

---

## 8. What is pip?

**pip** stands for **"Pip Installs Packages"** (a recursive acronym). It is Python's official package manager, used to install, upgrade, and remove third-party packages from **PyPI** — the Python Package Index, a public repository hosting hundreds of thousands of packages.

pip lets you:
* Install packages and specific versions
* Upgrade or downgrade packages
* Remove packages you no longer need
* Inspect installed packages and their metadata
* Manage a project's full list of dependencies

pip has shipped with Python automatically since Python 3.4, so in most modern installations you don't need to install it separately.

---

## 9. Setting Up: Checking Python and pip

### Check Python Installation

| OS | Command |
|---|---|
| Windows | `python --version` or `py --version` |
| Linux | `python3 --version` |
| macOS | `python3 --version` |

### Check pip Version

| OS | Command |
|---|---|
| Windows | `pip --version` or `py -m pip --version` |
| Linux | `pip3 --version` |
| macOS | `pip3 --version` |

### Upgrade pip

| OS | Command |
|---|---|
| Windows | `python -m pip install --upgrade pip` or `py -m pip install --upgrade pip` |
| Linux | `python3 -m pip install --upgrade pip` |
| macOS | `python3 -m pip install --upgrade pip` |

> **Why `python -m pip` instead of just `pip`?** If your system has multiple Python versions installed, typing `pip` alone might quietly point to the wrong one. Using `python -m pip` (or `python3 -m pip`) guarantees the package is installed for **the exact Python interpreter you're about to run** — this is the single most common fix for "I installed it but Python still can't find it" problems.

---

## 10. Installing, Upgrading, and Removing Packages

### Install a package

| OS | Command |
|---|---|
| Windows | `pip install requests` or `py -m pip install requests` |
| Linux | `pip3 install requests` or `python3 -m pip install requests` |
| macOS | `pip3 install requests` |

### Install a specific version
```bash
pip install selenium==4.35.0
```

### Install a minimum or range of versions
```bash
pip install "selenium>=4.0,<5.0"
pip install "requests>=2.28"
```

### Upgrade a package
```bash
pip install --upgrade selenium
```

### Uninstall a package
```bash
pip uninstall selenium
```

### List installed packages
```bash
pip list
```

### Show detailed info about a package
```bash
pip show selenium
```
Output includes version, location on disk, and dependencies.

### Download a package without installing
```bash
pip download selenium
```
Useful for preparing offline installs.

### Install without using the cache
```bash
pip install --no-cache-dir selenium
```

### Force reinstall (repair a broken install)
```bash
pip install --force-reinstall selenium
```

### Install directly from GitHub
```bash
pip install git+https://github.com/user/repo.git
```

### Install a local project in "editable" mode (for development)
```bash
pip install -e .
```
Changes to your source code take effect immediately without reinstalling — essential when developing your own package (see [Section 14](#14-building-your-own-package-intermediateadvanced)).

### Deprecated: `pip search`
```bash
pip search selenium
```
This command has been disabled on PyPI due to server load. Search for packages directly at [pypi.org](https://pypi.org) instead.

---

## 11. Managing Dependencies with requirements.txt

A `requirements.txt` file lists every package (and ideally, its exact version) your project needs, so anyone can recreate your environment with one command.

### Create it from your current environment
```bash
pip freeze > requirements.txt
```

**Example output:**
```
selenium==4.35.0
requests==2.32.4
pytest==8.4.1
```

### Install everything from a requirements file
```bash
pip install -r requirements.txt
```

### Best practice: split dependencies by purpose

For real projects, many teams split requirements into multiple files:

```
requirements.txt          # core production dependencies
requirements-dev.txt      # testing/linting tools, imports requirements.txt
```

**requirements-dev.txt**
```
-r requirements.txt
pytest==8.4.1
black==24.4.2
flake8==7.1.0
```

Install dev dependencies with:
```bash
pip install -r requirements-dev.txt
```

### Pinned vs. unpinned versions

```
requests==2.32.4     # pinned — exact reproducibility (recommended for apps)
requests>=2.32       # minimum version — more flexible (common for libraries)
requests              # unpinned — always installs latest (risky, avoid in production)
```

---

## 12. Virtual Environments (Essential)

A **virtual environment** is an isolated Python installation for a single project. It prevents one project's dependencies from conflicting with another's, and it's considered mandatory practice for any real Python work.

**Why it matters:** Imagine Project A needs `django==3.2` and Project B needs `django==5.0`. Without virtual environments, installing one breaks the other because pip installs packages globally by default. A virtual environment gives each project its own private copy of installed packages.

### Windows

Create:
```cmd
python -m venv venv
```

Activate (Command Prompt):
```cmd
venv\Scripts\activate
```

Activate (PowerShell):
```powershell
.\venv\Scripts\Activate.ps1
```

Deactivate:
```cmd
deactivate
```

### Linux

Create:
```bash
python3 -m venv venv
```

Activate:
```bash
source venv/bin/activate
```

Deactivate:
```bash
deactivate
```

### macOS

Create:
```bash
python3 -m venv venv
```

Activate:
```bash
source venv/bin/activate
```

Deactivate:
```bash
deactivate
```

### How to know it worked

Once activated, your terminal prompt typically shows the environment name in parentheses:
```
(venv) C:\Projects\MyApp>
```
Any `pip install` you run now only affects this isolated environment — not your system-wide Python.

### A typical new-project workflow
```bash
mkdir myproject && cd myproject
python3 -m venv venv
source venv/bin/activate        # or venv\Scripts\activate on Windows
pip install --upgrade pip
pip install requests pandas
pip freeze > requirements.txt
```

> **Tip:** Add `venv/` to your `.gitignore` file — never commit the virtual environment folder itself to version control, only `requirements.txt`.

---

## 13. Running Python Programs on Every OS

Assume this file exists:

**hello.py**
```python
print("Welcome to Python")
```

### Windows (Command Prompt)
```cmd
cd D:\PythonProjects
python hello.py
```
or
```cmd
py hello.py
```

### Windows (PowerShell)
```powershell
cd D:\PythonProjects
python .\hello.py
```
or
```powershell
py .\hello.py
```

### Windows (Git Bash)
```bash
cd /d/PythonProjects
python hello.py
```
or
```bash
python3 hello.py
```

### Linux Terminal
```bash
cd ~/PythonProjects
python3 hello.py
```

### macOS Terminal
```bash
cd ~/PythonProjects
python3 hello.py
```

### Running an Interactive Python Shell (REPL)

| OS | Start | Exit |
|---|---|---|
| Windows | `python` or `py` | `exit()` |
| Linux | `python3` | `exit()` |
| macOS | `python3` | `exit()` |

The interactive shell is useful for quickly testing a snippet of code without creating a file.

### Running a module as a script with `-m`
```bash
python -m module_name
```
This runs a module as if it were a script, using the correct import context — commonly used for tools like `python -m venv`, `python -m pip`, and `python -m http.server`.

---

## 14. Building Your Own Package (Intermediate/Advanced)

Once your project grows, you'll want to package your own code so it can be installed with `pip install .` — either for your own reuse across projects, or for publishing publicly.

### Modern project structure (using `pyproject.toml`)

```
mypackage/
├── pyproject.toml
├── README.md
├── LICENSE
├── src/
│   └── mypackage/
│       ├── __init__.py
│       ├── core.py
│       └── utils.py
└── tests/
    └── test_core.py
```

### Minimal `pyproject.toml`

```toml
[build-system]
requires = ["setuptools>=68.0"]
build-backend = "setuptools.build_meta"

[project]
name = "mypackage"
version = "0.1.0"
description = "A short description of what this package does"
readme = "README.md"
requires-python = ">=3.9"
license = { text = "MIT" }
authors = [
    { name = "Your Name", email = "you@example.com" }
]
dependencies = [
    "requests>=2.28",
]

[project.optional-dependencies]
dev = ["pytest>=8.0", "black>=24.0"]

[project.scripts]
mycli = "mypackage.core:main"
```

`pyproject.toml` has replaced the older `setup.py` as the standard way to describe a Python package. `setup.py` still works and is common in older codebases, but new projects should prefer `pyproject.toml`.

### Installing your package locally for development
```bash
cd mypackage
pip install -e .
```
The `-e` (editable) flag means edits to your source files are immediately reflected without reinstalling — critical for active development.

### The `[project.scripts]` section

This creates a command-line executable. After installing the package above, running `mycli` in the terminal calls the `main()` function inside `mypackage/core.py` — this is how tools like `black`, `flask`, and `pytest` become terminal commands after installation.

---

## 15. Publishing a Package to PyPI (Advanced)

### Step 1 — Install build tools
```bash
pip install build twine
```

### Step 2 — Build the distribution files
```bash
python -m build
```
This creates a `dist/` folder containing:
* A **wheel** file (`.whl`) — a pre-built, fast-to-install format
* A **source distribution** (`.tar.gz`) — the raw source, built at install time

### Step 3 — Upload to TestPyPI first (recommended)
```bash
twine upload --repository testpypi dist/*
```
TestPyPI (`test.pypi.org`) is a sandbox for verifying your package installs and works correctly before making it public.

### Step 4 — Upload to the real PyPI
```bash
twine upload dist/*
```
You'll need a PyPI account and an API token (PyPI no longer accepts plain username/password uploads).

### Step 5 — Anyone can now install it
```bash
pip install mypackage
```

---

## 16. Modern Dependency Tools (Advanced)

While `pip` + `venv` + `requirements.txt` remains the universal baseline, several modern tools build on top of pip to make dependency management more robust for larger projects:

| Tool | What it adds over plain pip |
|---|---|
| **`pip-tools`** | Generates a fully pinned `requirements.txt` from a loosely-specified `requirements.in`, ensuring reproducible builds. |
| **`poetry`** | Combines dependency management, virtual environments, and packaging/publishing into one tool with a lockfile (`poetry.lock`). |
| **`uv`** | A very fast, Rust-based drop-in replacement for pip and venv, with built-in lockfile support. |
| **`pipenv`** | Combines `pip` and `venv` with a `Pipfile`/`Pipfile.lock` for reproducible installs. |
| **`conda`** | A cross-language package/environment manager, popular in data science, that can manage non-Python dependencies too. |

These tools all solve the same underlying problem pip's basic `requirements.txt` doesn't fully solve on its own: **guaranteeing that everyone on a team, and your production server, install the exact same dependency tree**, including sub-dependencies (dependencies of your dependencies), not just the top-level packages you typed.

---

## 17. How pip Resolves Dependencies (Advanced)

When you run `pip install somepackage`, pip doesn't just install that one package — it also installs everything *that package* depends on, and everything *those* depend on, and so on.

Since pip version 20.3, pip uses a proper **dependency resolver** that:

1. Reads the requirements of the package you asked for.
2. Reads the requirements of every dependency, recursively.
3. Finds a single set of versions that satisfies **all** of them simultaneously.
4. Reports an error if no such combination exists (a "dependency conflict").

**Example of a conflict:**
```
ERROR: Cannot install package-a and package-b because these package versions
have conflicting dependencies.
The conflict is caused by:
    package-a 1.0.0 depends on requests<3.0,>=2.0
    package-b 2.0.0 depends on requests<2.0
```

This means package-a and package-b, as pinned, cannot both be satisfied by any single version of `requests`. Solutions typically involve loosening a version pin, upgrading one of the conflicting packages, or, if truly incompatible, isolating them into separate virtual environments.

You can inspect why a package is installed with:
```bash
pip show package_name
```
which lists both what it `Requires` and what `Required-by` it (i.e., what depends on it).

---

## 18. Security Best Practices

* **Only install from trusted sources.** By default pip installs from PyPI, which has some malware-scanning, but supply-chain attacks (malicious packages with names similar to popular ones — "typosquatting") do happen. Double-check package names before installing.
* **Pin versions in production** (`requests==2.32.4`, not `requests`) so an unexpected upstream update can't silently introduce a vulnerability or breaking change.
* **Use `pip install --require-hashes`** with a fully hashed requirements file in high-security environments, to guarantee the exact bytes installed match what you vetted.
* **Regularly audit dependencies** with tools like `pip-audit` (`pip install pip-audit && pip-audit`) to check installed packages against known vulnerability databases.
* **Avoid running pip as an administrator/root** unless installing genuinely system-wide tools — prefer virtual environments.
* **Review `requirements.txt` diffs in pull requests** just as carefully as code changes — a dependency bump can introduce new transitive dependencies you haven't vetted.

---

## 19. Troubleshooting Common Errors

| Error | Likely Cause | Fix |
|---|---|---|
| `ModuleNotFoundError: No module named 'x'` | Package not installed, or installed in a different environment | Activate the correct virtual environment, then `pip install x` |
| `pip: command not found` | pip isn't on PATH, or you need `pip3` | Try `python3 -m pip ...` or `pip3` instead of `pip` |
| Installed a package but Python still can't find it | Package installed for a different Python interpreter than the one running your script | Use `python -m pip install x` to guarantee the same interpreter |
| `Permission denied` during install | Trying to install globally without admin rights | Use a virtual environment instead of installing system-wide |
| `ERROR: Could not find a version that satisfies the requirement` | Typo in package name, or version doesn't exist, or Python version incompatible | Check spelling on PyPI, check `requires-python` compatibility |
| Two packages have conflicting dependency requirements | Version pins in your requirements are mutually incompatible | Loosen pins, upgrade one package, or use separate virtual environments |
| `SSL: CERTIFICATE_VERIFY_FAILED` | Corporate proxy/firewall intercepting HTTPS, or outdated certificates | Update `certifi`, or configure pip's trusted-host/proxy settings (consult your network admin before disabling SSL verification) |
| Old cached version keeps installing | Corrupted or stale pip cache | `pip install --no-cache-dir x` or `pip cache purge` |

---

## 20. Complete pip Command Reference

| Command | Description |
|---|---|
| `pip install package` | Install a package |
| `pip install package==1.2.3` | Install a specific version |
| `pip install "package>=1.0,<2.0"` | Install within a version range |
| `pip install --upgrade package` | Upgrade a package |
| `pip uninstall package` | Remove a package |
| `pip list` | List installed packages |
| `pip list --outdated` | Show packages with newer versions available |
| `pip show package` | Show detailed package info |
| `pip freeze` | Display installed packages with exact versions |
| `pip freeze > requirements.txt` | Save current dependencies to a file |
| `pip install -r requirements.txt` | Install all dependencies from a file |
| `pip install -e .` | Install the current project in editable/development mode |
| `pip install git+https://...` | Install directly from a Git repository |
| `pip download package` | Download a package without installing it |
| `pip install --no-cache-dir package` | Install while bypassing pip's cache |
| `pip install --force-reinstall package` | Reinstall a package from scratch |
| `pip cache purge` | Clear pip's entire download cache |
| `pip check` | Verify installed packages have compatible dependencies |
| `python -m pip --version` | Display pip version for a specific interpreter |
| `python -m pip install --upgrade pip` | Upgrade pip itself |

---

## 21. Best Practices Checklist

- [ ] Use a **virtual environment** for every project, without exception.
- [ ] Prefer `python -m pip` / `python3 -m pip` over bare `pip` to avoid interpreter mismatches.
- [ ] Install only the packages you actually need.
- [ ] Keep `pip` itself updated.
- [ ] Maintain a `requirements.txt` (or `pyproject.toml`) for every project.
- [ ] **Pin exact versions** in application `requirements.txt` files for reproducible deployments.
- [ ] Use looser version ranges (`>=`) only when publishing a *library* others will depend on.
- [ ] Add `venv/` (or `.venv/`) to `.gitignore` — never commit the environment folder.
- [ ] Periodically run `pip list --outdated` and update deliberately, not blindly.
- [ ] Audit dependencies for known vulnerabilities before deploying to production.
- [ ] Use `if __name__ == "__main__":` to separate script logic from importable logic.
- [ ] Avoid `from module import *` outside of quick interactive experiments.

---

## 22. Summary

* A **Module** is a single `.py` file containing reusable code — variables, functions, classes.
* A **Package** is a folder of related modules, made importable (traditionally via `__init__.py`).
* **pip** is Python's official package manager, used to install and manage third-party libraries from PyPI.
* Python looks for imports along `sys.path`: the script's own folder, `PYTHONPATH`, the standard library, and `site-packages`.
* Programs run from the command line using `python`, `py`, or `python3`, depending on the OS.
* **Virtual environments** isolate each project's dependencies and are considered essential, not optional, professional practice.
* Beyond installing packages, you can **build and publish your own** using `pyproject.toml`, `build`, and `twine`.
* For larger projects, tools like `pip-tools`, `poetry`, and `uv` add lockfiles and stronger reproducibility on top of pip's foundation.
* Good dependency hygiene — pinning versions, auditing for vulnerabilities, and reviewing what you install — is a core professional skill, not an afterthought.
