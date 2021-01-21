import socket
from time import time, ctime

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    c, addr = s.accept()
    print("Socket Up and running with a connection from",addr)
    while True:
        try:
            rcvdData = c.recv(1024).decode('utf-8')
        except:
            print("The client hasn't responded. The connection has ended!")
            c.close()
            break
        if rcvdData == 'weather':
            c.send(bytes('sunny',"utf-8"))
        elif rcvdData == 'time':
            t = time()
            t1 = ctime(t)
            c.send(bytes(t1, 'utf-8'))
        elif rcvdData == 'airquality':
            c.send(bytes('very bad', 'utf-8')) 
        elif rcvdData == 'bye':
            c.send(bytes("over", "utf-8"))
            print(f"The connection with {addr} has ended\n")
            c.close()
            break
        else:
            c.send(bytes('NaN', 'utf-8'))
            
            