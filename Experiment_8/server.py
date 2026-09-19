import socket
##This module lets programs communicate over a network.

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

##socket.AF_NET: means use IPV4
##socket.SOCK_STREAM: means use TCP,
##In short: Create an IPV4 TCP Socket.

server_socket.bind(("127.0.0.1", 5000)) ##Binding Server IP and Port
##127.0.0.1 means localhost, so both program will run on same PC.

server_socket.listen(1)
##Server, start waiting for incoming TCP connection requests.

print("Server started")
print("Waiting for a client...")

client_socket, client_address = server_socket.accept()
## Accept waits until a client establishes a TCP Connection.
## If no client has connected, the program will pause over here only.

''' This command waits for a client.

The server stops here until a client connects.'''


print("Client connected:", client_address)

while True:
    message = client_socket.recv(1024).decode()
    ## Will decode the coming message from the client of 1024 bytes.
    # It attempts to receive up to 1024 bytes from the TCP connection.

    print("Client:", message)

    if message == "Over":
        break

    ## Server Reply
    reply = input("Enter reply: ")

    client_socket.send(reply.encode())

client_socket.close()
server_socket.close()

print("Connection closed")