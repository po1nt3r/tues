from uuid import uuid4
import tkinter as tk


class Employee:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.id = self.generate_id()

    def generate_id(self):
        return uuid4()

    def print_employee(self):
        print(f"Name: {self.name}. Email {self.email}")


class Company:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, name, email):
        e = Employee(name, email)
        self.employees.append(e)

    def print_all(self):
        for i in self.employees:
            i.print_employee()
            
        
company = Company("Google")
company.print_all()

# Tkinter Graphic interface
window = tk.Tk()

label = tk.Label(text="Welcome to the company")
label.pack()
label = tk.Label(text=company.name)
label.pack()

def employees():
    a = company.employees
    label = tk.Label(text=a[-1].name + " " + a[-1].email)
    label.pack()
    
name = tk.Entry(window, text = "name")
email = tk.Entry(window, text = "email")


def submit_data():
    name1 = name.get()
    email1 = email.get()
    
    company.add_employee(name1, email1)
    
    name.delete(0, tk.END)
    email.delete(0, tk.END)
    
    print(company.employees[-1].name + " " + company.employees[-1].email)
    employees()

submit_button = tk.Button(text='Submit', command=submit_data)

name.pack()
email.pack()
submit_button.pack()

window.mainloop()

company.print_all()
