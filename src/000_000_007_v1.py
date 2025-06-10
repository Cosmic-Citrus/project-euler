"""
https://projecteuler.net/problem=7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10 001st prime number?
"""

from math import log

def f(n):
	prime_numbers = [2]
	count = 1
	i = 3
	while count < n:
		if any(i % prime == 0 for prime in prime_numbers):
			prime_numbers.append(prime)
			count += 1
		i += 2 ## skip even numbers
	return prime_numbers[-1]

if __name__ == '__main__':

	test_case = f(
		n=6)
	if test_case != 13:
		raise ValueError("test_case was not successful")
	use_case = f(
		n=10001)
	print("\n .. The 10,0001-st prime number is {:,}\n".format(use_case))

##
