"""Trying out Python cryptography."""

import sys
import os
import hashlib
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes


def main() -> None:
    print("BEGINNING... ")
    print(sys.argv)

    encrypt(sys.argv[1], b"starwars")
    
def encrypt(filename: str, password: str) -> None:
    print("ENCRYPTING... ")
    fileText = ""
    with open(filename, "rb") as f:
         fileText = f.read()

    print("Encyrpting file: ", fileText)

    salt = get_random_bytes(32)
    print("Using salt: ", salt)
    key = hashlib.scrypt(password, salt=salt, n=2**4, r=8, p=1, dklen=32)
    print("KEY: ", key)
    cipher = AES.new(key, AES.MODE_GCM)
    print("CIPHER: ", cipher)
    cipherText, tag = cipher.encrypt_and_digest(fileText)
    print("CIPHERTEXT: ", cipherText, "  \nTAG: ", tag)

    with open("encrypted_" + filename, "wb") as ef:
        ef.write(cipher.nonce)
        ef.write(tag)
        ef.write(cipherText)

if __name__ == "__main__":
    main()

