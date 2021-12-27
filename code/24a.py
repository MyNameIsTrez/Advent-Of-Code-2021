import utils


def main():
	model_number = get_maximum_model_number()
	# model_number = 13579246899999

	while "0" in str(model_number) or not is_valid_model_number(model_number):
		model_number -= 1
		if model_number % 10000 == 0:
			print(model_number)
	
	print(f"The largest model number accepted by MONAD is {model_number}")


def attempt_convert_to_int(string):
	return int(string) if string.lstrip("-").isdecimal() else string


def get_maximum_model_number():
	"""
	Submarine model numbers are always fourteen-digit numbers
	consisting only of digits 1 through 9.
	The digit 0 cannot appear in a model number.
	"""
	return int("9" * 14)


def is_valid_model_number(model_number):
	w = x = y = z = 0

	digits = get_digits_from_int(model_number)

	for digit, rule in zip(digits, RULES):
		# print(digit, rule)
		x = z
		x %= 26
		z /= rule[0]
		x += rule[1]
		x = 1 if x != digit else 0 # The ternary is not strictly necessary as True is identical to 1
		z *= 26 if x != digit else 1
		y = digit + rule[2]
		y *= x
		z += y

	return z == 0


def get_digits_from_int(integer):
	return list(map(int, str(integer)))


if __name__ == "__main__":
	RULES = (
		(1, 11, 8),
		(1, 14, 13),
		(1, 10, 2),
		(26, 0, 7),
		(1,12,11),
		(1,12,4),
		(1,12,13),
		(26,-8,13),
		(26,-9,10),
		(1,11,1),
		(26,0,2),
		(26,-5,14),
		(26,-6,6),
		(26,-12,14)
	)

	main()
