# Cryptography Client-Server Messaging Project

A secure messaging application built in **Python** using **TCP sockets**, **RSA encryption**, and **SHA256 hashing**. This project demonstrates how a client and server can exchange encrypted messages and verify their integrity.

---

## 📋 Overview

This project implements a client-server system where:

- Both client and server generate RSA keypairs
- Public keys are exchanged securely
- Messages are encrypted before transmission
- Message integrity is verified using SHA256 hashing

The client sends an encrypted message to the server, and the server responds with a hash used to verify whether the message was altered during transmission.

---

## ⭐ Key Features

- TCP socket communication  
- RSA public/private key generation  
- Public key exchange (`tunnel`)  
- Encrypted messaging (`post`)  
- SHA256 hashing for integrity  
- Secure/Compromised verification  

---

## 🏗️ How It Works

1. Client connects to server using `connect`
2. A data socket is established
3. Client sends its public key (`tunnel`)
4. Server responds with its public key
5. Client encrypts a message using server’s public key
6. Client sends encrypted message (`post`)
7. Server decrypts message and computes SHA256 hash
8. Server encrypts hash and sends it back
9. Client compares hashes:
   - Match → **Secure**
   - No match → **Compromised**

---

## 🔄 Communication Flow

Client → Server: `connect`  
Client → Server: `tunnel` (public key exchange)  
Client → Server: `post` (encrypted message)  
Server → Client: encrypted hash  

---

## 🚀 Running the Program

### Start the Server

python server.py

### Start the Client

python client.py

---

## 🧪 Example Output

### Server

Starting server…
Creating RSA keypair
RSA keypair created
Awaiting connections…
Post requested.
Decrypted message: Hello
Responding with hash: <hash>

### Client

Starting client…
Connecting to server
Tunnel established
Encrypting message: Hello
Received hash
Secure


---

## 🔐 Cryptography Used

- **RSA Encryption**: Secures message transmission using public/private keys  
- **SHA256 Hashing**: Ensures message integrity  

---

## 📦 Files

- `server.py` – server implementation  
- `client.py` – client implementation   
- `answers.txt` – written responses  

---

## 🔍 Security Notes

This system demonstrates core cryptography concepts but may be vulnerable to:

- Man-in-the-middle attacks  
- No public key authentication  
- Replay attacks  

Possible improvements:
- Use digital certificates  
- Add key verification  
- Implement TLS  

---

## 📊 Grading Breakdown

| Component | Weight |
|----------|-------:|
| connect | 20% |
| tunnel | 20% |
| post | 20% |
| Secure/Compromised | 20% |
| Written answers | 15% |
| Video | 5% |

---

## 👤 Authors

Danielle Martin  
Migdony Romero  
Xavier Williams  

---

## 🎓 Course

**CNT 4713 – Cryptography Project**
