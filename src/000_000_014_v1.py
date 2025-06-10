"""
https://projecteuler.net/problem=14

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

def get_collatz_sequence_size(n, count={1 : 1}):
	if n in count:
		return count[n]
	else:
		if n % 2 == 0:
			count[n] = get_collatz_sequence_size(n // 2, count=count) + 1
		else:
			count[n] = get_collatz_sequence_size(n * 3 + 1, count=count) + 1
		return count[n]

def f(n):
	loc, size = None, 0
	for i in range(1, n + 1):
		collatz_size = get_collatz_sequence_size(n=i)
		if collatz_size > size:
			size = collatz_size
			loc = i
	return loc, size


if __name__ == '__main__':

	test_case = get_collatz_sequence_size(
		n=13)
	if test_case != 10:
		raise ValueError("test_case was not successful")
	use_loc, use_size = f(
		n=int(1e6))
	print("\n .. The longest chain (up to {:,}) has size={:,} and starts at the number {:,}\n".format(
		int(1e6),
		use_size,
		use_loc))

##
