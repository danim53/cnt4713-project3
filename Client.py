import socket
import rsa
import hashlib

HOST = '127.0.0.1'
CONTROL_PORT = 8080

def main():
    print('Starting client…')
    # Generate key pair without printing (as per Example Output)
    public_key, private_key = rsa.newkeys(1024)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print('Connecting to server')
    client_socket.connect((HOST, CONTROL_PORT))

    client_socket.send("connect".encode())

    data_port = int(client_socket.recv(4096).decode())

    data_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    data_socket.connect((HOST, data_port))

    # Requesting tunnel
    data_socket.send("tunnel".encode())
    data_socket.recv(1024) # wait for OK
    
    # Send client public key
    client_key_pem = public_key.save_pkcs1("PEM")
    data_socket.send(client_key_pem)
    
    # Receive server public key
    server_key_txt = data_socket.recv(4096)
    server_public_key = rsa.PublicKey.load_pkcs1(server_key_txt)
    
    print("Tunnel established")

    message = "Hello"
    print(f"Encrypting message: {message}")

    # Encrypt message
    encrypted_msg = rsa.encrypt(message.encode(), server_public_key)

    # Post message
    data_socket.send("post".encode())
    data_socket.recv(1024) # wait for OK
    data_socket.send(encrypted_msg)

    # Receive encrypted hash
    encrypted_hash = data_socket.recv(4096)
    print("Received hash")
    
    # Decrypt hash
    returned_hash = rsa.decrypt(encrypted_hash, private_key).decode()

    # Compare hash
    my_hash = hashlib.sha256(message.encode()).hexdigest()

    if returned_hash == my_hash:
        print("Secure")
    else:
        print("Compromised")

    data_socket.close()
    client_socket.close()

if __name__ == "__main__":
    main()