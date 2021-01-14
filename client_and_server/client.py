import socket

reest = ''

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 6969))
    while True:
        str = input("Enter weather, time or airquality: ")
        s.send(bytes(str, 'utf-8'))   
        return_value = s.recv(1024).decode('utf-8')
        print("Server:", return_value)

        if return_value == 'NaN':
            s.close()
            break
    print("Connection with the server has ended!")
    reest = input("Do you want to reestablish the connection(y/n): ")
    if reest == 'n':
        break

print('Goodbye!')