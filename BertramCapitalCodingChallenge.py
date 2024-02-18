import tkinter as tk
import sqlite3

# Create a SQLite database or connect to an existing one
conn = sqlite3.connect('coffee_bills.db')
c = conn.cursor()

# Create table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS employees
             (id INTEGER PRIMARY KEY, name TEXT, bill REAL)''')
conn.commit()
currentbill = []

def add_employee():
    name = name_entry.get()
    bill = float(bill_entry.get())

    currentbill.append(bill)

    # Check if employee already exists in database
    c.execute("SELECT * FROM employees WHERE name=?", (name,))
    existing_employee = c.fetchone()

    if existing_employee:
        # Update bill for existing employee
        new_bill = existing_employee[2] + bill
        c.execute("UPDATE employees SET bill=? WHERE name=?", (new_bill, name))
    else:
        # Insert new employee into database
        c.execute("INSERT INTO employees (name, bill) VALUES (?, ?)", (name, bill))
    
    conn.commit()

    # Clear entry fields
    name_entry.delete(0, tk.END)
    bill_entry.delete(0, tk.END)

def show_employees():
    # Fetch all employees from database
    c.execute("SELECT * FROM employees")
    employees = c.fetchall()

    # Display employees in a new window
    window = tk.Toplevel(root)
    window.title("Employees")
    for i, employee in enumerate(employees):
        tk.Label(window, text=f"{employee[1]}: ${employee[2]:.2f}").grid(row=i, column=0, padx=10, pady=5)

def pay_bills():
    # Calculate total bill
    c.execute("SELECT SUM(bill) FROM employees")
    total_bill = sum(currentbill)

    # Find employee with the highest bill
    c.execute("SELECT name, MAX(bill) FROM employees")
    highest_bill = c.fetchone()
    highest_bill_name = highest_bill[0]
    highest_bill_amount = highest_bill[1]

    # Update bill for employee who pays everyone's bill
    new_bill = highest_bill_amount - total_bill
    c.execute("UPDATE employees SET bill=? WHERE name=?", (new_bill, highest_bill_name))
    conn.commit()

    # Display the message indicating who pays everyone's bill
    highest_bill_text.set(f"{highest_bill_name} pays everyone's bill (${total_bill:.2f})")

def delete_records():
    # Delete all records from the database
    c.execute("DELETE FROM employees")
    conn.commit()

def on_close():
    conn.close()
    root.destroy()

root = tk.Tk()
root.title("Coffee Payment Tracker")
root.protocol("WM_DELETE_WINDOW", on_close)

# Employee Name Entry
tk.Label(root, text="Employee Name:").grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

# Coffee Bill Entry
tk.Label(root, text="Coffee Bill:").grid(row=1, column=0, padx=10, pady=5)
bill_entry = tk.Entry(root)
bill_entry.grid(row=1, column=1, padx=10, pady=5)

# Add Employee Button
add_button = tk.Button(root, text="Add / Update Employee", command=add_employee)
add_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

# Show Employees Button
show_button = tk.Button(root, text="Show Employees", command=show_employees)
show_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

# Pay Bills Button
pay_bills_button = tk.Button(root, text="Pay", command=pay_bills)
pay_bills_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

# Delete Records Button
delete_button = tk.Button(root, text="Delete Records", command=delete_records)
delete_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

# Label to display message indicating who pays everyone's bill
highest_bill_text = tk.StringVar()
highest_bill_label = tk.Label(root, textvariable=highest_bill_text)
highest_bill_label.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()



