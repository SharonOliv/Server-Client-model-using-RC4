import socket
from Crypto.Cipher import ARC4
KEY = b'topsecret@!$'  # Shared secret key for RC4
def rc4_encrypt(data, key):
    cipher = ARC4.new(key)
    return cipher.encrypt(data)

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("10.1.95.131", 21321))
    print("Connected to server!")
    input_file = "text.txt"
    encrypted_file = "encrypted.txt"
    with open(input_file, "rb") as f:
        plaintext = f.read()
    encrypted_data = rc4_encrypt(plaintext, KEY)
    with open(encrypted_file, "wb") as f:
        f.write(encrypted_data)
    print("Sending encrypted file...")
    client_socket.sendall(encrypted_data)
    client_socket.shutdown(socket.SHUT_WR)
    client_socket.close()
    print("File sent successfully!")
if __name__ == "__main__":
    main()