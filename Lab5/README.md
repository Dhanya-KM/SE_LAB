# SE Lab 5 – Static Code Analysis

## Project Title
**Supplier Orders Application**

## Objective
To analyze Python source code using static code analysis tools, identify code quality and security issues, fix the identified issues, and compare the results before and after the corrections.

## Tools Used
- **Pylint:** Checks code quality, naming conventions, documentation, and common programming issues.
- **Flake8:** Checks Python coding style, whitespace, indentation, and formatting.
- **Bandit:** Checks Python code for common security issues.
- **Git and GitHub:** Used for version control and source code management.

## Project Files
- `supplier_orders.py` – Final Python source code.
- `issues.xlsx` – Spreadsheet containing identified issues, fixes, and verification results.
- `pylint_report_before.txt` – Pylint analysis before fixes.
- `pylint_report_after.txt` – Pylint analysis after fixes.
- `flake8_report_before.txt` – Flake8 analysis before fixes.
- `flake8_report_after.txt` – Flake8 analysis after fixes.
- `bandit_report_before.txt` – Bandit analysis before fixes.
- `bandit_report_after.txt` – Bandit analysis after fixes.
- `Lab5_Report.docx` – Lab report describing the objective, tools, corrections, results, and conclusion.

## Issues Addressed
- Missing module and function documentation.
- Naming convention violations.
- Unnecessary global state.
- Unused function arguments.
- Long lines and formatting issues.
- Unsafe shell-command usage and SQL query handling.

## Corrections Made
- Added module and function docstrings.
- Renamed functions to follow snake_case.
- Removed the global order-total variable and accumulated the total within `main()`.
- Removed the unused argument from the received-order function.
- Corrected line lengths, indentation, and whitespace.
- Used parameterized SQL queries.
- Removed the unsafe shell-command usage.

## Final Results
- **Pylint:** 10.00/10.
- **Flake8:** Passed with no errors reported.
- **Bandit:** No issues identified.
- **Program execution:** Completed successfully.

Expected program output:

```text
notifying warehouse about Acme
1 540
```
### Source Code and Repository Attribution

This lab uses a forked repository as the starting codebase. The static code analysis, issue identification, and code improvements documented in this submission were performed as part of Lab 5.

- **My forked repository:** https://github.com/Dhanya-KM/L5_18_supplier_orders
- **Final source file:** https://github.com/Dhanya-KM/L5_18_supplier_orders/blob/main/supplier_orders.py

The original project belongs to its respective author. The fork is used to maintain and demonstrate the changes made for this lab.
## How to Run
1. Install Python 3 if it is not already installed.
2. Open a terminal in the project folder.
3. Run the program:

   ```bash
   python supplier_orders.py
   ```

4. To run the analysis tools, install them if necessary:

   ```bash
   python -m pip install pylint flake8 bandit
   ```

5. Run the checks:

   ```bash
   pylint supplier_orders.py
   flake8 supplier_orders.py
   bandit -r supplier_orders.py
   ```

## Conclusion
Static code analysis helped improve the readability, maintainability, formatting, and security of the Supplier Orders Application. The final code achieved a Pylint score of 10.00/10, passed Flake8 without errors, and had no issues identified by Bandit. The application was executed to verify its expected output.

