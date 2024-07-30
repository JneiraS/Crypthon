import os

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

from src.hash import SecureHasher


class Encrypt:
    def __init__(self, password, input_filename, output_filename):
        self.password: str = SecureHasher(password).create_sha256_hash()
        self.input_filename: str = input_filename
        self.output_filename: str = output_filename

    def encrypt_file(self) -> None:
        """
        Chiffre le fichier spécifié par self.input_filename et écrit le fichier chiffré dans
        self.output_filename.
        Ce processus utilise AESGCM pour le chiffrement et génère un sel et un nonce pour chaque opération
        de chiffrement afin d'assurer l'unicité des données chiffrées.
        """
        salt = os.urandom(16)
        nonce = os.urandom(12)
        key = self.generate_encryption_key(salt)
        encryption_object = AESGCM(key)

        with open(self.input_filename, 'rb') as f_in:
            data = f_in.read()

        encrypted_data = encryption_object.encrypt(nonce, data, None)

        with open(self.output_filename, 'wb') as f_out:
            f_out.write(salt)
            f_out.write(nonce)
            f_out.write(encrypted_data)

    def decrypt_file(self) -> None:
        """
        Déchiffre le fichier spécifié par self.input_filename et écrit le fichier déchiffré dans
        self.output_filename.
        Ce processus utilise AESGCM pour le déchiffrement et nécessite le sel et le nonce stockés dans le
        fichier d'origine pour reconstituer la clé de chiffrement.


        """
        with open(self.input_filename, 'rb') as f_in:
            salt = f_in.read(16)
            nonce = f_in.read(12)
            encrypted_data = f_in.read()

        key = self.generate_encryption_key(salt)

        encryption_object = AESGCM(key)

        decrypted_data = encryption_object.decrypt(nonce, encrypted_data, None)

        with open(self.output_filename, 'wb') as f_out:
            f_out.write(decrypted_data)

    def generate_encryption_key(self, salt):
        """
        Génère une clé de chiffrement à partir d'un mot de passe et d'un sel donnés en utilisant
        l'algorithme PBKDF2HMAC avec SHA256.

        :param salt: Sel (données aléatoires) utilisé pour éviter les attaques par dictionnaire sur le mot
        de passe.
        :return: Clé de chiffrement générée sous forme de bytes.
        """
        kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000,
                         backend=default_backend())
        key = kdf.derive(self.password.encode())
        return key
