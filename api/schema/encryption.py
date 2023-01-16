import rsa
import os.path
from os import path
class Encryption:

    def encrypt(plaintext):
        n = 10
        ciphertext = ""

        for i in range(len(plaintext)):
            ch = plaintext[i]
            
            if ch==" ":
                ciphertext+=" "
            elif (ch.isupper()):
                ciphertext += chr((ord(ch) + n-65) % 26 + 65)
            
            else:
                ciphertext += chr((ord(ch) + n-97) % 26 + 97)
        
        return ciphertext

    def decrypt(ciphertext):
     
        letters="abcdefghijklmnopqrstuvwxyz"
        
        k = 10
        plaintext = ""

        for ch in ciphertext:

            if ch in letters:
                position = letters.find(ch)
                new_pos = (position - k) % 26
                new_char = letters[new_pos]
                plaintext += new_char
            else:
                plaintext += ch
        
        return plaintext

