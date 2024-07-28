import hashlib


class SecureHasher:

    def __init__(self, password: str):
        self._password = password

    def create_sha256_hash(self) -> str:
        """
        Génère un hash SHA-256 à partir du mot de passe stocké dans l'instance.
        Cette méthode encode d'abord le mot de passe en bytes, puis utilise l'algorithme SHA-256 pour
        produire un hash du mot de passe encodé. Le hash résultant est retourné sous forme de chaîne hexadécimale.

        :return: Le hash SHA-256 du mot de passe, sous forme de chaîne hexadécimale.
        """
        encoded_data = self._password.encode()  # Encode les données en bytes
        hashed_data = hashlib.sha256(encoded_data).hexdigest()  # Hache les données
        return hashed_data
