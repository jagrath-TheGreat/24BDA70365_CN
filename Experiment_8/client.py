
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

## SOCK_STREAM: represents TCP Segment / TCP Data

client_socket.connect(("127.0.0.1", 5000))

## Client connecting to server with 127.0.0.1 on port 5000

print("Connected to server")

while True:
    message = input("Enter message: ")

    client_socket.send(message.encode())   ##Encode(): Converts raw string to bytes

    if message == "Over":
        break

    reply = client_socket.recv(1024).decode()

    print("Server:", reply)

client_socket.close()

print("Connection closed")