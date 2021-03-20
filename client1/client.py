import json
import os
import pickle
import socket

IP = "34.77.60.185"
PORT = 8080


class Client:
    def __init__(self, ip, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ip = ip
        self.port = port
        self.command = ""
        self.data = ""
        self.command_dict = self.make_dict()
        self.index_dict = {
            "time": 0,
            "weather": 0,
            "airquality": 0
        }
        self.catch_up()

    def catch_up(self):
        keys = list(self.command_dict["Commands"])
        for i in range(len(keys)):
            if "time" in keys[i]:
                keys[i] = "time"
            elif "weather" in keys[i]:
                keys[i] = "weather"
            else:
                keys[i] = "airquality"
        self.index_dict["time"] += keys.count("time")
        self.index_dict["weather"] += keys.count("weather")
        self.index_dict["airquality"] += keys.count("airquality")

    def make_dict(self):
        if os.path.exists("commands.json"):
            with open("commands.json", "r") as fr:
                command_dict = json.load(fr)
            return command_dict
        else:
            command_dict = {
                "Commands": {}
            }
            return command_dict

    def send_data(self):
        self.command = input("Enter 'time', 'weather' or 'airquality': ")
        self.s.send(pickle.dumps(self.command))

    def recv_data(self):
        # Господине, pickle.dump()-нали сте информацията, която се връща 2 пъти
        self.data = pickle.loads(pickle.loads(self.s.recv(1024)))

    def est_connection(self):
        self.s.connect((self.ip, self.port))
        self.send_data()
        self.recv_data()
        self.s.close()

    def print_data(self):
        if self.command != "weather":
            print(self.data)
            self.command_dict["Commands"][self.command + str(self.index_dict[self.command])] = self.data
        else:
            print(self.data[0]["main"])
            self.command_dict["Commands"][self.command + str(self.index_dict[self.command])] = self.data[0]["main"]

    def save_data(self):
        with open("commands.json", "w") as fw:
            json.dump(self.command_dict, fw, indent=4)


def data_exchange(client1):
    if not isinstance(client1, Client):
        raise ValueError("Object not compatible")

    while True:
        if client1.s.fileno() == -1:
            client1.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client1.est_connection()
        client1.print_data()
        client1.save_data()

        if input("Type 1 to reestablish the connection: ") != '1':
            break


client = Client(IP, PORT)
data_exchange(client)