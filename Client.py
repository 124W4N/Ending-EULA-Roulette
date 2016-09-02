# EqualisingEULA web service//Client Side that sends detected EULA
# and receive information from server and present to user screen

import socket

# create a socket object
ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = 9999

# connection to hostname on the port.
ClientSocket.connect((host, port))

# Client will send to the server the EULA
EULAdir = 'EULAcorpus/'
filename='NEWEula.txt'
f = open(EULAdir + filename, 'r')
EULA = f.read()
f.close()
ClientSocket.send( EULA)

# Receive no more than 90000 bytes = 90 KB
Receive = ClientSocket.recv(90000)

ClientSocket.close()

print("The information received from the server: %s" % Receive.decode('ascii'))
