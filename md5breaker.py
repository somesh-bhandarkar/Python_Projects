#!/usr/bin/env python3
# coding #utf-8
# Author: Somesh Bhandarkar
# This python program is a project for course ENPM693
# 
#
#
import hashlib, sys



def errorhandling(hash_input, wordlist_input):
	if len(hash_input) != 32:
		print("\n")
		print("Error Caught: {} is not a valid MD5 hash".format(hash_input))
		sys.exit()

	try:
		worddoc = open(wordlist_input, 'r')
		worddoc.close()
	except IOError:
		print("\n")
		print("Error Caught: {} is not a valid filename".format(wordlist_input))
		sys.exit()

	return




def load_wordlist(filename):
    print("Loading word list from file...")
    wordlist = []
    with open(filename) as file:
        for line in file:
            wordlist.append(line.rstrip())
    print (" ", len(wordlist), "words loaded in Wordlist.")
    file.close()
    print("\n")
    return wordlist




def matcher(hash_input, dictionary):

    for words in dictionary:
    	print("[+] Trying \"{}\" as a possible value".format(words))
    	new_hash = hashlib.md5(str(words).encode('utf-8'))
    	if new_hash.hexdigest() == hash_input:
    		print("\n")
    		print("[+] Hash Successfully Cracked")
    		print("[+] HASH {}: VALUE {}".format(hash_input, words))
    		cracked = 'yes'
    		break
    	else:
    		cracked = 'no'
    return cracked 



    
def main():
    hash_input = input("Enter an MD5 hash to be decoded:")
    wordlist_input = input("Enter the Dictionary you would like to use:")
    errorhandling(hash_input, wordlist_input)
    wordlist = load_wordlist(wordlist_input)
    cracked = matcher(hash_input, wordlist)
    if cracked == 'no':
    	print("\n")
    	print("[x][x] This hash is not crackable using {} [x][x]".format(wordlist_input))

        

if __name__ == '__main__':
    main()

