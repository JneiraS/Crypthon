## Crypthon - A File Encryption Tool

Crypthon is a Python project designed to offer a straightforward yet secure solution for file encryption and decryption. Leveraging AES-GCM for encryption and combining SHA-256 with PBKDF2HMAC for secure password management, Crypthon aims to protect sensitive data from unauthorized access.
Features

    - File encryption and decryption using AES-GCM.
    - Secure generation of encryption keys from a user-provided password.
    - Command line interface for easy use.

## Installation

Crypthon requires Python 3.6 or higher. Dependencies can be installed using pip:

```pip install -r requirements.txt```

Ensure all dependencies listed in requirements.txt are installed.
## Usage

Crypthon provides a simple command line interface. Here's how you can encrypt or decrypt a file:
```
python cryothon.py -m <enc|dec> -p <your_password> -i <path_to_input_file> -o <path_to_output_file>
```

Replace <encrypt|decrypt> with the desired action (encrypt for encryption, decrypt for decryption), <your_password> with your secure password, and the paths to the input and output files according to your needs.
Contributing

Contributions are welcome! If you wish to contribute to Crypthon, please follow these steps:

    Fork the repository on GitHub.
    Create a new branch for your contribution.
    Make your changes and ensure the code is clean and well-documented.
    Open a pull request with a detailed description of your changes.

License

Crypthon is distributed under the MIT license. See LICENSE for more information.

This README provides a solid foundation for your Crypthon project. You can extend or modify it according to the specific needs of your project, such as adding sections on unit testing, technical documentation, or any other significant feature.