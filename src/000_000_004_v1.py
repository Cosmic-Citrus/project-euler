"""
https://projecteuler.net/problem=4

A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def f(number_digits):
	if number_digits >= 10:
		raise ValueError("modify start and stop, or use a different algorithm")
	start = int(number_digits * 10 ** (number_digits - 1))
	stop = int(eval('1e{}'.format(number_digits)))
	choices = list(range(start, stop))
	seq, size, factors = None, 0, None
	for a in choices:
		for b in choices:
			product = int(a * b)
			s = str(product)
			if s == s[::-1] and product > size:
				seq = s
				size = product
				factors = (a, b)
	return seq, size, factors

if __name__ == '__main__':

	test_seq, test_size, test_factors = f(
		number_digits=2)
	if test_factors not in [(91, 99), (99, 91)]:
		raise ValueError("test_case was not successful")
	if test_size != 9009:
		raise ValueError("test_case was not successful")

	use_seq, use_size, use_factors = f(
		number_digits=3)
	print("\n .. The largest palindrome made from the product of 3-digit numbers is {:,} = {:,} × {:,}\n".format(
			use_size,
			*use_factors))

##
