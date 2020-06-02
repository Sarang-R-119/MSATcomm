import tkinter as tk
from threading import Thread
#standard library for socket programming
#socket is the endpoint on a connection line
import  socket

#IP address of the Host or Server
HOST = '172.16.64.31' #'192.168.43.223'
#Chooses a port that is not being used already
PORT = 5560

HEIGHT = 500
WIDTH = 500

#Sets up the Client.
#Creates a socket with attributes
#AF_INET -- IPV4 : chooses the type of address that the socket is going to communicate with and chooses Internet protocol version 4 address
#SOC_STREAM -- TCP : to choose a tcp protocol.
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.connect((HOST,PORT)) #Connects to the server with the specified IPV4 address and port chosen.
print("Connection created")

#Function used to send Messages to the Server.
def sendMessage(event = None):
	#Extracts the text entered from the text entry.
	command = text.get()
	print('Entered command: ' + command)
	display.insert(tk.END, "Client: " + command)

	if command == 'EXIT':
	    # Send EXIT request to other end and shuts down the Client, ending connection with the Server.
	    mySocket.send(str.encode(command))
	    print("Shutting down the Client.")
	    mySocket.close()

	elif command == 'KILL':
	    # Send KILL command to shut down the Server.
	    mySocket.send(str.encode(command))
	    print("Disconnected from the Server.")
	
	#Assuming relay is the main operation of raspberry pi 1, it sends the command to the raspberry pi 1.
	elif 'RELAY' in command:
		# Send command to the relay
		commands = command.split(' ', 1)
		relayCommand = commands[1]
		mySocket.send(str.encode(relayCommand))
	text.set("")

def listenMessage():
	#Listens for messages from the server continuously on a different thread.
	#Once a message is received, it is displayed onto the display of the window.
	#If there was no infinite loop, rest of the messages won't have been received.
	while True:	
	    print("Checking for messages")
	    reply = mySocket.recv(1024)
	    receivedMessage = reply.decode('utf-8')
	    print("Received message is " + receivedMessage)
	    display.insert(tk.END, receivedMessage)

#The special window to send and receive messages from the servers of the users choice.

root = tk.Tk()
root.title("Client")

#Main frame

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

#Background Image

backgroundImage = tk.PhotoImage(file = 'landscape.png')
backgroundLabel = tk.Label(root, image = backgroundImage)
backgroundLabel.place(relwidth = 1, relheight = 1)
print("Created Background")

#Top frame

topframe = tk.Frame(root, bg = 'red')
topframe.place( relx = 0.1, rely = 0.1, relheight = 0.075, relwidth = 0.8)	

text = tk.Entry(topframe, font = 40)
text.bind(sequence = "<Return>", func = sendMessage)
text.place(relwidth = 0.75, relheight = 1)

# the lambda expression creates a link to the function rather than invoking the function and returning its value to the object.

send = tk.Button(topframe, text = 'Send', font = 40, command = sendMessage)
send.place(relx = 0.75, relwidth = 0.25, relheight = 1)

print("Created the top frame")

#Bottom frame

bottomframe = tk.Frame(root, bg = 'blue')
bottomframe.place(relx = 0.1, rely = 0.2, relheight = 0.65, relwidth = 0.8)

scrollbar = tk.Scrollbar(bottomframe)
scrollbar.pack(side = tk.RIGHT,fill = tk.Y)

display = tk.Listbox(bottomframe, font = 40, bg = 'gray', yscrollcommand = scrollbar.set)
display.place(relwidth = 1, relheight = 1)

print("Created the lower frame")

client_receive_thread = Thread(target = listenMessage)
client_receive_thread.start()
root.mainloop()