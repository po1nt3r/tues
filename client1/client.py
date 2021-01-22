import socket
import pickle

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("34.77.60.185", 8080))
    
    userInput = input("Enter 'time', 'weather' or 'airquality': ")
    command = pickle.dumps(userInput)
    s.send(command)
    data = s.recv(1024)

    #Господине, pickle.dump()-нали сте информацията, която се връща 2 пъти
    decode_data1 = pickle.loads(data)
    decode_data2 = pickle.loads(decode_data1)

    s.close()

    print(decode_data2)

    if input("Type 1 to reestablish the connection: ") != 1:
        break


    
