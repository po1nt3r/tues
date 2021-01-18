import socket
from time import time, ctime

t = time()
t1 = ctime(t)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    c, addr = s.accept()
    print("Socket Up and running with a connection from",addr)
    while True:
        
        rcvdData = c.recv(1024).decode('utf-8')

        if rcvdData == 'weather':
            c.send(bytes('sunny',"utf-8"))
        elif rcvdData == 'time':
            c.send(bytes(t1, 'utf-8'))
        elif rcvdData == 'airquality':
            c.send(bytes('very bad', 'utf-8')) 
        else: 
            c.send(bytes('NaN', 'utf-8'))
            c.close()
            break