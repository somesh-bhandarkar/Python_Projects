#! /usr/bin/env python
#
# Author: Somesh Bhandarkar
# UID: 116715843
# This program is written as a project for the course ENPM697
##
# The program uses z3 SMT solver https://github.com/Z3Prover/z3
#
# This program finds the prime factors for very large numbers
# I have written two approaches to solve this particular problem, this is the first approach
# In this approach I find all the factors of the large number and then pass it to the 
# SMT solver to check whether that factor is prime
from z3 import *

from functools import reduce

def isPrime(number):
	int1 = Int('int1')
	int2 = Int('int2')
	out = Int('out')
	s = Solver()
	cond1 = (out==number)
	cond2 = And(int1>1, int2>1, int1 * int2 == number)
	s.add(cond1)
	s.add(cond2)

	if s.check() == unsat:
		return 'prime'




def factors(number):
	fac = []
	for n in range (2, int(number**0.5)+1):

		if number % n == 0:
			factor1 = n
			factor2 = int(number/n)

			fac.extend([factor1,factor2])

	return list(set(fac))




def main():
	final_list = []
	number = raw_input("Enter a large number to find prime factors:")
	factor_list = factors(int(number))
	print("\n")
	print ("[+] Finding Prime Factors for the number {}".format(number))

	for fac in factor_list:
		ans = isPrime(fac)
		if ans == 'prime':
			final_list.append(fac)

	print("\n")
	print "The Prime Factors are:", final_list
	#print final_list


if __name__ == '__main__':
	main()