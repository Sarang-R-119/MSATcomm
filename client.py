import  socket

host = '172.30.50.145'
port = 5560

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.connect((host,port))

while True:
    command = input("Enter your command: ")
    if command == 'EXIT':
        # Send EXIT request to other end
        mySocket.send(str.encode(command))
        break
    elif command == 'KILL':
        # Send KILL command
        mySocket.send(str.encode(command))
        break
    mySocket.send(str.encode(command))
    reply = mySocket.recv(1024)
    print(reply.decode('utf-8'))
mySocket.close()
