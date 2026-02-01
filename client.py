# Client Code
import socket
s = socket.socket() # Create a socket object
port = 40674 # Define the port on which you want to connect to the server
s.connect(('127.0.0.1', port)) # Connect to the server
print(s.recv(1024).decode()) # Receive and print the message from the server
s.close() # Close the connection