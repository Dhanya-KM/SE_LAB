# ATM Withdrawal System – Code and Branch Coverage Analysis

## Project Repository

[GitHub Repository – L6_L7_18_atm_withdrawal](https://github.com/Dhanya-KM/L6_L7_18_atm_withdrawal)

## Project Overview

This project implements an ATM Withdrawal System using Python. It includes functions for:

- **Withdraw:** Validates account type, withdrawal amount, daily withdrawal limits, bank fees, and available balance.
- **PIN Check:** Verifies the entered PIN and manages incorrect attempts and card blocking.
- **Note Breakup:** Calculates the number of ₹500, ₹200, and ₹100 notes required for a withdrawal.

## Technologies Used

- Python 3
- Pytest
- Coverage.py

## Project Files

- `atm_withdrawal.py` – Main application containing the ATM functions.
- `CodeCoverageTest_atm_withdrawal.py` – Test cases for statement/code coverage.
- `BranchCoverageTest_atm_withdrawal.py` – Test cases for branch coverage.
- `Before_code_coverage.png` – Initial code coverage result.
- `After_code_coverage.png` – Final code coverage result.
- `Before_Branch_coverage.png` – Initial branch coverage result.
- `After_Branch_coverage.png` – Final branch coverage result.

## 1. Code Coverage Analysis

Code coverage measures how much of the application's source code is executed by the test cases.

**Command used:**

```bash
coverage erase
coverage run --include="atm_withdrawal.py" -m pytest CodeCoverageTest_atm_withdrawal.py
coverage report -m
```

**Result: 100% Code Coverage**

All 34 executable statements in the application were covered by the test cases.

## 2. Branch Coverage Analysis

Branch coverage measures whether all possible decision outcomes in the application are executed.

**Command used:**

```bash
coverage erase
coverage run --branch --include="atm_withdrawal.py" -m pytest BranchCoverageTest_atm_withdrawal.py
coverage report -m
```

**Result: 100% Branch Coverage**

All 22 branches in the application were covered, with 0 partially covered branches.

## Coverage Summary

| Coverage Type | Initial Coverage | Final Coverage |
|---|---:|---:|
| Code Coverage | 62% | 100% |
| Branch Coverage | 54% | 100% |

## Conclusion

The ATM Withdrawal System was tested using Pytest and Coverage.py. Initially, some statements and decision branches were not covered. Additional test cases were written to cover the missing execution paths.

The final results achieved **100% code coverage and 100% branch coverage**, satisfying the coverage target for this lab exercise.