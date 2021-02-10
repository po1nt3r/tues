import random

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self,  amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print("Can't withdraw money")
            return
        self.balance -= amount

    def get_balance(self):
        #print(self.balance)
        return self.balance

class Client:
    def __init__(self):
        self.id = random.randint(100000, 1000000)
        self.bank_accounts = []

    def add_account(self, amount):
        a = BankAccount(amount)
        self.bank_accounts.append(a)
    
    def check_amount(self, amount, balance):
        if balance < amount:
            print("You don't have enough money to complete the transaction!")
            return False

    def withdraw(self, amount):
        self.get_account()
        a = int(input("Account to withdraw from: "))-1
        if not self.check_amount(amount, self.bank_accounts[a].balance):
            b = int(input("Account to transfer to: "))-1
            self.bank_accounts[a].balance -= amount
            self.bank_accounts[b].balance += amount

    
    def deposit(self, amount):
        self.get_account()
        a = int(input("Account to depostit to: "))-1
        if not self.check_amount(amount, self.bank_accounts[a].balance):
            b = int(input("Account to transfer from: "))-1
            self.bank_accounts[a].balance += amount
            self.bank_accounts[b].balance -= amount

    def transfer_to_self(self, amount, type = "withdraw"):
        if len(self.bank_accounts) >= 2:
            if type == "withdraw":
                self.withdraw(amount)
            elif type == "deposit":
                self.deposit(amount)
        else:
            print("You have only one account.")

    def get_account(self):
        for i in range(len(self.bank_accounts)):
            print(f"Money in account {i+1}:", self.bank_accounts[i].get_balance())


cl = Client()
cl.add_account(1200)
cl.add_account(2200)
cl.transfer_to_self(250)
cl.get_account()
print("---------------------")
cl.transfer_to_self(250, "deposit")
cl.get_account()