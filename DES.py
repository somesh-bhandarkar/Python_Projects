#!/usr/bin/env python3
# coding: utf-8
# Final Program
# Name: Somesh Bhandarkar



BookInitPermOrder = [58,50,42,34,26,18,10,2,
                   60,52,44,36,28,20,12,4,
                   62,54,46,38,30,22,14,6,
                   64,56,48,40,32,24,16,8,
                   57,49,41,33,25,17,9,1,
                   59,51,43,35,27,19,11,3,
                   61,53,45,37,29,21,13,5,
                   63,55,47,39,31,23,15,7]


BookInvInitPermOrder = [40,8,48,16,56,24,64,32,
                        39,7,47,15,55,23,63,31,
                        38,6,46,14,54,22,62,30,
                        37,5,45,13,53,21,61,29,
                        36,4,44,12,52,20,60,28,
                        35,3,43,11,51,19,59,27,
                        34,2,42,10,50,18,58,26,
                        33,1,41,9,49,17,57,25]


PC1 = [57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,52,44,36,63,55,47,39,31,23,15,
       7,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,28,20,12,4]
PC2 = [14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,26,8,16,7,27,20,13,2, 41,52,31,37,47,55,30,40,51,45,33,48,
       44,49,39,56,34,53,46,42,50,36,29,32]

E_TABLE = [32,1,2,3,4,5,4,5,6,7,8,9,8,9,10,11,12,13,12,13,14,15,16,17,
16,17,18,19,20,21,20,21,22,23,24,25,24,25,26,27,28,29,28,29,30,31,32,1]

P = [16,7,20,21,29,12,28,17,1,15,23,26,5,18,31,10,2,8,24,14,32,27,3,9,19,13,30,6,22,11,4,25]


def byteseq2binstr(byteseq):
    bitslist2 = [bin(int(b))[2:].zfill(8) for b in byteseq]
    allbitsstr = ''.join(bitslist2)
    
    return allbitsstr

def after_PC1(input_key_64bit, PC1):
    key_56bit = []
    key_56bit += [input_key_64bit[index-1] for index in PC1]
    key_56bit = ''.join(key_56bit)
    return key_56bit

#key_56 = after_PC1(demo_key, PC1)

def two_halves(key_56bit):
    left_half, right_half = key_56bit[:28], key_56bit[28:]
    return left_half, right_half


def des_keygen(C_inp, D_inp, roundindex):
    # Implement Figure 6
    C_shifted = C_inp[roundindex:] + C_inp[:roundindex]
    D_shifted = D_inp[roundindex:] + D_inp[:roundindex]
    key_48bit = []
    key_56bit_local = C_shifted + D_shifted
    key_48bit += [key_56bit_local[index-1] for index in PC2]
    key48 = ''.join(key_48bit)
    C_out = C_shifted
    D_out = D_shifted
    #print(list(key48))
    return key48, C_out, D_out



def des_key_generation(input_key_64bit):
    subkey = []
    permuted_choice_1 = after_PC1(input_key_64bit, PC1)
    C_inp, D_inp = two_halves(permuted_choice_1)
    left_shift_index = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    
    for round in range(0,16):
        round_key, C_out, D_out = des_keygen(C_inp, D_inp, left_shift_index[round])
        C_inp = C_out
        D_inp = D_out
        subkey.append(round_key) 
    return subkey
    


def Permutation(bitstr, permorderlist):
    permedbitstr = None
    InitPermOrder = [x-1 for x in permorderlist]
    inputbitslistperm = [bitstr[b] for b in InitPermOrder]
    permedbitstr = ''.join(inputbitslistperm)
    return permedbitstr


def Expansion(inputbitstr32, e_table):
    outputbitstr48 = []
    outputbitstr48 = [inputbitstr32[index-1] for index in e_table]
    outputbitstr48 = ''.join(outputbitstr48)
    return outputbitstr48

#bits32 = "11110000101010101111000010101010"
#out_bits48 = Expansion(bits32, E_TABLE)
#print (out_bits48)


def permutation_function(sbox_value, P):
    outputbitstr32 = []
    outputbitstr32 = [sbox_value[index-1] for index in P]
    outputbitstr32 = ''.join(outputbitstr32)
    return outputbitstr32

def XORbits(bitstr1,bitstr2):
    xor_result = ""
    outstr = ""
    for index in range(len(bitstr1)):
        if bitstr1[index] == bitstr2[index]:
            xor_result += "0"
        else:
            xor_result += "1"
    #print("XOR:", xor_result)
    #xor_result = outstr
    return xor_result
#bits1 = '1100'
#bits2 = '1010'
#print (XORbits(bits1,bits2))


SBOX = [
# Box-1
[
[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
[0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
[4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
[15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]
],
# Box-2

[
[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
[3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
[0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
[13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]
],

# Box-3

[
[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
[13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
[13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
[1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]
],

# Box-4
[
[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
[13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
[10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
[3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]
],

# Box-5
[
[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
[14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
[4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
[11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]
],
# Box-6

[
[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
[10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
[9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
[4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]

],
# Box-7
[
[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
[13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
[1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
[6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]
],
# Box-8

[
[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
[1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
[7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
[2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]
]

]

# Let's define a table for quick conversion of sbox decimals to 4 bit binary
DECtoBIN4 = {0: '0000',
            1: '0001',
            2: '0010',
            3: '0011',
            4: '0100',
            5: '0101',
            6: '0110',
            7: '0111',
            8: '1000',
            9: '1001',
            10: '1010',
            11: '1011',
            12: '1100',
            13: '1101',
            14: '1110',
            15: '1111'}

#print(DECtoBIN4[12])

def pre_sbox_lookup(xor_result):
    blocklist=[xor_result[i:i+6] for i in range(0,len(xor_result),6)]
    return blocklist

def sbox_lookup(input6bitstr, sboxindex):
    row = int(input6bitstr[0] + input6bitstr[-1],base=2)
    col = int(input6bitstr[1:5],base=2)
    sbox_value = SBOX[int(sboxindex)][row][col]
    return DECtoBIN4[sbox_value]


def des_round(LE_inp32, RE_inp32, key48):
    LE_out32 = RE_inp32
    RE_tmp = functionF(RE_inp32,key48)
    RE_out32 = XORbits(LE_inp32, RE_tmp)
    
    
    return LE_out32, RE_out32


def functionF(bitstr32, keybitstr48):
    outbitstr32 = ''
    result_sbox_lookup = ''
    after_sbox_lookup = []
    result_outbitstr32 = []
    sbox_bits = ''
    expanded_right_48bit = Expansion(bitstr32, E_TABLE)
    xor_result = XORbits(expanded_right_48bit, keybitstr48)
    xor_result_6bits = pre_sbox_lookup(xor_result)
    for i,j in zip(range(0,len(xor_result),6),range(0,8)):
        sbox_bits = sbox_bits + sbox_lookup(xor_result[i:i+6],j)
    result_outbitstr32 = permutation_function(sbox_bits, P)
    outbitstr32 = ''.join(result_outbitstr32)

    return outbitstr32


def des_enc(inputblock, num_rounds, inputkey64): 
    key_64bit = byteseq2binstr(inputkey64)
    keylist = des_key_generation(key_64bit)
    input_64bit = byteseq2binstr(inputblock)
    inputblock = Permutation(input_64bit,BookInitPermOrder)
    LE_init = inputblock[:32]
    RE_init = inputblock[32:]    
    for i in range(0,num_rounds):
        LE_init, RE_init = des_round(LE_init, RE_init,keylist[i])
    cipherRevblock = RE_init + LE_init
    cipher_block = Permutation(cipherRevblock, BookInvInitPermOrder)
    cipherblock = bytes([int(cipher_block[i:i+8],base =2) for i in range(0,len(cipher_block),8)])
    return cipherblock


def des_enc_test(input_fname, inputkey64, num_rounds, output_fname):
    finp = open(input_fname, 'rb')
    inpbyteseq = finp.read()
    finp.close()
    cipherblocks=[]
    inpbyteseq=inpbyteseq+(b'\x20'*(8-(len(inpbyteseq)%8))) if len(inpbyteseq)%8 !=0 else inpbyteseq
    blocklist=[inpbyteseq[i:i+8] for i in range(0,len(inpbyteseq),8)]
    cipherblocks = [des_enc(i,num_rounds,inputkey64) for i in blocklist]
    cipherbyteseq = b''.join(cipherblocks)
    fout = open(output_fname, 'wb')
    fout.write(cipherbyteseq)
    fout.close()

    
def des_dec(inputblock, num_rounds, inputkey64):  
    key_64bit = byteseq2binstr(inputkey64)
    keylist = des_key_generation(key_64bit)
    input_64bit = byteseq2binstr(inputblock)
    inputblock = Permutation(input_64bit,BookInitPermOrder)
    LE_init = inputblock[:32]
    RE_init = inputblock[32:]    
    for i in range(0,num_rounds):
        LE_init, RE_init = des_round(LE_init, RE_init,keylist[15 - i])
    plainRevblock = RE_init + LE_init
    plain_block = Permutation(plainRevblock, BookInvInitPermOrder)
    
    plainblock = bytes([int(plain_block[i:i+8],base =2) for i in range(0,len(plain_block),8)])
    return plainblock
    
def des_dec_test(input_fname, inputkey64, num_rounds, output_fname):
    finp = open(input_fname, 'rb')
    cipherbyteseq = finp.read()
    finp.close()
    blocklist=[cipherbyteseq[i:i+8] for i in range(0,len(cipherbyteseq),8)]
    plainblocks = []
    plainblocks = [des_dec(i,num_rounds,inputkey64) for i in blocklist]
    plainbyteseq = b''.join(plainblocks)
    fout = open(output_fname, 'wb')
    fout.write(plainbyteseq)
    fout.close()


    
#def main():
    
#    inputblock = b'\x02\x46\x8a\xce\xec\xa8\x64\x20'
#    key = b'\x0f\x15\x71\xc9\x47\xd9\xe8\x59'
#    cipherblock = '\xda\x02\xce\x3a\x89\xec\xac\x3b'
#    cipherblock = des_enc(inputblock, 16, key)
#    print(cipherblock)


if __name__ == "__main__":
    main()

def main(): 
    Plaintext =b'\x02\x46\x8a\xce\xec\xa8\x64\x20'
    Key = b'\x0f\x15\x71\xc9\x47\xd9\xe8\x59'#0f1571c947d9e859
    Ciphertext = des_enc(Plaintext, 16, Key)
    print(Ciphertext.hex())
    Message = des_dec(Ciphertext, 16, Key)
    print(Message.hex())
#inp="test.txt"
#inputkey64= b'\x0f\x15\x71\xc9\x47\xd9\xe8\x59'
#output="output_des.txt"
#des_enc_test(inp,inputkey64,16,output)
#inp="output_des.txt"
#output="sample1_des.txt"
#des_dec_test(inp,inputkey64,16,output)
