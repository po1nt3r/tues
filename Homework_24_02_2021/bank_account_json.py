import random
import yaml
import csv
import json
import os


class BankAccount:
    def __init__(self, balance, account_file):
        self.account_file = account_file
        global number
        number += 1
        if os.path.exists(account_file):
            with open(account_file) as f:
                self.data = json.load(f)
                if number <= len(self.data.keys()):
                    print(list(self.data.keys())[number-1])
                    self.id = list(self.data.keys())[number-1]
                    
                    self.balance = self.data[self.id]
                else:
                    self.id = self.identify()
                    self.balance = balance
                    self.data.update({self.id: self.balance})
                    with open(account_file, "w") as f:
                        json.dump(self.data, f)
        else:
            self.id = random.randint(0, 999999)
            self.balance = balance
            self.data = {self.id: self.balance}
            with open(account_file, "w") as f:
                json.dump(self.data, f)

    def identify(self):
        self.id = random.randint(0, 999999)
        while self.id in self.data.keys():
            self.id = random.randint(0, 999999)
        
        return self.id
    
    def deposit(self,  amount):
        self.balance += amount
        self.data[self.id] = self.balance
        with open(self.account_file, "w") as f:
            json.dump(self.data, f)

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print("Can't withdraw money")
            return
        self.balance -= amount
        self.data[self.id] = self.balance
        with open(self.account_file, "w") as f:
            json.dump(self.data, f)

    def get_balance(self):
        print(self.balance)
        return self.balance

number = 0
SOURCE = "smetka1.json"
smetka1 = BankAccount(1500, SOURCE)
smetka1.withdraw(500)
smetka2 = BankAccount(1500, SOURCE)
smetka2.deposit(1500)
smetka3 = BankAccount(1500, SOURCE)
smetka4 = BankAccount(1500, SOURCE)
smetka5 = BankAccount(1500, SOURCE)