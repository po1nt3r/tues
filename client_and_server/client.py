import socket
import os

def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

reest = ''

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 1234))
    while True:
        string = input("Type weather, time or airquality |if you want to exit type 'bye'|: ")
        s.send(bytes(string, 'utf-8'))   
        return_value = s.recv(1024).decode('utf-8')

        print("\nServer: " + return_value + "\n")
        input("Press any key to continue")
        clear()
        if return_value == 'over':
            print("The connection is over!")
            s.close()
            break
    reest = input("Type 1 to reestablish the connection: ")
    if reest != '1':
        break

print('Goodbye!')