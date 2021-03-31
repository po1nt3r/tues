import uuid

class Employee:
    def __init__(self, name, email):
        self.name = name
        self.email = email 
        self.id = self.generate_id()
    
    def generate_id(self):
        id = uuid.uuid4()
        return id
    
    def print_email_and_name(self):
        print(f"Name: {self.name}; Email: {self.email}")

class Company:
    def __init__(self, name):
        self.name = name
        self.employees = []
    
    def add_employee(self):
        num = int(input("Enter how many employees you want to add: "))
        for _ in range(num):
            self.employees.append(Employee(input("Enter name: "), input("Enter email: ")))
        
    def print_employees(self):
        for i in self.employees:
            print(f"User id: {i.id}")
            i.print_email_and_name()

company1 = Company("(* ^ ω ^)")
company1.add_employee()
company1.print_employees()
        