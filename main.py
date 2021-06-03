from core.encryption import encrypt as enc
from core.decryption import decrypt as dec
from user.keys import keys as keys

def print_output(obj_keys,encrypted_message,decrypted_message):
    print("\nPrivate Key:\n"+str(obj_keys.get_private_key())+"\n")
    print("Public Key:\n"+str(obj_keys.get_public_key())+"\n")
    print("Encrypted Message:\n"+str(encrypted_message)+"\n")
    print("Decrypted Message:\n"+decrypted_message.decode()+"\n")


def main():
    obj_keys = keys.Keys(1024)
    print("Enter Message:")
    message = input()
    obj_enc = enc.Encrypt(message.encode(), obj_keys.get_public_key())
    encrypted_msg = obj_enc.encrypt()
    obj_dec = dec.Decrypt(encrypted_msg, obj_keys.get_private_key())
    decrypted_msg = obj_dec.decrypt()
    print_output(obj_keys,encrypted_msg,decrypted_msg)


if __name__ == "__main__":
    main()
