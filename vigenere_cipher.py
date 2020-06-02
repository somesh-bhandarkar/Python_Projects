#!/usr/bin/env python3
# Author: Somesh Bhandarkar


# Vigenere encryption function
def vigenere_enc(keyword, plaintext):
    plaintext =  plaintext.replace(" ","")
    plaintext = plaintext.lower()
    key_length = len(keyword)
    integer_key = [ord(k)-97 for k in keyword]
#    print(integer_key)
    integer_plaintext = [ord(p)-97 for p in plaintext]
    c = ''
    for i in range(0, len(integer_plaintext)):
        key_value = integer_key[i % key_length]
#        print(key_value)
        integer_ciphertext = (integer_plaintext[i] + key_value) % 26
        c = c + chr(integer_ciphertext + 97)    
    return c


# Vionegere decryption function
def vigenere_dec(keyword, ciphertext):
    ciphertext =  ciphertext.replace(" ","")
    ciphertext = ciphertext.lower()
    key_length = len(keyword)
    integer_key = [ord(k)-97 for k in keyword]
    integer_ciphertext = [ord(c)-97 for c in ciphertext]
    p = ''
    for i in range(len(integer_ciphertext)):
        key_value = integer_key[i % key_length]
        integer_plaintext = (integer_ciphertext[i] - key_value+26) % 26
        p = p + chr(integer_plaintext + 97)
    return p


def main():
    keyword = "cipher"
    plaintext = "a z a z a z a z a z"
    ciphertext = "chpgeqchpg"
    enc = vigenere_enc(keyword, plaintext)
    print(enc)
    dec = vigenere_dec(keyword, ciphertext)
    print(dec)

if __name__=="__main__":
    main()
