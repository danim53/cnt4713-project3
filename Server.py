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

print("Creating server scoket")
server = socket.socket()
server.bind((HOST, CONTROL_PORT))
server.listen()

print("Awaiting connection...")
connect, addr = server.accept()

# command
command = con.recv(1024).decode()

if command == "CONNECT":
    print("Connection requested. Creating data soket")
    data_server = socket.socket(
