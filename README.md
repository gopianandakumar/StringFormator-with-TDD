The StringCalculator class implements the Add method with the following functionality:

Returns 0 for an empty string ("").
Handles single numbers (e.g., "1" → 1).
Sums two numbers separated by commas (e.g., "1,2" → 3).
Supports an unknown number of numbers (e.g., "1,2,3" → 6).
Allows newlines as delimiters (e.g., "1\n2,3" → 6).
Supports custom delimiters (e.g., "//;\n1;2" → 3).
Throws an exception for negative numbers (e.g., "-1,2,-3" → "negatives not allowed: -1, -3").
Ignores numbers greater than 1000 (e.g., "2,1001" → 2).
Handles delimiters of any length (e.g., "//[***]\n1***2***3" → 6).
Supports multiple delimiters (e.g., "//[*][%]\n1*2%3" → 6).

Setup Instructions
To run the project locally, follow these steps:

Clone the Repository:
git clone https://github.com/gopianandakumar/StringFormator-with-TDD
cd string-calculator


Set Up a Virtual Environment:
python -m venv .venv
.venv\Scripts\activate  # On Windows
source .venv/bin/activate  # On Linux/Mac


Install Dependencies:
pip install pytest


Run Tests:
pytest

The test suite in test_calculator.py verifies all functionality using the pytest framework.


TDD Process
The implementation was developed using TDD, with the following steps reflected in the commit history:

Empty String: Added test and implementation for "" returning 0.
Single Number: Added test and implementation for single numbers (e.g., "1" → 1).
Two Numbers: Supported comma-separated numbers (e.g., "1,2" → 3).
Multiple Numbers: Extended to handle any number of comma-separated values (e.g., "1,2,3" → 6).
Newline Delimiters: Added support for newlines (e.g., "1\n2,3" → 6).
Negative Numbers: Implemented exception handling for negatives (e.g., "-1,-2,3" → error).
Numbers > 1000: Ignored numbers greater than 1000 (e.g., "2,1001" → 2).
Custom Delimiters: Supported custom delimiters (e.g., "//;\n1;2" → 3).
Long and Multiple Delimiters: Handled delimiters of any length and multiple delimiters (e.g., "//[***]\n1***2***3" → 6, "//[*][%]\n1*2%3" → 6).

Each step includes a failing test, minimal implementation to pass, and refactoring where needed. The commit history in this repository shows the evolution of the code.
Project Structure
string-calculator/
├── string_calculator.py  # Implementation of StringCalculator class
├── test_calculator.py    # Pytest test suite
├── .gitignore            # Excludes __pycache__, .venv, etc.
├── README.md             # This file

Requirements

Python: 3.10 or higher
pytest: For running tests
No external dependencies beyond the Python standard library (e.g., re for regex).

Running the Calculator
To manually test the calculator:
from string_calculator import StringCalculator
calc = StringCalculator()
print(calc.Add(""))  # 0
print(calc.Add("1"))  # 1
print(calc.Add("1,2"))  # 3
print(calc.Add("1\n2,3"))  # 6
print(calc.Add("//;\n1;2"))  # 3
print(calc.Add("//[***]\n1***2***3"))  # 6
print(calc.Add("//[*][%]\n1*2%3"))  # 6
print(calc.Add("2,1001"))  # 2
try:
    calc.Add("-1,2,-3")
except ValueError as e:
    print(e)  # negatives not allowed: -1, -3

Notes

The code is written in Python 3.10 to align with modern Python practices and the role’s requirements.
The implementation uses regular expressions (re) for robust delimiter parsing.
Error handling ensures invalid inputs (e.g., malformed delimiters, non-numeric values) raise appropriate exceptions.
The commit history follows TDD principles, with each commit representing a test-implementation-refactor cycle.

For any issues or questions, please contact gopianandakumar@gmail.com.
