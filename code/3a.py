import utils


def remove_newline(str):
	return str.rstrip("\n")


def get_most_common_bit(i):
	zeros = 0
	ones = 0

	for byte_string in data:
		if byte_string[i] == "0":
			zeros += 1
		else:
			ones += 1

	return 0 if zeros > ones else 1


if __name__ == "__main__":
	data = utils.parse("3", remove_newline)

	bit_string_len = 12

	gamma = 0
	for i in range(bit_string_len):
		gamma = (gamma << 1) | get_most_common_bit(i) # Push a bit on the right

	mask = 2 ** bit_string_len - 1 # For a bit_string_len of 5 this'd be 0b11111
	epsilon = gamma ^ mask # Invert bits

	print(gamma * epsilon)
