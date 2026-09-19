import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ("127.0.0.1", 5000)

print("UDP Client started")

while True:

    message = input("Enter message: ")

    client_socket.sendto(message.encode(), server_address)

    if message == "Over":
        break

    reply, server_address_received = client_socket.recvfrom(1024)

    print("Server:", reply.decode())

client_socket.close()

print("Client closed")