import socket

## Creating a UDP Socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

## A socket is a software endpoint through which one program sends or receives data.

server_socket.bind(("127.0.0.1", 5000))

print("UDP Server started")
print("Waiting for messages...")

while True:

    message, client_address = server_socket.recvfrom(1024)

    message = message.decode()

    print("Client:", message)

    if message == "Over":
        break

    reply = input("Enter reply: ")

    server_socket.sendto(reply.encode(), client_address)

server_socket.close()

print("Server closed")