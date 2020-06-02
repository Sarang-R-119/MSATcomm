#standard library for socket programming
#socket is the endpoint on a connection line
import socket

from Relay import *

#IP address of the Host or Server
HOST = ''
serverMessage = 'Thankfully it worked'
#Chooses a port that is not being used already
PORT = 5560

#Establishes the server socket and returns the server socket.
def setupServer():
	#Sets up the Client.
	#Creates a socket with attributes
	#AF_INET -- IPV4 : chooses the type of address that the socket is going to communicate with and chooses Internet protocol version 4 address
	#SOC_STREAM -- TCP : to choose a tcp protocol.
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket Created")

    #Binds the server's socket. Establishes the connection.
    try:
        s.bind((HOST,PORT))

    except socket.error as errorMessage:
        print(errorMessage)

    print("Socket bind complete.")
    return s

#extra starts
def GET():
    return serverMessage

def REPEAT(dataMessage):
    return dataMessage[1]

def MESSAGE(dataMessage):
	reply = input('client: ' + dataMessage[1] + '\n')
	return 'Server: ' + reply
#extra ends

#Establishes a connection between a client socket and the server socket.
#Listens for 2 connections at a time and gets the credentials of the client socket.
#Finally, it returns an instance of the client socket.
def setupConnection():
    s.listen(2);
    connection, address = s.accept()

    print("Connected to: " + str(address[0]))
    return connection

#Receives Messages from the client and decides the course of action accordingly.
def dataTransfer(connection):

    while True:
    	#Receives a message of maximum limit of 1024 bytes.
        data = connection.recv(1024)
        data = data.decode('utf-8')

        #Splits the message into two for checking the command word.
        dataMessage = data.split(' ', 1)
        command = dataMessage[0]

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
            break

        elif command == 'ON':
        	reply = "Relay is switched ON"
        	relaySwitchON()

        elif command == 'OFF':
        	reply = "Relay is switched OFF"
        	relaySwitchOFF()
        	
        else:
            print('Unknown command')

        connection.sendall(str.encode(reply))
        print('Data has been sent!')
    connection.close();

s = setupServer()
setupRelay()

while True:
    try:
        connection = setupConnection()
        dataTransfer(connection)
    except:
        break
