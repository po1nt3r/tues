import socket

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("34.77.60.185", 8080))
    while True:
        userInput = input("Enter time, weather or air quality")
        s.send(bytes(userInput, "utf-8"))
        print(s.recv(1024).decode("utf-8"))
        if userInput == "bye":
            s.close()
            break
    if input("Type 1 to reestablish the connection: ") != '1':
        break
