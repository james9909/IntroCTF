import socket, math

SERVER = "introctf.koding.io"
PORT = 22222

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
sock.connect((SERVER, PORT))

response = sock.recv(1024)
print response
while sock:
    response = sock.recv(1024)
    print response.strip()
    try:
        ans = str(eval(response))
        print ans
        sock.send(ans + "\n")
    except:
        sock.close()
        break
    print sock.recv(1024).strip()
