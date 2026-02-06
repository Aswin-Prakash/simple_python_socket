# Server Code
import socket
s = socket.socket() # Create a socket object
port = 40674 # Define the port on which you want to bind the server
s.bind(('', port)) # Bind the socket to the port (empty string '' means all available IPs on the machine)
print(f"Socket successfully binded to port {port}")
s.listen(5)  # Put the socket into listening mode, Up to 5 connections can be queued
print("Socket is listening...")
# Keep the server running indefinitely
while True:
    c, addr = s.accept() # Establish connection with a client
    print(f"Got connection from {addr}")
    c.send(b'Thank you for connecting') # Send a thank you message to the client
    c.close() # Close the connection with the client