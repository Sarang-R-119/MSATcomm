import socket
from Relay import RELAY

host = ''
serverMessage = 'Server is connected. Test complete.'
port = 5560

def setupServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket Created")
    try:
        s.bind((host,port))
    except socket.error as msg:
        print(msg)

    print("Socket bind complete.")
    return s

#To test if the server and the client can communicate with each other. (Debugging)
def GET():
    return serverMessage

def REPEAT(dataMessage):
    return dataMessage[1] 

#ADDED
def HEATER(data):
    data.split(' ', 1)
    if data[0] == 'RELAY1':

        if(data[1] == 'ON'):

            RELAY()


def setupConnection():
    s.listen(1);
    connection, address = s.accept()
    print("Connected to: " + address[0] + ":" + str(address[1]))
    return connection

def dataTransfer(connection):
    while True:
        #Receives the messages from the client
        #Messages transferred are commands to run this subsystem
        data = connection.recv(1024)
        data = data.decode('utf-8')
        dataMessage = data.split(' ', 1)
        command = dataMessage[0]
        commandElement = dataMessage[1]

        if command == 'GET':
            reply = GET()

        elif command == 'REPEAT':
            reply = REPEAT(dataMessage)
            print('Repeated message was: ' + reply)

        elif command == 'EXIT':
            print("There is no client anymore")
            break

        elif command == 'KILL':
            print('Server is shutting down')
            s.close()
        #ADDED
        elif command == 'HEATER'
            reply = HEATER(commandElement)

        else:
            print('Unknown command')
            
        connection.sendall(str.encode(reply))
        print('Data has been sent!')
    connection.close();

s = setupServer()

while True:
    try:
        connection = setupConnection()
        dataTransfer(connection)
    except:
        break

        

