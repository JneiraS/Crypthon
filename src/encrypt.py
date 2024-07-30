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

    def encrypt_file(self):
        # Générer une clé de chiffrement à partir du mot de passe
        salt = os.urandom(16)

        key = self.generate_encryption_key(salt)

        # Choisir un nonce pour AES-GCM
        nonce = os.urandom(12)

        # Créer l'objet de chiffrement
        aesgcm = AESGCM(key)

        # Ouvrir le fichier en mode binaire et lire son contenu
        with open(self.input_filename, 'rb') as f_in:
            data = f_in.read()

        # Chiffrer les données
        encrypted_data = aesgcm.encrypt(nonce, data, None)

        # Écrire le sel, le nonce et les données chiffrées dans le fichier de sortie
        with open(self.output_filename, 'wb') as f_out:
            f_out.write(salt)
            f_out.write(nonce)
            f_out.write(encrypted_data)

    def decrypt_file(self):
        # Ouvre le fichier chiffré et lire le sel, le nonce et les données chiffrées
        with open(self.input_filename, 'rb') as f_in:
            salt = f_in.read(16)
            nonce = f_in.read(12)
            encrypted_data = f_in.read()

        # Reconstituer la clé de chiffrement à partir du mot de passe et du sel
        key = self.generate_encryption_key(salt)

        # Créer l'objet de déchiffrement
        aesgcm = AESGCM(key)

        # Décrypter les données
        decrypted_data = aesgcm.decrypt(nonce, encrypted_data, None)

        # Écrire les données déchiffrées dans le fichier de sortie
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
