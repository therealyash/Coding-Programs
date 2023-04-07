import tkinter as tk
import sqlite3
import tkinter.messagebox as messagebox
from tkinter import ttk


class Employee:

    def add_employee(self):
        # connect to the database
        conn = sqlite3.connect("employee.db")
        c = conn.cursor()
        #c.execute("CREATE TABLE employees (name TEXT, email TEXT, contact TEXT, address TEXT)")

        # insert data into the table
        c.execute("INSERT INTO employees VALUES (:name, :email, :contact, :address)",
                  {
                      'name': self.name.get(),
                      'email': self.email.get(),
                      'contact': self.contact.get(),
                      'address': self.address.get()
                  })
        # commit the transaction
        conn.commit()
        # close the connection
        conn.close()

        # clear the entries
        self.name.set("")
        self.email.set("")
        self.contact.set("")
        self.address.set("")

        # display a success message
        tk.messagebox.showinfo("Success", "Employee added successfully")


    def view_employees(self):
        # connect to the database
        conn = sqlite3.connect("employee.db")
        c = conn.cursor()

        # fetch all the records from the table
        c.execute("SELECT * FROM employees")
        rows = c.fetchall()

        # clear the treeview
        self.employee_table.delete(*self.employee_table.get_children())

        # insert the records into the treeview
        for row in rows:
            self.employee_table.insert("", tk.END, values=row)

        # close the connection
        conn.close()

    def delete_employee(self):
        # connect to the database
        conn = sqlite3.connect("employee.db")
        c = conn.cursor()

        # delete the record from the table
        c.execute("DELETE FROM employees WHERE name=:name", {'name': self.name.get()})

        # commit the transaction
        conn.commit()
        # close the connection
        conn.close()

        # clear the entries
        self.name.set("")
        self.email.set("")
        self.contact.set("")
        self.address.set("")

        # display a success message
        tk.messagebox.showinfo("Success", "Employee deleted successfully")

    def search_employee(self):
        # connect to the database
        conn = sqlite3.connect("employee.db")
        c = conn.cursor()

        # search the record in the table
        c.execute("SELECT * FROM employees WHERE name=:name", {'name': self.name.get()})
        rows = c.fetchall()

        # clear the treeview
        self.employee_table.delete(*self.employee_table.get_children())

        # insert the records into the treeview
        for row in rows:
            self.employee_table.insert("", tk.END, values=row)

        # close the connection
        conn.close()


    def __init__(self, root):
        self.root = root
        self.root.title("Employee Management System")
        self.root.geometry("1350x750+0+0")

        # create frames
        main_frame = tk.Frame(self.root, bg="white")
        main_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        form_frame = tk.Frame(main_frame, bg="#fcc324")
        form_frame.pack(side=tk.TOP, fill=tk.X)

        # create widgets for the form frame
        tk.Label(form_frame, text="Employee Management System", font=("times new roman", 20, "bold"), bg="#fcc324", fg="white").pack()
        tk.Label(form_frame, text="", bg="#fcc324").pack()

        tk.Label(form_frame, text="Name", font=("times new roman", 15, "bold"), bg="#fcc324", fg="white").pack()
        self.name = tk.StringVar()
        tk.Entry(form_frame, textvariable=self.name, width=30).pack()

        tk.Label(form_frame, text="Email", font=("times new roman", 15, "bold"), bg="#fcc324", fg="white").pack()
        self.email = tk.StringVar()
        tk.Entry(form_frame, textvariable=self.email, width=30).pack()

        tk.Label(form_frame, text="Contact", font=("times new roman", 15, "bold"), bg="#fcc324", fg="white").pack()
        self.contact = tk.StringVar()
        tk.Entry(form_frame, textvariable=self.contact, width=30).pack()

        tk.Label(form_frame, text="Address", font=("times new roman", 15, "bold"), bg="#fcc324", fg="white").pack()
        self.address = tk.StringVar()
        tk.Entry(form_frame, textvariable=self.address, width=30).pack()

        tk.Label(form_frame, text="", bg="#fcc324").pack()
        tk.Button(form_frame, text="Add Employee", width=20, command=self.add_employee).pack()
        tk.Button(form_frame, text="View Employees", width=20, command=self.view_employees).pack()
        tk.Button(form_frame, text="Delete Employees", width=20, command=self.delete_employee).pack()
        tk.Button(form_frame, text="Search Employee", width=20, command=self.search_employee).pack()

        # create table frame
        table_frame = tk.Frame(main_frame, bg="white")
        table_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        # create table
        self.employee_table = tk.ttk.Treeview(table_frame, column=("Name", "Email", "Contact", "Address"), height=500)
        self.employee_table.pack(fill=tk.BOTH, expand=True)



if __name__ == "__main__":
    root = tk.Tk()
    app = Employee(root)
    root.mainloop()

