import socket
from Crypto.Cipher import ARC4
KEY = b'topsecret@!$'  # Secret key
def rc4_decrypt(data, key):
    cipher = ARC4.new(key)
    return cipher.decrypt(data)

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("10.1.95.131", 21321))
    server_socket.listen(1)
    print("Server is waiting for a connection...")
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")
    encrypted_file = "encrypted.txt"
    decrypted_file = "decrypted.txt"
    with open(encrypted_file, "wb") as f:
        while True:
            data = conn.recv(4096)
            if not data:
                break
            f.write(data)
    conn.close()
    print("Encrypted file received!")
    with open(encrypted_file, "rb") as f:
        encrypted_data = f.read()
    decrypted_data = rc4_decrypt(encrypted_data, KEY)
    with open(decrypted_file, "wb") as f:
        f.write(decrypted_data)
    print("File decrypted and saved!")
    server_socket.close()
if __name__ == "__main__":
    main()