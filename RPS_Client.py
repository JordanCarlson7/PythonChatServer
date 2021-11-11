#############################################################################
# Program:
#    Lab RPS, Computer Networks
#    Brother Jones, CSE354
# Author:
#    Jordan Carlson
# Summary:
#    RPS client CODE
#
##############################################################################

from socket import *
from datetime import date
import sys
import os
CRLF = "\r\n"
   
# Successful connection and response to client
def send200(content):
   response = f"HTTP/1.1 200 OK\r\nConnection: Close\r\nContent-type: text/html\r\n\n"
#    connectionSocket.send(response.encode('ascii'))
#    connectionSocket.send(content.encode('ascii'))
#    connectionSocket.close()
   return

# 404 File Not Found errors
def send404():
#    response = "HTTP/1.1 404 Not Found\r\nContent-type: text/html\r\n\n"
#    connectionSocket.send(response.encode('ascii'))
#    connectionSocket.close()
   return
   
# client Connection Setup
clientPort = int(sys.argv[1]) if len(sys.argv) == 2 else 6789
clientSocket = socket(AF_INET, SOCK_STREAM)
print ("client is running on port " , str(clientPort))


try:
   # Main client Loop
    # clientSocket.send("GET HTTP/1.1 Hi I am your client!".encode('ascii'))
    while 1:
        rps = input("R, P, S, or Quit: ")
        clientSocket.send("")
        response = clientSocket.recv(1024).decode('ascii')
        print("Server", response)
        
      # ACCEPT ANY REQUEST
    #   connectionSocket, addr = clientSocket.accept()
    #   data = connectionSocket.recv(1024).decode('ascii')
    
    #   # DETERMINE GET REQUEST & REQUESTED FILE
    #   split = data.split(' ')
    #   requestVerb = split[0]
    #   requestFile = split[1][1:]

    #   # DETERMINE IF FILE EXISTS
    #   send200("HEY you connected!")
      
      

except KeyboardInterrupt:
   print ("\nClosing client")
   clientSocket.close()
   quit()
