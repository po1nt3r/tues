import random
import os
import yaml

alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
PATH = "accounts.yaml"

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    # def deposit(self,  amount):
    #     self.balance += amount

    # def withdraw(self, amount):
    #     if self.balance - amount < 0:
    #         print("Can't withdraw money")
    #         return
    #     self.balance -= amount

    def get_balance(self):
        print(self.balance)
        return self.balance


class Client():

    num_of_clients = 0

    def __init__(self):
        Client.num_of_clients += 1 
        if os.path.exists(PATH):
            with open(PATH, "r") as fr:
                self.account_dict = yaml.full_load(fr)
                self.bank_accounts = []
                self.num_accounts = 0
            if len(self.account_dict) >= Client.num_of_clients:
                self.id = list(self.account_dict.keys())[Client.num_of_clients-1]
                self.num_accounts = len(self.account_dict[self.id])
                self.bank_accounts.extend(self.account_dict[self.id])
            else:
                self.id = ''
                for _ in range(0, 8):
                    self.id += random.choice(alphabet)
                self.add_bank_account(int(input("Enter balance: ")))
                self.account_dict.update({self.id : i for i in self.bank_accounts})
                with open("accounts.yaml", "a") as fw:
                    yaml.dump({self.id : [i for i in self.bank_accounts]}, fw)

        else:
            self.bank_accounts = []
            self.num_accounts = 0
            self.add_bank_account(int(input("Enter balance: ")))            
            self.id = ""
            for _ in range(0, 8):
                self.id += random.choice(alphabet)            
            self.account_dict = {self.id:self.bank_accounts[0]}
            with open(PATH, "w") as fw:
                yaml.dump(self.account_dict, fw)
            


    def add_bank_account(self, amount, modify = False):
        self.num_accounts += 1
        b = BankAccount(amount)
        self.bank_accounts.append({f"Account {self.num_accounts}": b.balance})

        if modify:
            with open("accounts.yaml", "r") as fr:
                self.account_dict = yaml.load(fr, Loader=yaml.FullLoader)
                # print(self.account_dict)
                self.account_dict[self.id] = self.bank_accounts

                # print(self.account_dict)
                with open("accounts.yaml", "w") as fw:
                    yaml.dump(self.account_dict, fw)

    def print_acc(self):    
        for i in self.bank_accounts:
            print(i)

    def deposit(self, amount):
        if not self.bank_accounts:
            raise ValueError("No bank accounts")
        print("banana")
        self.print_acc()
        acc_num = int(input("Enter the number of the account to choose it: "))
        self.account_dict[self.id][acc_num-1][f"Account {acc_num}"] += amount
        with open("accounts.yaml", "w") as fw:
            yaml.dump(self.account_dict, fw)
        

    def withdraw(self, amount):
        if not self.bank_accounts:
            raise ValueError("No bank accounts")
        self.print_acc()
        acc_num = int(input("Enter the number of the account to choose it: "))
        self.account_dict[self.id][acc_num-1][f"Account {acc_num}"] -= amount
        with open("accounts.yaml", "w") as fw:
            yaml.dump(self.account_dict, fw)

    def transfer(self, client, amount, operation="deposit"):
        if not isinstance(client, Client):
            print("Not a client")
            return
        if operation == "deposit":
            # add reading and writing
            client.withdraw(amount)
            with open("accounts.yaml", "r") as fr:
                self.account_dict = yaml.full_load(fr)
            self.deposit(amount)
        else:
            client.deposit(amount)
            with open("accounts.yaml", "r") as fr:
                self.account_dict = yaml.full_load(fr)
            self.withdraw(amount)

client1 = Client()
print(client1.account_dict)
client2 = Client()
client2.transfer(client1, 250, "deposit")

