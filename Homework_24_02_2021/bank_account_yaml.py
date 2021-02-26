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
                self.data = yaml.full_load(f)
                if len(self.data) >= number:
                    self.id = list(self.data.keys())[number-1]
                    self.balance = self.data[self.id]
                else:
                    self.id = self.identify()
                    self.balance = balance
                    with open(account_file, "a") as f:
                        yaml.dump({self.id:self.balance}, f)
        else:
            self.id = random.randint(0, 999999)
            self.balance = balance
            with open(account_file, "w") as f:
                yaml.dump({self.id:self.balance}, f)
                with open(account_file, "r") as f1:
                    self.data = yaml.full_load(f1)
    
    def identify(self):
        self.id = random.randint(0, 999999)
        while self.id in self.data.keys():
            self.id = random.randint(0, 999999)
        
        return self.id

    def deposit(self,  amount):
        self.balance += amount
        with open(self.account_file, "w") as f:
            self.data[self.id] = self.balance
            yaml.dump(self.data, f)

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print("Can't withdraw money")
            return
        self.balance -= amount
        with open(self.account_file, "w") as f:
            self.data[self.id] = self.balance
            yaml.dump(self.data, f)

    def get_balance(self):
        print(self.balance)
        return self.balance

number = 0
smetka1 = BankAccount(1500, "smetka1.yml")
smetka1.withdraw(500)
smetka2 = BankAccount(1500, "smetka1.yml")
smetka2.deposit(1500)