import random
import os
import yaml
import argparse
import uuid
import os

PATH = None

def new_client(client_list):
    if isinstance(client_list, list):
        client_list.append(Client())
    else:
        raise ValueError("Object is not a list")

def clients_for_transaction(client_list, transaction_properties):
    transaction_pr = ['', '', int(transaction_properties[2])]
    for i in client_list:
        if i.id == transaction_properties[0]:
            transaction_pr[0] = i
        elif i.id == transaction_properties[1]:
            transaction_pr[1] = i
    
    if "" in transaction_pr:
        raise ValueError("Client id does not exist")          
    
    return transaction_pr      
            
def clear_screen():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

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
            self.account_dict = self.read_file()
            self.bank_accounts = []
            self.num_accounts = 0
            if len(self.account_dict) >= Client.num_of_clients:
                self.id = list(self.account_dict.keys())[Client.num_of_clients-1]
                self.num_accounts = len(self.account_dict[self.id])
                self.bank_accounts.extend(self.account_dict[self.id])
            else:
                self.id = str(uuid.uuid4())
                self.add_bank_account(int(input("Enter balance: ")))
                self.account_dict.update({self.id : [i for i in self.bank_accounts]})
                with open("accounts.yaml", "a") as fw:
                    yaml.dump({self.id : [i for i in self.bank_accounts]}, fw)

        else:
            self.bank_accounts = []
            self.num_accounts = 0
            self.add_bank_account(int(input("Enter balance: ")))            
            self.id = str(uuid.uuid4())         
            self.account_dict = {self.id:[i for i in self.bank_accounts]}
            print(self.account_dict)
            self.write_file()
            
    def write_file(self):
        with open(PATH, "w") as fw:
            yaml.dump(self.account_dict, fw)
    
    def read_file(self):
        with open(PATH, "r") as fr:
            return yaml.full_load(fr)

    def add_bank_account(self, amount, modify = False):
        self.num_accounts += 1
        b = BankAccount(amount)
        self.bank_accounts.append({f"Account {self.num_accounts}": b.balance})

        if modify:
            self.account_dict = self.read_file()
            self.account_dict[self.id] = self.bank_accounts
            self.write_file()

    def print_acc(self):    
        for i in self.bank_accounts:
            print(i)

    def deposit(self, amount):
        if not self.bank_accounts:
            raise ValueError("No bank accounts")
        self.print_acc()
        acc_num = int(input("Enter the number of the account to choose it: "))
        self.account_dict[self.id][acc_num-1][f"Account {acc_num}"] += amount
        self.write_file()

    def withdraw(self, amount):
        if not self.bank_accounts:
            raise ValueError("No bank accounts")
        self.print_acc()
        acc_num = int(input("Enter the number of the account to choose it: "))
        self.account_dict[self.id][acc_num-1][f"Account {acc_num}"] -= amount
        self.write_file()

    def transfer(self, client, amount, operation="deposit"):
        if not isinstance(client, Client):
            print("Not a client")
            return
        if operation == "deposit":
            client.withdraw(amount)
            self.account_dict = self.read_file()
            self.deposit(amount)
        else:
            client.deposit(amount)
            self.account_dict = self.read_file()
            self.withdraw(amount)
            
            
parser = argparse.ArgumentParser()

parser.add_argument("-f", action="store", dest="filename", required=True,
                    help="Path to yaml file.")
parser.add_argument("-a", action="store", dest="add_clients", type=int, required=True,
                    help="Number of clients to be added.")
parser.add_argument("-t", action="store", dest="transaction_type", help="deposit - deposit to client1, withdraw from client2 |\
                    withdraw - withdraw from client1, deposit to client 2 | default is deposit",
                    default="deposit")
parser.add_argument("-o", action="store", dest="transaction_properties", nargs=3, default = None,
                    help="id of client to withdraw/deposit (you) | id of client to withdraw/deposit | amount")

options = parser.parse_args()
PATH = options.filename
client_list = []

print("Create accounts")
for _ in range(options.add_clients):
    new_client(client_list)

clear_screen()

print("Transaction")
if options.transaction_properties:
    if options.transaction_type == 'deposit':
        transaction_pr = clients_for_transaction(client_list, options.transaction_properties)
        transaction_pr[0].transfer(transaction_pr[1], transaction_pr[2])
    else:
        transaction_pr = clients_for_transaction(client_list, options.transaction_properties)
        transaction_pr[0].transfer(transaction_pr[1], transaction_pr[2], operation="withdraw")
else:
    transaction_type = input("Enter transaction type: ")
    for i in client_list:
            print(i.id)
    if transaction_type == 'deposit':
        transaction_pr = clients_for_transaction(client_list, [input("ID of user to which to deposit"), 
                                                               input("ID of user from which to withdraw"),
                                                               int(input("Amount for transaction"))])
        clear_screen()
        transaction_pr[0].transfer(transaction_pr[1], transaction_pr[2])
    else:
        transaction_pr = clients_for_transaction(client_list, [input("ID of user to which to withdraw"), 
                                                               input("ID of user from which to deposit"),
                                                               int(input("Amount for transaction"))]) 
        clear_screen()
        transaction_pr[0].transfer(transaction_pr[1], transaction_pr[2], operation="withdraw")

    

