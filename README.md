# Server-Client Model using RC4 Encryption
The purpose of this repository is to implement a **server-client model** where the messages being sent and received are encrypted and decrypted using the **RC4** encryption algorithm. This project demonstrates the use of **RC4** in a real-world application for secure communication between the server and client.

## Overview

This project simulates a simple communication system between a server and client, with messages being encrypted using the **RC4 encryption algorithm** before being sent over the network. Both the server and client have the ability to:

- **Encrypt** the message using RC4 before transmission.
- **Decrypt** the message upon receiving it to retrieve the original text.

## Features

- **RC4 encryption** for secure communication between server and client.
- Simple **key exchange mechanism** for initializing encryption.
- Encryption and decryption of messages over the network.
- Demonstration of secure message transmission using RC4.

## Technologies Used

- Python 3
- **RC4 Encryption Algorithm**
- Sockets (for communication between server and client)

## How to Run

1. Install necessary dependencies (if applicable):
   ```bash
   pip install rc4
   ```

2. Run the server:
   ```bash
   python server.py
   ```

3. Run the client:
   ```bash
   python client.py
   ```

4. The client will connect to the server, encrypt the message with RC4, and the server will decrypt it and respond back.

## Note

RC4 is a **stream cipher** and while historically popular for encryption, it is no longer considered secure for modern use. This project is meant for educational purposes to understand the implementation and usage of RC4 in a basic client-server model.
