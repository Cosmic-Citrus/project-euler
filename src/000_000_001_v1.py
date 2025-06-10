"""
https://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def f(n, div_a=3, div_b=5):
	res = []
	for i in range(1, n):
		if (i % div_a == 0) or (i % div_b == 0):
			res.append(i)
	return sum(res)

if __name__ == '__main__':

	test_case = f(
		n=10)
	if test_case != 23:
		raise ValueError("test_case was not successful")

	use_case = f(
		n=1000)
	print("\n .. The sum of all multiples less than 1000 is {:,}\n".format(use_case))
##
