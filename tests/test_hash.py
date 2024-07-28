import hashlib
import unittest

from src.hash import *


class TestHash(unittest.TestCase):

    def setUp(self):
        self.hash_factory: SecureHasher = SecureHasher('my_password')

    def test_hash_class(self):
        self.assertIsInstance(self.hash_factory, SecureHasher)

    def test_generator(self):
        hash_test: str = self.hash_factory.create_sha256_hash()
        self.assertEqual(hash_test, 'f6e248ea994f3e342f61141b8b8e3ede86d4de53257abc8d06ae07a1da73fb39')


if __name__ == '__main__':
    unittest.main()

