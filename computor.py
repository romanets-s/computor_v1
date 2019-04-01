#!/usr/bin/env python
import sys
import re


class X:
	def __init__(self, digit, degree):  # if degree 0 is A, if 1 is B and if 2 is C
		self.degree = degree
		self.digit = digit

	def __str__(self):
		return str(self.digit) + "X^" + str(self.degree)

	def __lt__(self, x2):  # x < y
		pass

	def __le__(self, x2):  # x <= y
		pass

	def __eq__(self, x2):  # x == y
		pass

	def __ne__(self, x2):  # x != y
		pass

	def __gt__(self, x2):  # x > y
		pass

	def __ge__(self, x2):  # x >= y
		pass

	def __add__(self, x2):
		if self.degree == x2.degree:
			return X(self.digit + x2.digit, self.degree)
		else:
			return None

	def __sub__(self, x2):
		if self.degree == x2.degree:
			return X(self.digit - x2.digit, self.degree)
		else:
			return None

	def __mul__(self, x2):
		if self.degree == x2.degree:
			return X(self.digit * x2.digit, self.degree)
		else:
			return None

	def __truediv__(self, x2):
		if self.degree == x2.degree:
			return X(self.digit / x2.digit, self.degree)
		else:
			return None


regex = r'([\+\-\=]?)([0-9\.]+)?(\*?X(?:\^([0-9]+))?)?'


def parse(raw_input):
	raw_input = raw_input.replace(' ', '')
	if raw_input.count('=') != 1:
		exit(1)
	left, right = raw_input.split('=')
	parsed_left = re.findall(regex, left)
	parsed_right = re.findall(regex, right)

	print(parsed_left, parsed_right)
	for i in range(0, len(parsed_left) - 1):
		print(parsed_left[i])
	print('=====')
	for i in range(0, len(parsed_right) - 1):
		print(parsed_right[i])


if __name__ == '__main__':
	if len(sys.argv) == 2:
		input = sys.argv[1].upper()
		input = "5 + 4 * X + x^2= X^2".upper()
		parse(input)
	else:
		print('not valid input')