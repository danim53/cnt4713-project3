import socket
import rsa
import hashlib

HOST = "127.0.0.1"
CONTROL_PORT = 8080

def main():
    print("Starting server…")
    print("Creating RSA keypair")
    public_key, private_key = rsa.newkeys(1024)
    print("RSA keypair created")

    print("Creating server socket")
    server = socket.socket()
    server.bind((HOST, CONTROL_PORT))
    server.listen(1)

    print("Awaiting connections…")
    
    while True:
        connect, addr = server.accept()
        
        command = connect.recv(1024).decode()
        
        if command == "connect":
            print("Connection requested. Creating data socket")
            data_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            data_server.bind((HOST, 0))
            data_server.listen(1)
            
            port = data_server.getsockname()[1]
            connect.send(str(port).encode())
            
            data_connection, data_addr = data_server.accept()
            
            client_public_key = None
            
            while True:
                command = data_connection.recv(1024).decode()
                if not command:
                    break
                
                if command == "tunnel":
                    print("Tunnel requested. Sending public key")

                    data_connection.send(b"OK")
                    client_key_pem = data_connection.recv(4096)
                    client_public_key = rsa.PublicKey.load_pkcs1(client_key_pem)
                    data_connection.send(public_key.save_pkcs1("PEM"))
                    
                elif command == "post":
                    print("Post requested.")
                    data_connection.send(b"OK")
                    
                    encrypted = data_connection.recv(4096)
                    print(f"Received encrypted message: {encrypted}")
                    
                    # decrypt message
                    message = rsa.decrypt(encrypted, private_key).decode()
                    print(f"Decrypted message: {message}")

                    print("Computing hash")
                    
                    # compute hash
                    msg_hash = hashlib.sha256(message.encode()).hexdigest()
                    print(f"Responding with hash: {msg_hash}")
                    
                    # encrypt hash with client's public key
                    encrypted_hash = rsa.encrypt(msg_hash.encode(), client_public_key)
                    data_connection.send(encrypted_hash)
                    break
                    
            data_connection.close()
            data_server.close()
        connect.close()

if __name__ == "__main__":
    main()
