"""
https://projecteuler.net/problem=19

You are given the following information, but you may prefer to do some
research for yourself.

	1 Jan 1900 was a Monday.
	Thirty days has September,
	April, June and November.
	All the rest have thirty-one,
	Saving February alone,
	Which has twenty-eight, rain or shine.
	And on leap years, twenty-nine.
	A leap year occurs on any year evenly divisible by 4, but not on a
	century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?
"""

import datetime

def f(year_start, year_end):
	day = 1
	count = 0
	for year in range(year_start, year_end + 1):
		for month in range(1, 13):
			dt = datetime.date(year, month, day)
			if dt.weekday() == 6:
				count += 1
	return count


if __name__ == '__main__':

	# test_case = ...
	# if test_case != ...:
	#     raise ValueError("test_case was not successful")
	use_case = f(
		year_start=1901,
		year_end=2000)
	print("\n .. There are {:,} Sundays on the first of the month between 01/01/1901 - 12/31/2000 \n".format(use_case))

##
