# Coffee Payment Tracker

This is a Python application built with Tkinter and SQLite for tracking coffee bills among employees.

## Prerequisites

- Python 3.x installed on your system
- Tkinter library (usually included with Python)
- SQLite database support (usually included with Python)

## Getting Started

1. *Clone the repository:*

    bash
    git clone https://github.com/aptekedar/BertramCapitalCodingChallenge.git
    

2. *Navigate to the project directory:*

    bash
    cd BertramCodingChallenge
    

3. *Install dependencies (not needed as there are no external dependencies):*

    This project doesn't have any external dependencies beyond what's included with Python.

4. *Run the application:*

    bash
    python bertramCapitalCodingChallenge.py
    

5. *Interact with the application:*

    - Enter employee names and their coffee bills.
    - Click on "Add / Update Employee" to add or update an employee's bill.
    - Click on "Show Employees" to display the list of employees and their bills in a new window.
    - Click on "Pay" to calculate the total bill and determine who pays everyone's bill.
    - Click on "Delete Records" to delete all records from the database.
    - Close the application window when done.

## Notes

- The application stores employee names and their bills in a SQLite database named coffee_bills.db.
- If the database file doesn't exist, it will be created automatically in the project directory.
- The application allows adding multiple bills for the same employee, and it updates the total bill accordingly.
- When clicking on "Pay", the employee with the highest bill is determined, and their bill is reduced by the total bill amount.


## Assumptions and Login
- Here I am assuming every employee's name is unique.
- The logic I have used retrives the employee who owes the highest amount from the database and that employee pays the bill for that particular day.
- The paid amount then gets deducted from their owed amount and on the next day we again check which employee now owes the highest amount and then that employee pays the bill.
- This logic fairly calculates whuch employee pays the bill since here we are using historical data of the amount owed to determine who pays the coffee bill.
- For each new day the program would have to be stopped and run again for accurate output.