import socket, math

SERVER = "introctf.koding.io"
PORT = 22222

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
sock.connect((SERVER, PORT))

response = sock.recv(1024)
print response
response = response.translate(None, "abcdefghijklmnopqrstuvwxyz ")
while sock:
    response = sock.recv(1024)
    print response
    sock.send(str(eval(response)) + "\n")
    print sock.recv(1024)
