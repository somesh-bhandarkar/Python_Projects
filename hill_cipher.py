import numpy as np
from pprint import pprint

def matrixinvmod26(M):
    Minv = np.linalg.inv(M)
    Mdet = np.linalg.det(M)

    Mod26invTable = {}
    for m in range(26):
        for n in range(26):
            if (m*n)%26==1:
                Mod26invTable[m] = n
           #     print(m,n)

    Mdet26 = Mdet%26
    if Mdet26 in Mod26invTable:
        Mdetinv26 = Mod26invTable[Mdet26]
    else:
        Mdetinv26 = None 
    Madj = Mdet*Minv
    Madj26 = Madj%26

    Minv26 = (Mdetinv26*Madj26)%26
    Minv26 = np.matrix.round(Minv26, 0)%26
    return Minv26

def hill_enc(M, plaintext):
    plaintext =  plaintext.replace(" ","")
    plaintext = plaintext.lower()
    while len(plaintext) % 3 != 0:
        plaintext = plaintext + "x"

    char_list = [ord(c)-97 for c in plaintext]
    cit=[]
    for i in range(0,len(char_list),3):  
            sublist = char_list[i:i+3]  
            mat_mul = np.matmul(M,sublist) % 26
            mult_res = [chr(i+97) for i in mat_mul]
            cit=cit+mult_res

    c=''.join(cit)
    return c


def hill_dec(M, ciphertext):
    ciphertext =  ciphertext.replace(" ","")
    ciphertext = ciphertext.lower()
    Minv = matrixinvmod26(M)
    Minv = Minv.astype(int)
    char_list = [ord(c)-97 for c in ciphertext]
    pla=[]
    for i in range(0,len(char_list),3):  
            sublist = char_list[i:i+3]  
            mat_mul = np.matmul(Minv,sublist) % 26
            mult_res = [chr(i+97) for i in mat_mul]
            pla=pla+mult_res
            
    p=''.join(pla)
    return p


def main():
    plaintext2 = "plaintext"
    ciphertext2 = "atakvninz"
    M = np.array([[17,17,5],[21,18,21],[2,2,19]])
    cipher = hill_enc(M,plaintext2)
    print(cipher)
    decipher = hill_dec(M,ciphertext2)
    print(decipher)

if __name__=="__main__":
    main()
