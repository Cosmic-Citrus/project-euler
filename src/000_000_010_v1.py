"""
https://projecteuler.net/problem=10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

def f(n):
	## approach borrowed from # 7
	sieve = [True] * n ## sieve eratosthenes
	prime_numbers = set()
	for i in range(2, n):
		if sieve[i]:
			prime_numbers.add(i)
			for j in range(2 * i, n, i):
				sieve[j] = False
	return sum(prime_numbers)

if __name__ == '__main__':

	test_case = f(
		n=10)
	if test_case != 2 + 3 + 5 + 7:
		raise ValueError("test_case was not successful")
	use_case = f(
		n=int(2e6))
	print("\n .. The sum of all prime numbers less than {:,} is {:,}\n".format(int(2e6), use_case))

##
