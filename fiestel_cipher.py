import random
import hmac
import hashlib

def xor(byteseq1, byteseq2):
    l1 = [b for b in byteseq1]
    l2 = [b for b in byteseq2]
    l1xorl2 = [bytes([elem1^elem2]) for elem1,elem2 in zip(l1,l2)]
    result = b''.join(l1xorl2)
    return result

def feistel_block(LE_inp, RE_inp, k):
    LE_out = RE_inp
    RE_xor = F(RE_inp,k)
    RE_out = xor(LE_inp,RE_xor)
    return LE_out, RE_out

def F(byteseq, k):
    h = hmac.new(bytes(k), byteseq, hashlib.sha1)
    return h.digest()[:8]

def gen_keylist(keylenbytes, numkeys, seed):
    keylist = []
    random.seed(seed)
    keylist = [random.randint(0,255) for i in range(numkeys)]
    return keylist

def feistel_enc(inputblock, num_rounds, seed):
    keylist = gen_keylist(8, num_rounds, seed)
    left_inputblock = inputblock[0:4]
    right_inputblock = inputblock[4:8]
    for i in range(0,16):
        left_inputblock, right_inputblock = feistel_block(left_inputblock, right_inputblock, keylist[i])


    cipherblock = right_inputblock + left_inputblock
    return cipherblock

def feistel_enc_test(input_fname, seed, num_rounds, output_fname):
    finp = open(input_fname, 'rb')
    inpbyteseq = finp.read()
    finp.close()
    inpbyteseq=inpbyteseq+(b'\x20'*(8-(len(inpbyteseq)%8))) if len(inpbyteseq)%8 !=0 else inpbyteseq

    blocklist=[inpbyteseq[i:i+8] for i in range(0,len(inpbyteseq),8)]
    cipherblock = [feistel_enc(inputblock,num_rounds,seed) for inputblock in blocklist]

    cipherbyteseq = b''.join(cipherblock)
    fout = open(output_fname, 'wb')
    fout.write(cipherbyteseq)
    fout.close()

def feistel_dec(inputblock, num_rounds, seed):
    keylist = gen_keylist(8, num_rounds, seed)
    left_inputblock = inputblock[0:4]
    right_inputblock = inputblock[4:8]
    for i in range(0,16):
        left_inputblock, right_inputblock = feistel_block(left_inputblock, right_inputblock, keylist[15-i])

    plainblock = right_inputblock + left_inputblock

    return plainblock

def feistel_dec_test(input_fname, seed, num_rounds, output_fname):
    finp = open(input_fname, 'rb')
    inpbyteseq = finp.read()
    finp.close()
    inpbyteseq=inpbyteseq+(b'\x20'*(8-(len(inpbyteseq)%8))) if len(inpbyteseq)%8 !=0 else inpbyteseq

    blocklist=[inpbyteseq[i:i+8] for i in range(0,len(inpbyteseq),8)]
    plainblock = [feistel_dec(inputblock,num_rounds,seed) for inputblock in blocklist]
    plainbyteseq = b''.join(plainblock)
    fout = open(output_fname, 'wb')
    fout.write(plainbyteseq)
    fout.close()

def main():
    feistel_enc_test("test.txt", 8, 16, "test_enc.txt")
    feistel_dec_test("test_enc.txt",8,16, "test_dec.txt")

if __name__ == "__main__":
    main()
