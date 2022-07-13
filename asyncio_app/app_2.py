'''Socket Receiving and Sending Data over network'''
from cmath import e
import socket
from wsgiref.simple_server import server_version

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ("127.0.0.1",8000)
socket_server.bind(server_address)
socket_server.listen()
print("Listening to localhost:8000")

try:
    connection, client_address = socket_server.accept()
    print(f"I've got a connection from {client_address}")

    buffer = b''
    while buffer[-2:] != b'\r\n':
        data = connection.recv(2)
        if not data:
            break
        else:
            print(f"I've got data: {data}!")
            buffer = buffer + data
    print(f"All the data is {buffer}")
    connection.sendall(buffer)
finally:
    socket_server.close()