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
        print(self.balance)
        return self.balance

class Client:
    def __init__(self):
        self.id = random.randint(100000, 1000000)
        self.bank_account = []
    
    def add_account(self, amount):
        a = BankAccount(amount)
        self.bank_account.append(a)

    def print_accounts(self):
        for i in range(len(self.bank_account)):
            print(f"Account {i+1}: {self.bank_account[i].balance}")

    def choose_account(self): 
        self.print_accounts()
        return int(input("Choose na account: "))-1

    def transfer(self, c2, amount, type):
        if isinstance(c2, Client):
            if type == "withdraw":
                self.bank_account[self.choose_account()].balance += amount
                c2.bank_account[Client.choose_account(c2)].balance -= amount
            else:
                self.bank_account[self.choose_account()].balance -= amount
                c2.bank_account[Client.choose_account(c2)].balance += amount
        else:
            print("Not a client")

    def transfer_to_self(self, amount):
        if(len(self.bank_account) >= 2):
            print("Withdrow from:")
            self.bank_account[self.choose_account()].balance -= amount
            print("Deposit to:")
            self.bank_account[self.choose_account()].balance += amount
        else:
            print("Not enough accounts")



client1 = Client()
client1.add_account(2500)

client2 = Client()
client2.add_account(2600)

client1.transfer(client2, 350, "withdraw")
client1.print_accounts()
client2.print_accounts()