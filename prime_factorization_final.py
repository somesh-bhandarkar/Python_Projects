
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
# In this approach, I take the large number as an input and give it to the SMT solver
# the SMT solver finds factors for the particular number. 
#

from z3 import *


prime_fac = set([])

def factor(number):
	global prime_fac
	int1 = Int('int1')
	int2 = Int('int2')
	out = Int('out')
	s = Solver()
	cond1 = (out==number)
	cond2 = And(int1>1, int2>1, int1 * int2 == number)
	s.add(cond1)
	s.add(cond2)

	if s.check() == unsat:
		prime_fac.add(number)
	elif s.check() == sat:
		result = s.model()
		factor(result[int1])
		factor(result[int2])

	
def main():

	number = raw_input("Enter a large number to find prime factors:")
	print "\n"
	print "[+] Finding Prime Factors for {}".format(number)

	factor(int(number))

	print "\n"
	print "The Prime Factors are:", list(prime_fac)


if __name__ == '__main__':
	main()
