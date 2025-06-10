"""
https://projecteuler.net/problem=7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10 001st prime number?
"""

from math import log

def f(n):
	ubound = int(2 * n * log(n))
	sieve = [True] * ubound ## sieve eratosthenes
	nth_prime, count = None, 0
	for i in range(2, ubound):
		if sieve[i]:
			count += 1
			if count == n:
				nth_prime = i
				break
			## set multiples of primes to False
			## i = 7 ==> 14, 21, 28, ..., n * 7 // 7
			for j in range(2 * i, ubound, i):
				sieve[j] = False
	return nth_prime

if __name__ == '__main__':

	test_case = f(
		n=6)
	if test_case != 13:
		raise ValueError("test_case was not successful")
	use_case = f(
		n=10001)
	print("\n .. The 10,0001-st prime number is {:,}\n".format(use_case))

##
