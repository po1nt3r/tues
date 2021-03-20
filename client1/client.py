import json
import os
import pickle
import socket

if os.path.exists("commands.json"):
    with open("commands.json", "r") as fr:
        command_dict = json.load(fr)
else:
    command_dict = {
        "Commands": {}
    }

index_dict = {
    "time": 0,
    "weather": 0,
    "airquality": 0
}

keys = list(command_dict["Commands"])
for i in range(len(keys)):
    if "time" in keys[i]:
        keys[i] = "time"
    elif "weather" in keys[i]:
        keys[i] = "weather"
    else:
        keys[i] = "airquality"

index_dict["time"] += keys.count("time")
index_dict["weather"] += keys.count("weather")
index_dict["airquality"] += keys.count("airquality")

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("34.77.60.185", 8080))

    userInput = input("Enter 'time', 'weather' or 'airquality': ")
    index_dict[userInput] += 1

    command = pickle.dumps(userInput)
    s.send(command)
    data = s.recv(1024)

    # Господине, pickle.dump()-нали сте информацията, която се връща 2 пъти
    decode_data1 = pickle.loads(data)
    decode_data2 = pickle.loads(decode_data1)

    s.close()

    if userInput != 'weather':
        print(decode_data2)
        command_dict["Commands"][userInput + str(index_dict[userInput])] = decode_data2
    else:
        print(decode_data2[0]['main'])
        command_dict["Commands"][userInput + str(index_dict[userInput])] = decode_data2[0]['main']

    print(command_dict)

    if input("Type 1 to reestablish the connection: ") != '1':
        break

with open("commands.json", "w") as fw:
    json.dump(command_dict, fw, indent=4)
