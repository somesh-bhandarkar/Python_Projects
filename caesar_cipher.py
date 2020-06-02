#!/usr/bin/env python3
# Course: ENPM694 - Network Security
# Author: Somesh Bhandarkar
#
#
#


print("[+] This program will convert Plain Text to Encoded Text using Ceasar Cipher")

def input_message():
    print("Enter the Plain Text to be Encoded")
    plain_text = input('> ')
    return plain_text

def input_key():
    print("Enter the Key by which the Plain Text should be shifted")
    print("Key Range:(1-26)")
    key = int(input('> '))
    if key > 25:
        print("The key should be in the range 1 to 25")
    else:
        return key

def encode_message(plain_text, K):
    encoded_message = ""
    for char in plain_text:
          p = ord(char) - 97
          encoded_p = int((p + K) % 26)
          encoded_char = chr(encoded_p + 97)
          encoded_message = encoded_message + encoded_char


          if char == " ":
                encoded_message = encoded_message + " "

          
    return encoded_message

if __name__ == "__main__":
	plain_text = input_message()
	key = input_key()

	encrypted_message = encode_message(plain_text, key)
	print("The encrypted message is", encrypted_message) 


