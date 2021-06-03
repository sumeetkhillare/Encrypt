from Crypto.Cipher import PKCS1_OAEP


class Decrypt:
    def __init__(self, msg, private_key):
        self.msg = msg
        self.private_key = private_key

    def get_message(self):
        return self.msg

    def get_private_key(self):
        return self.private_key

    def get_values(self):
        return self.msg, self.private_key

    def decrypt(self):
        cipher = PKCS1_OAEP.new(self.private_key)
        return cipher.decrypt(self.msg)
