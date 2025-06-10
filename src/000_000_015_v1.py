"""
https://projecteuler.net/problem=15

Starting in the top left corner of a 2×2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

from math import factorial

def f(m, n):
	## m + n choose n; see picture
	return factorial(m + n) // (factorial(m) * factorial(n))


if __name__ == '__main__':

	test_case = f(
		m=2,
		n=2)
	if test_case != 6:
		raise ValueError("test_case was not successful")
	use_case = f(
		m=20,
		n=20)
	print("\n .. The 20x20 grid has {:,} possible routes\n".format(use_case))

##
