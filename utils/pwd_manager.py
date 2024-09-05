import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv

class PasswordManager:
    def __init__(self, key_file="secret.key"):
        self.key_file = key_file
        self.key = self.load_key()

    def generate_key(self):
        """Generate a key and save it to a file."""
        key = Fernet.generate_key()
        with open(self.key_file, "wb") as key_file:
            key_file.write(key)
        self.key = key

    def load_key(self):
        """Load the previously generated key."""
        try:
            return open(self.key_file, "rb").read()
        except FileNotFoundError:
            self.generate_key()
            return self.key

    def encrypt_password(self, password):
        """Encrypt the password."""
        encoded_password = password.encode()
        f = Fernet(self.key)
        encrypted_password = f.encrypt(encoded_password)
        return encrypted_password

    def decrypt_password(self, encrypted_password):
        """Decrypt the password."""
        f = Fernet(self.key)
        decrypted_password = f.decrypt(encrypted_password)
        return decrypted_password.decode()