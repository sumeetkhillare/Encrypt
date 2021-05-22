from Crypto import Random
from Crypto.PublicKey import RSA


class Keys:
    def __init__(self, keysize):
        self.keysize = keysize
        random_generator = Random.new().read
        key = RSA.generate(self.keysize, random_generator)
        self.private, self.public = key, key.publickey()

    def get_key_size(self):
        return self.keysize

    def get_public_key(self):
        return self.public

    def get_private_key(self):
        return self.private
