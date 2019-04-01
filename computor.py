#!/usr/bin/env python
import sys

class X:
	def __init__(self, digit, degree): #if degree 0 is A, if 1 is B and if 2 is C
		self.degree = degree
		self.digit = digit
	def __str__(self):
		return str(self.digit) + "X^" + str(self.degree)
	def __lt__(self, x2): #x < y
		pass
	def __le__(self, x2): #x <= y
		pass
	def __eq__(self, x2): #x == y
		pass
	def __ne__(self, x2): #x != y 
		pass
	def __gt__(self, x2): #x > y 
		pass
	def __ge__(self, x2): #x >= y 
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

regex = ''

def parse(input):
	input = input.replace(' ', '').replace('+-', '-').replace('-+', '-').replace('--', '+').replace('++', '+')
	print(input)

if __name__ == '__main__':
	if len(sys.argv) == 2:
		input = sys.argv[1]
		input = "5 + 4 * X + X^2= X^2"
		x1 = X(3, 2)
		x2 = X(5, 2)
		x3 = X(2, 3)
		print(x1, x2, x3)
		print(x1 + x3)
		print(x1 + x2)
		print(x1 - x2)
		print(x1 * x2)
		print(x1 / x2)
		parse(input)
	else:
		print('not valid input')