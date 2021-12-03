import utils


def remove_newline(str):
	return str.rstrip("\n")


def count_bits(i, byte_strings, fn):
	zeros = 0
	ones = 0

	for byte_string in byte_strings:
		if byte_string[i] == "0":
			zeros += 1
		else:
			ones += 1

	return fn(zeros, ones)


def remove_bit_strings_with_bit(lst, remove_bit, bit_index):
	for string_index, string in reversed(list(enumerate(lst))):
		if int(string[bit_index]) == remove_bit:
			del lst[string_index]


def least_common_bit_fn(zeros, ones):
	if zeros < ones:
		return 0
	elif ones < zeros:
		return 1
	else:
		return "equal"


def most_common_bit_fn(zeros, ones):
	if zeros > ones:
		return 0
	elif ones > zeros:
		return 1
	else:
		return "equal"


if __name__ == "__main__":
	data = utils.parse("3", remove_newline)

	bit_string_len = 12


	oxygen_data = data.copy()

	for i in range(bit_string_len):
		least_common_bit = count_bits(i, oxygen_data, least_common_bit_fn)
		remove_bit_strings_with_bit(oxygen_data, least_common_bit if least_common_bit != "equal" else 0, i)
		if len(oxygen_data) == 1:
			oxygen_generator_rating = int(oxygen_data[0], 2)

	print(oxygen_generator_rating)


	co2_data = data.copy()

	for i in range(bit_string_len):
		least_common_bit = count_bits(i, co2_data, most_common_bit_fn)
		remove_bit_strings_with_bit(co2_data, least_common_bit if least_common_bit != "equal" else 1, i)
		if len(co2_data) == 1:
			co2_scrubber_rating = int(co2_data[0], 2)

	print(co2_scrubber_rating)


	print(oxygen_generator_rating * co2_scrubber_rating)


# 4017424, 4259420