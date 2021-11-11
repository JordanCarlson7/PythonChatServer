#############################################################################
# Program:
#    Lab RPS, Computer Networks
#    Brother Jones, CSE354
# Author:
#    Jordan Carlson
# Summary:
#    RPS SERVER CODE
#
##############################################################################

from socket import *
from datetime import date
import sys
import os
CRLF = "\r\n"

# Successful connection and response to client
def send200(content):
   response = "HTTP/1.1 200 OK\r\n\n"
   connectionSocket.send(response.encode('ascii'))
   connectionSocket.send(content.encode('ascii'))
   return

# 404 File Not Found errors
def send404(content):
   response = "HTTP/1.1 404 Not Found\r\nContent-type: text/html\r\n\n"
   connectionSocket.send(response.encode('ascii'))
   connectionSocket.send(content.encode('ascii'))
   connectionSocket.close()
   return
   
# Server Connection Setup
serverPort = int(sys.argv[1]) if len(sys.argv) == 2 else 6789
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(2)
print ("Server is running on port " , str(serverPort))


try:
   # Main Server Loop
   while(True):
      # ACCEPT ANY REQUEST
      connectionSocket, addr = serverSocket.accept()
      data = connectionSocket.recv(1024).decode('ascii')
      if data:
         print("Client: ", connectionSocket, data)
         send200(data)
      else:
         break
      
      # DETERMINE GET REQUEST & REQUESTED FILE
      # split = data.split(' ')
      # requestVerb = split[0]
      # requestFile = split[1][1:]

      # DETERMINE IF FILE EXISTS
      
      
      

except KeyboardInterrupt:
   print ("\nClosing Server")
   send404("Hey you didnt connect")
   connectionSocket.close()
   serverSocket.close()
   quit()
