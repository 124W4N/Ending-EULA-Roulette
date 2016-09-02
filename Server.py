# EqualisingEULA web service//Server Side

import socket

# create a socket object
ServerSocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()
port = 9999

# bind to the port
ServerSocket.bind((host, port))

# queue up to 5 requests
ServerSocket.listen(5)

while True:
    # establish a connection
    clientsocket,addr = ServerSocket.accept()
    Receive = clientsocket.recv(90000)
    print("Got a connection from client %s" % str(addr))
    # 1- RECIEVE THE EULA FROM CLIENTS
    print("The EULA got from the client is:\n %s" % Receive.decode('ascii'))
    # 2- SEND TO EULA ANALYZER
    # 3- GET RESULTS
    # 4- SEND BACK THE RESULTS
    clientsocket.send("Hey from the server, information regarding EULA includes...")
    clientsocket.close()
