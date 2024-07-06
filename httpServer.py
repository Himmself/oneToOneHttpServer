import socket

SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)

print('Listening on port %s ...' % SERVER_PORT)

while True:
    # Wait for client connections
    client_connection, client_address = server_socket.accept()

    # Get Client Request
    request = client_connection.recv(1024).decode()
    # print(request)

    # Parse Headers of HTTP
    headers = request.split('\n')
    filename = headers[0].split()[1]
    # print("[ ] FILENAME = ", filename)

    if filename == '/':
        filename = 'index.html'
    elif filename == '/ipsum':
        filename = 'ipsum.html'
    else:
        filename = '404.html'

    # Get Page contents
    file = open('htdocs/'+filename)
    content = file.read()
    file.close()

    response = 'HTTP/1.0 200 OK\n\n' + content
    client_connection.sendall(response.encode())
    client_connection.close()

server_socket.close()