#############################################################################
# Program:
#   Multi-Thread Chat server
# Author:
#    Jordan Carlson
# Summary:
#    Scalable chat server allowing any number of connections dynamically under
#    predetermined size. Fluid communcation between clients without waiting.
#
#
# *****************************************************************************
#
# 
#     Client  -> server
#     Client  <- server
#     Client  -> server
#     Client  <- server
#     Client  -> server
#                server -> All Other Clients
#     Client  -> server
#     ...
#
##############################################################################

from array import array
import time
import sys
from socket import *
import threading

DEFAULT_VALUE = 6789
serverPort = int(sys.argv[1]) if len(sys.argv) == 2 else DEFAULT_VALUE

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen()

print('CHAT ROOM:', serverPort)

connectionPool = {}
def threadFunction():
    
    #Connection setup and introducion
    print("new thread")
    connectionSocket, addr = serverSocket.accept()
    connectionSocket.send('Hello, What is your name?'.encode('ascii'))
    name = connectionSocket.recv(1024).decode('ascii')
    connectionSocket.send(("Hi " + name + "! Enter messages: ").encode('ascii'))
   
    # Add connectionSocket to pool (dictionary)
    connectionPool[addr] = connectionSocket
    print(connectionPool)

    # Handle Client input and notify all other Clients
    while (True):
        message = connectionSocket.recv(1024).decode('ascii')
        # remove connection from pool (Server still runs when client drops)
        if (message == "CLOSE"):
            connectionPool.pop(addr)
        else:
            for key in connectionPool:
                obj = connectionPool[key]
                if obj != connectionSocket:
                    obj.send((name + ": " + message).encode('ascii'))
try:
    # Make 10 available threads/connections
    count = 0
    while (count < 10):
        thread = threading.Thread(target=threadFunction)
        thread.start()
        count += 1    
    
    # Indicate the Server is Still Running
    while (True):
        time.sleep(5)
        print("Server Running")
        
        
except OSError as e:
    print("Error in connecting", e)
    serverSocket.close()
    sys.exit(1)
except KeyboardInterrupt:
    print("\nClosing Server")
    serverSocket.close()
    sys.exit(1)
