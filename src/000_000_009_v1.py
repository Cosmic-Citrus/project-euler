"""
https://projecteuler.net/problem=9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def f(n):
	candidates = []
	products = []
	## a > 0
	for i in range(1, n):
		## b > a, a + b < c
		for j in range(i, n - i):
			k = n - i - j
			if (i ** 2 + j ** 2 == k ** 2):
				candidates.append([i, j, k])
				products.append(i * j * k)
	return candidates, products

if __name__ == '__main__':

	test_candidates, test_products = f(
		n=3+4+5)
	if test_products[-1] != 3 * 4 * 5:
		raise ValueError("test_case was not successful")
	use_candidates, use_products = f(
		n=1000)
	print("\n .. abc = {:,} for the Pythagorean Triplet a={}, b={}, c={}\n".format(use_products[-1], *use_candidates[-1]))

##
