from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os
import rarfile
import subprocess

# AES Encryption helper functions
def pad(data):
    # PKCS7 padding
    pad_len = 16 - (len(data) % 16)
    return data + bytes([pad_len] * pad_len)

def unpad(data):
    pad_len = data[-1]
    return data[:-pad_len]

def encrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as f:
        data = f.read()
    data = pad(data)
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted = iv + cipher.encrypt(data)
    with open(output_file, 'wb') as f:
        f.write(encrypted)
    print(f"File encrypted and saved as {output_file}")

def decrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as f:
        encrypted = f.read()
    iv = encrypted[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(encrypted[16:])
    decrypted = unpad(decrypted)
    with open(output_file, 'wb') as f:
        f.write(decrypted)
    print(f"File decrypted and saved as {output_file}")

def compress_to_rar(input_file, rar_file):
    # Make sure WinRAR is installed and added to PATH
    # Command: rar a archive.rar file_to_compress
    command = ['rar', 'a', rar_file, input_file]
    subprocess.run(command, check=True)
    print(f"Compressed {input_file} into {rar_file}")

def extract_rar(rar_file, extract_path):
    with rarfile.RarFile(rar_file) as rf:
        rf.extractall(extract_path)
    print(f"Extracted {rar_file} to {extract_path}")

if __name__ == "__main__":
    key = get_random_bytes(16)  # AES-128 key; store this securely!
    input_file = 'example.txt'  # Replace with your file
    encrypted_file = 'example_encrypted.bin'
    rar_file = 'encrypted.rar'
    extract_path = './extracted'

    # Encrypt the file
    encrypt_file(input_file, encrypted_file, key)

    # Compress encrypted file to rar
    compress_to_rar(encrypted_file, rar_file)

    # Optional: Extract and decrypt for testing
    if not os.path.exists(extract_path):
        os.makedirs(extract_path)
    extract_rar(rar_file, extract_path)
    decrypt_file(os.path.join(extract_path, encrypted_file), 'decrypted_example.txt', key)
