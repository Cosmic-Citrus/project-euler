"""
https://projecteuler.net/problem=6

The sum of the squares of the first ten natural numbers is

	1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is

	(1 + 2 + ... + 10)^2 = 3025

Hence the difference between the sum of the squares of the 
first ten natural numbers and the square of the sum is

	3025 - 385 = 2640

Find the difference between the sum of the squares of the
first one hundred natural numbers and the square of the sum.
"""


def get_sum_of_squares(largest_natural_number):
	sum_of_squares = 0
	for number in range(1, largest_natural_number + 1):
		sum_of_squares += (number * number)
	return sum_of_squares

def get_square_of_sum(largest_natural_number):
	tally = 0
	for number in range(1, largest_natural_number + 1):
		tally += number
	square_of_sum = tally * tally
	return square_of_sum

def f(largest_natural_number):
	sum_of_squares = get_sum_of_squares(
		largest_natural_number=largest_natural_number)
	square_of_sum = get_square_of_sum(
		largest_natural_number=largest_natural_number)
	difference = square_of_sum - sum_of_squares
	return difference

if __name__ == '__main__':

	test_case = f(10)
	if test_case != 2640:
		raise ValueError("test_case was not successful")
	use_case = f(100)
	print("\n .. The difference between the sum of the squares and the square of the sum for the first 100 natural numbers is {:,}\n".format(use_case))

##