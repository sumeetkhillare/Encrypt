from Crypto.Cipher import PKCS1_OAEP


class Encrypt:
    def __init__(self, message, public_key):
        self.message = message
        self.public_key = public_key

    def encrypt(self):
        cipher = PKCS1_OAEP.new(self.public_key)
        return cipher.encrypt(self.message)

    def get_message(self):
        return self.message

    def get_publickey(self):
        return self.public_key

