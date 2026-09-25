# Python Automations

A collection of small Python programs I am creating while learning how to automate tasks with Python.

The goal of this repository is to practice Python fundamentals and gradually build more useful automation programs as I learn new concepts.

## Current Projects

### 1. Collatz Sequence

**File:** `collatz_sequence.py`

This program demonstrates the **Collatz sequence**.

The program takes an integer from the user and repeatedly applies these rules:

* If the number is **even**, divide it by 2.
* If the number is **odd**, multiply it by 3 and add 1.
* Continue until the result reaches `1`.

For example, starting with `6`:

```text
6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1
```

This program helped me practice:

* Functions
* `if/else` statements
* Modulo (`%`)
* Integer division (`//`)
* `while` loops
* User input
* Returning values from functions

### 2. Strong Password Detection

**File:** `strong_password_detection.py`

This program uses Python's **regular expressions (`re`)** to check whether a password meets several basic strength requirements.

A password must:

* Be at least **8 characters** long
* Contain at least **one digit**
* Contain at least **one uppercase letter**
* Contain at least **one lowercase letter**

The `strong_pass()` function returns:

```text
True
```

if the password meets all of the requirements, and:

```text
False
```

if it does not.

This program helped me practice:

* Functions
* Boolean values
* Conditional statements
* String length
* Regular expressions
* The `re` Python module
* Returning `True` and `False`

## How to Run

Make sure Python is installed on your computer.

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/Python_Automations.git
```

Move into the repository:

```bash
cd Python_Automations
```

Run the Collatz program:

```bash
python collatz_sequence.py
```

Run the password detection program:

```bash
python strong_password_detection.py
```

Depending on your system, you may need to use:

```bash
python3
```

instead of `python`.

As I learn more Python, I plan to add more programs that automate repetitive or useful tasks.

## Learning Goal

The long term goal of this repository is to build my Python skills through increasingly useful automation projects.

Each program is meant to introduce or reinforce a Python concept while moving toward more practical scripts.
