"""
https://projecteuler.net/problem=5

2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""

def get_gcd(a, b):
	a, b = abs(a), abs(b)
	if a > b:
		a, b = b, a
	while b:
		a, b = b, a % b
	return a

def get_lcm(a, b):
	return a * b / get_gcd(a, b)

def f(ubound):
	res = 1
	for i in range(1, ubound + 1):
		res = get_lcm(res, i)
	return res

if __name__ == '__main__':

	test_case = f(10)
	if test_case != 2520:
		raise ValueError("test_case was not successful")
	use_case = f(20)
	print("\n .. The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is {:,}\n".format(use_case))

##
