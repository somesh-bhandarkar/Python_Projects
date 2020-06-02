#!/usr/bin/env python3
# Author: Somesh Bhandarkar
#
#
#
import sys

def caesar_str_enc(plaintext, K):
    ciphertext=""
    for ch in plaintext:
        encch = caesar_ch_enc(ch, K)
        ciphertext = ciphertext + encch
        
    return ciphertext

def caesar_ch_enc(ch, K):
    if ch == " ":
    	enc_char = " "
    	return enc_char
    else:
        pt = ord(ch) - 97 
        coded_pt = int((pt + K) % 26)
        enc_char = chr(coded_pt + 97)
        return enc_char
    

def caesar_str_dec(ciphertext, K):
    plaintext = ""
    for ch in ciphertext:
        decch = caesar_ch_dec(ch, K)
        plaintext = plaintext + decch
        
    return plaintext

def caesar_ch_dec(ch, K):
    if ch == " ":
        dec_char = " "
        return dec_char
    else:
        ct = ord(ch) - 97
        coded_ct = int((ct - K) % 26)
        dec_char = chr(coded_ct + 97)
        return dec_char


def test_module():
    K = int(sys.argv[1])
    input_str = sys.argv[2]
    encstr = caesar_str_enc(input_str, K)
    print(encstr)
    decstr = caesar_str_dec(encstr, K)
    print(decstr)
    
    
if __name__=="__main__":
    test_module()

