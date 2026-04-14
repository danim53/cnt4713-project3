import socket
from idlelib.undo import Command
import rsa
import hashlib
from multiprocessing import connection

HOST ="127.0.0.1"
CONTROL_PORT = 8080

print("Starting Server...")
print("Creating RSA keypair")
public_key, private_key = rsa.newkeys(512)
print("RSA keypair created")

print("Creating server socket")
server = socket.socket()
server.bind((HOST, CONTROL_PORT))
server.listen()

print("Awaiting connection...")
connect, addr = server.accept()

# command
command = connect.recv(1024).decode()

if command == "CONNECT":
    print("Connection requested. Creating data soket")
    data_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    data_server.bind((HOST, CONTROL_PORT))
    data_server.listen()

    port = data_server.getsockname()[1]
    data_server.sendto(command.encode(), (HOST, port))

    data_connection, addr = server.accept()




# Post
command = data_connection.recv(1024).decode()
if command == "POST":
    print("POST requested.")

    encypted = data_connection.recv(4096)
    print("Recieved encrypted message:", encypted)

    #decrpt message
    message = rsa.decrypt(encypted, private_key).decode()
    print("Decrypted message:", message)

    print("Computing hash")
    hash = hashlib.sha256(message.encode()).hexdigest()

    #encrypt hash
    hash = hashlib.sha256(hash.encode(), client_public_key)
    print("Responding with hash:", hash)
    data_connection.send(encypted_hash)





