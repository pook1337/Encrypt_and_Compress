
# Encrypt_and_Compress

A simple Python tool to **encrypt files using AES encryption** and then **compress the encrypted files into a .rar archive**. This project combines cryptography and compression to securely store or share sensitive data.

---

## Features

- AES-128 encryption with CBC mode and PKCS7 padding  
- Compress encrypted files into `.rar` archives using WinRAR  
- Decrypt and extract files from `.rar` archives  
- Command-line interface for easy usage (if implemented)  

---

## Requirements

- Python 3.6+  
- [pycryptodome](https://pycryptodome.readthedocs.io/en/latest/) - for AES encryption  
- [rarfile](https://rarfile.readthedocs.io/en/latest/) - for handling `.rar` archives  
- WinRAR installed and added to your system PATH (required for creating `.rar` archives)  

---

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/pook1337/Encrypt_and_Compress.git
   cd Encrypt_and_Compress
   ```

2. Install Python dependencies:

   ```
   pip install pycryptodome rarfile
   ```

3. Make sure WinRAR is installed and the `rar` command is available in your system PATH.

---

## Usage

### Encrypt a file and compress it to `.rar`:

```
python ec.py
```

*(Modify `ec.py` to specify your input file, or extend the script to accept command-line arguments.)*

### Example workflow:

1. Encrypt a file (e.g., `example.txt`) → produces `example_encrypted.bin`  
2. Compress `example_encrypted.bin` into `encrypted.rar`  
3. Extract and decrypt the file from `encrypted.rar`  

---

## How it works

- **Encryption:** The script uses AES encryption in CBC mode with a random initialization vector (IV). The data is padded to fit AES block size.  
- **Compression:** The encrypted file is compressed into a `.rar` archive using the WinRAR command-line tool.  
- **Decryption:** The encrypted file is extracted from the `.rar` archive and decrypted back to the original content.

---

## Notes

- Keep your AES encryption key secure! Losing the key means you cannot decrypt your data.  
- This tool requires WinRAR for compression; if you prefer `.zip` compression, consider modifying the script to use Python's built-in `zipfile` module.  
- The script currently uses a randomly generated key each run - for practical use, you should implement key management.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/pook1337/Encrypt_and_Compress/issues).

