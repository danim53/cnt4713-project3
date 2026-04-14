import socket

HOST = '127.0.0.1'
CONTROL_PORT = 8080

def main():
    print('Starting client...')
    print('Creating RSA keypair')
    #public key & private key = generate key pair
    print('RSA keypair created')

    print("Creating client socket")
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print("Connecting to the server")
    client_socket.connect((HOST, CONTROL_PORT))

    client_socket.send("connect".encode())

    data_port = int(client_socket.recv(4096).decode())

    print("Creating data socket")
    data_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    data_socket.connect((HOST, data_port))

    print("Requesting tunnel")
    #insert tunnel message
    data_socket.send("tunnel".encode())

    server_key_txt = data_socket.recv(8192).decode()
    #add deserialized key

    print("Server public key received")
    print("Tunnel established")

    message = "Hello"
    print(f"Encrypting message: {message}")

    #serialize cipher
    #post message

    encrypted_hash = data_socket.recv(8192).decode()

    print("Received hash")
    print("Computing hash")

    #encrypt & return hash

    #my_hash = hash_message(message)

    #if returned_hash == my_hash:
        #print("Secure")
    #else:
        #print("Compromised")

    data_socket.close()
    client_socket.close()

if __name__ == "__main__":
    main()