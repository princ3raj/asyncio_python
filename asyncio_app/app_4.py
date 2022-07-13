'''Non-blocking Sockets'''

import socket

socket_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('127.0.0.1', 8000)
socket_server.bind(server_address)
print("Listening to 127.0.0.1:8000")
socket_server.listen()
socket_server.setblocking(False)


connections = []
try:
    while True:
        try:
            connection, client_address = socket_server.accept()
            connection.setblocking(False)
            print(f"I have got a connection from {client_address}")
            connections.append(connection)
        except BlockingIOError:
            pass

        for connection in connections:
            buffer   = b''
            try:
                while buffer[-2:] != b'\r\n':
                    data = connection.recv(2)
                    if not data:
                        break
                    else:
                        print(f"I've got data {data}")
                        buffer = buffer + data
                print(f"All the data is: {buffer} ")
                connection.send(buffer)
            except BlockingIOError:
                pass
finally:
    socket_server.close()

