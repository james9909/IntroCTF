import socket, math

SERVER = "introctf.koding.io"
PORT = 22222

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
sock.connect((SERVER, PORT))

print sock.recv(1024) # This is how you print received data from the server
print sock.recv(1024)
sock.sendall("\n") # This is how you send information to the server
print sock.recv(1024)
print sock.recv(1024)
sock.sendall(str(120958 + 167063)+"\n")
print sock.recv(1024)
print sock.recv(1024)
sock.sendall(str(math.sqrt(876543212365))+"\n")
print sock.recv(1024)
print sock.recv(1024)
sock.sendall("\n")
print sock.recv(1024)
print sock.recv(1024)
sock.sendall(str(1005)+"\n")
print sock.recv(1024)
print sock.recv(1024)
a = math.factorial(8) * math.pow(3, 7)
sock.sendall(str(a)+"\n")
print sock.recv(1024)
print sock.recv(1024)
sock.sendall("\n")
