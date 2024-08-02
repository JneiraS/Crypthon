import getpass
import hashlib


class SecureHasher:

    def __init__(self, password: str):
        self._password = input_user_pw()

    def __setattr__(self, key, value):
        if key == '_password':
            if not isinstance(value, str):
                raise ValueError('password doit être une chaine de caractère')
        super().__setattr__(key, value)

    def create_sha256_hash(self) -> str:
        """
        Génère un hash SHA-256 sécurisé à partir du mot de passe stocké dans l'instance et supprime le mot
        de passe original.

        Cette méthode commence par encoder le mot de passe en bytes, puis utilise l'algorithme SHA-256 pour
        produire un hash du mot de passe encodé. Après la génération du hash, le mot de passe original est
        supprimé de l'instance pour renforcer la sécurité. Le hash résultant est retourné sous forme de
        chaîne hexadécimale.

        :return: Le hash SHA-256 du mot de passe, sous forme de chaîne hexadécimale.
        """

        encoded_data = self._password.encode()
        hashed_data = hashlib.sha256(encoded_data).hexdigest()
        del self._password
        return hashed_data


def input_user_pw():
    return getpass.getpass()
