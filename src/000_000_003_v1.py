"""
https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

def f(upper_bound):
	i = 2
	while i ** 2 < upper_bound:
		while upper_bound % i == 0:
			upper_bound //= i
		i += 1
	return upper_bound

if __name__ == '__main__':

	test_case = f(
		upper_bound=13195)
	if test_case != 29:
		raise ValueError("test_case was not successful")

	use_case = f(
		upper_bound=600851475143)
	print("\n .. The largest prime factor of {:,} is {:,}\n".format(
		600851475143,
		use_case))

##
