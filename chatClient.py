#############################################################################
# Program:
#   Multi-Thread Chat Client
# Author:
#    Jordan Carlson
# Summary:
#   Client to communicate with other clients via a central multithread server
#
##############################################################################


import sys
from socket import *
import threading
import time

DEFAULT_VALUE = 6789

# Allow for custom hosts and ports
serverName, serverPort = (sys.argv[1] if len(sys.argv) == 3 else "localhost", int(
    sys.argv[2]) if len(sys.argv) == 3 else DEFAULT_VALUE)
clientSocket = socket(AF_INET, SOCK_STREAM)

try:
    # Connect client port and server port
    clientSocket.connect((serverName, serverPort))
except gaierror as e:
    print("Bad hostname: ", e)
    sys.exit(1)
except error as e:
    print("Bad port number: ", e)
    sys.exit(1)
print("Usage: ", serverName, serverPort)

# Initial connection
connected = clientSocket.recv(1024).decode('ascii')

if connected:
    print("Server Responded:", connected)

# Send client specific data to client to confirm connection
name = input('Name: ')
clientSocket.send(name.encode('ascii'))
print(clientSocket.recv(1024).decode('ascii'))

# Separate thread for LISTENING to server response


def threadFunction():
    while (True):
        response = clientSocket.recv(1024).decode('ascii')
        # Allow easy distinction between client and data received from server
        print("                " + response)


thread = threading.Thread(target=threadFunction)
thread.start()

try:
    # Send initial message to start the conversation
    msg = input()
    clientSocket.send(msg.encode('ascii'))

    # Main execution for SENDING requests/messages to server
    while(True):
        msg = input()
        clientSocket.send(msg.encode('ascii'))

except KeyboardInterrupt:
    print("\nClosing Server")
    clientSocket.send("CLOSE".encode('ascii'))
    clientSocket.close()
    sys.exit(1)
