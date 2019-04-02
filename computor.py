#!/usr/bin/env python
import argparse
import re


class X:
	def __init__(self, digit, degree):
		self.degree = degree
		self.digit = digit

	def add_value(self, digit, sign, is_revert):
		if not digit:
			digit = 0.0
		else:
			digit = float(digit)
		if sign == '-':
			digit *= -1
		if is_revert:
			digit *= -1
		self.digit += digit

	def __str__(self):
		if self.digit:
			return '{:+.10g} * X^'.format(self.digit) + str(self.degree)
		return ''


class Solver:
	def __init__(self, raw_input):
		self.a = X(0, 2)
		self.b = X(0, 1)
		self.c = X(0, 0)
		self.raw_input = raw_input
		self.max_degree = 0

	def parse(self):
		left, right = self.raw_input.split('=')
		parsed_left = re.findall(regex, left)
		parsed_right = re.findall(regex, right)
		self.__change_abc(parsed_left, False)
		self.__change_abc(parsed_right, True)
		if self.a.digit:
			self.max_degree = self.c.degree
		elif self.b.digit:
			self.max_degree = self.b.degree

	def resolve(self):
		if self.max_degree == 2:
			disc = self.b.digit ** 2 - (4 * self.a.digit * self.c.digit)
			print('dis is ' + str(disc))
			if disc == 0:
				print("Discriminant is 0, the solution is:")
				print("-b / (2 * a) = " + str(-self.b.digit / (2 * self.a.digit)))
			elif disc > 0:
				print("Discriminant is strictly positive, the two solutions are:")
				print("(-b - (d ** 0.5)) / (2 * a) = " + str((-self.b.digit - (disc ** 0.5)) / (2 * self.a.digit)))
				print("(-b + (d ** 0.5)) / (2 * a) = " + str((-self.b.digit + (disc ** 0.5)) / (2 * self.a.digit)))
			else:
				print("Discriminant is strictly negative, the two solutions are:")
				print("(-b - (d ** 0.5)) / (2 * a) = " + str((-self.b.digit - (abs(disc) ** 0.5)) / (2 * self.a.digit)))
				print("(-b + (d ** 0.5)) / (2 * a) = " + str((-self.b.digit + (abs(disc) ** 0.5)) / (2 * self.a.digit)))
		elif self.max_degree == 1:
			print("The solution is:")
			print("-c / b = " + str(-self.c.digit / self.b.digit))
		else:
			if self.c.digit == 0:
				print("Every real are solution")
			else:
				print("No solution")

	def get_reduced_form(self):
		reduced = str(self.c) + ' ' + str(self.b) + ' ' + str(self.a) + ' = 0'
		return reduced

	def __change_abc(self, parsed, is_revert):
		for i in range(0, len(parsed)):
			if not parsed[i][0] and not parsed[i][1] and not parsed[i][2] and not parsed[i][3]:
				continue
			if parsed[i][2]:
				if parsed[i][3] == '0':
					self.c.add_value(parsed[i][1], parsed[i][0], is_revert)
				elif not parsed[i][3] or parsed[i][3] == '1':
					self.b.add_value(parsed[i][1], parsed[i][0], is_revert)
				elif parsed[i][3] == '2':
					self.a.add_value(parsed[i][1], parsed[i][0], is_revert)
				pass
			elif parsed[i][1]:
				self.c.add_value(parsed[i][1], parsed[i][0], is_revert)


regex = r'([\+\-\=]?)([0-9\.]+)?(\*?X(?:\^([0-2]))?)?'


def get_max_degree(raw_input):
	max_degree = 0
	all_degree = re.findall(r'\^([0-9]+)', raw_input)
	for i in range(0, len(all_degree)):
		if int(all_degree[i]) > max_degree:
			max_degree = int(all_degree[i])
	return max_degree


def regex_type_validation(raw_input):
	raw_input = re.sub(r'\s+', '', raw_input.upper())
	validation = re.findall(regex, raw_input)
	n = 0
	for i in range(0, len(validation)):
		n = n + len(validation[i][0]) + len(validation[i][1]) + len(validation[i][2])
	max_degree = get_max_degree(raw_input)
	if max_degree > 2 or n != len(raw_input) or raw_input.count('=') != 1:
		if max_degree > 2:
			raise argparse.ArgumentTypeError('Polynomial degree: ' + str(max_degree) + '\nThe polynomial degree is stricly greater than 2, I can`t solve.')
		raise argparse.ArgumentTypeError('Polinomial equation not valid')
	return raw_input


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Computor v1 (by sromanet)', usage='%(prog)s [-h] polynomial equation, for example:\n%(prog)s "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"')
	parser.add_argument('polynomial_equation', type=regex_type_validation, help='Polynomial equation of degree less than or equal to 2 (for example 5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0)')
	args = parser.parse_args()
	solve = Solver(args.polynomial_equation)
	solve.parse()
	print('Reduced form: ' + solve.get_reduced_form())
	print('Polynomial degree: ' + str(solve.max_degree))
	print(solve.a, solve.b, solve.c)
	solve.resolve()
