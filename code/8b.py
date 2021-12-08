import utils


def split_on_spaces_and_sort(string):
	return list(map(lambda x : "".join(sorted(x)), string.split(" ")))


def parse(line):
	input, output = line[:-1].split(" | ")
	return split_on_spaces_and_sort(input), split_on_spaces_and_sort(output)


def is_unique(mixed_segments):
	return len(mixed_segments) in (2, 3, 4, 7) # The digits 1, 7, 4, 8, in this order


def get_sorted_segments(mixed_input_segments_list):
	unique_segments_list = []
	non_unique_segments_list = []

	for mixed_segments in mixed_input_segments_list:
		if is_unique(mixed_segments):
			unique_segments_list.append(mixed_segments)
		else:
			non_unique_segments_list.append(mixed_segments)

	return unique_segments_list, non_unique_segments_list


"""
 AAAA
B    C
B    C
 DDDD
E    F
E    F
 GGGG
"""
def get_potential_segment_letters_from_unique(unique_segments_list):
	unique_segments_len_pair_digit = {
		2: 1,
		3: 7,
		4: 4,
		7: 8
	}

	digit_pair_digit_segment_letters = {
		0: "ABCEFG",
		1: "CF",      # unique
		2: "ACDEG",
		3: "ACDFG",
		4: "BCDF",    # unique
		5: "ABDFG",
		6: "ABDEFG",
		7: "ACF",     # unique
		8: "ABCDEFG", # unique
		9: "ABCDFG"
	}

	segment_letter_pair_potential_segment_letters = {
		'A': [],
		'B': [],
		'C': [],
		'D': [],
		'E': [],
		'F': [],
		'G': []
	}

	for potential_segment_letters in segment_letter_pair_potential_segment_letters.values():
		for c in "abcdefg":
			potential_segment_letters.append(c)

	for unique_segments in unique_segments_list:
		unique_segments_len = len(unique_segments)

		digit = unique_segments_len_pair_digit[unique_segments_len]

		digit_segment_letters = digit_pair_digit_segment_letters[digit]

		# TODO: Don't attempt to remove 8 as its letters are everywhere?
		for letter in "ABCDEFG":
			if letter not in digit_segment_letters:
				potential_segment_letters = segment_letter_pair_potential_segment_letters[letter]

				for potential_segment_letter in unique_segments:
					if potential_segment_letter in potential_segment_letters:
						potential_segment_letters.remove(potential_segment_letter)

		# print(unique_segments, digit, digit_segment_letters, segment_letter_pair_potential_segment_letters, "\n")

	return segment_letter_pair_potential_segment_letters


def filter_using_non_unique(potential_segment_letters, non_unique_segments_list):
	filter_069(potential_segment_letters, non_unique_segments_list)
	filter_235(potential_segment_letters, non_unique_segments_list)


"""
   0:     6:      9:
 AAAA    AAAA    AAAA
B    C  B    .  B    C
B    C  B    .  B    C
 ....    DDDD    DDDD
E    F  E    F  .    F
E    F  E    F  .    F
 GGGG    GGGG    GGGG
"""
def filter_069(potential_segment_letters, non_unique_segments_list):
	len_069 = 6
	segments_list_069 = filter_on_string_len(non_unique_segments_list, len_069)

	# print(segments_list_069)

	for c in "abcdefg":
		count = 0

		for segment_069 in segments_list_069:
			if c in segment_069:
				count += 1

		# print(count)

		if count == 3: # c is either A / B / F / G, so remove c from C, D, E
			if c in potential_segment_letters["C"]:
				potential_segment_letters["C"].remove(c)
			if c in potential_segment_letters["D"]:
				potential_segment_letters["D"].remove(c)
			if c in potential_segment_letters["E"]:
				potential_segment_letters["E"].remove(c)

		if count == 2: # c is either C / D / E, so remove c from A, B, F, G
			if c in potential_segment_letters["A"]:
				potential_segment_letters["A"].remove(c)
			if c in potential_segment_letters["B"]:
				potential_segment_letters["B"].remove(c)
			if c in potential_segment_letters["F"]:
				potential_segment_letters["F"].remove(c)
			if c in potential_segment_letters["G"]:
				potential_segment_letters["G"].remove(c)


"""
  2:      3:      5:
 AAAA    AAAA    AAAA
.    C  .    C  B    .
.    C  .    C  B    .
 DDDD    DDDD    DDDD
E    .  .    F  .    F
E    .  .    F  .    F
 GGGG    GGGG    GGGG
"""
def filter_235(potential_segment_letters, non_unique_segments_list):
	len_235 = 5
	segments_list_235 = filter_on_string_len(non_unique_segments_list, len_235)

	# print(segments_list_235)

	for c in "abcdefg":
		count = 0

		for segment_235 in segments_list_235:
			if c in segment_235:
				count += 1

		# print(count)

		if count == 3: # c is either A / D / G, so remove c from B, C, E, F
			if c in potential_segment_letters["B"]:
				potential_segment_letters["B"].remove(c)
			if c in potential_segment_letters["C"]:
				potential_segment_letters["C"].remove(c)
			if c in potential_segment_letters["E"]:
				potential_segment_letters["E"].remove(c)
			if c in potential_segment_letters["F"]:
				potential_segment_letters["F"].remove(c)

		if count == 2: # c is either C / F, so remove c from A, B, D, E, G
			if c in potential_segment_letters["A"]:
				potential_segment_letters["A"].remove(c)
			if c in potential_segment_letters["B"]:
				potential_segment_letters["B"].remove(c)
			if c in potential_segment_letters["D"]:
				potential_segment_letters["D"].remove(c)
			if c in potential_segment_letters["E"]:
				potential_segment_letters["E"].remove(c)
			if c in potential_segment_letters["G"]:
				potential_segment_letters["G"].remove(c)

		if count == 1: # c is either B / E, so remove c from A, C, D, F, G
			if c in potential_segment_letters["A"]:
				potential_segment_letters["A"].remove(c)
			if c in potential_segment_letters["C"]:
				potential_segment_letters["C"].remove(c)
			if c in potential_segment_letters["D"]:
				potential_segment_letters["D"].remove(c)
			if c in potential_segment_letters["F"]:
				potential_segment_letters["F"].remove(c)
			if c in potential_segment_letters["G"]:
				potential_segment_letters["G"].remove(c)


def filter_on_string_len(lst, length):
	return list(filter(lambda x : len(x) == length, lst))


def sort(string):
	return "".join(sorted(string))


def remap_output_digits(output_segments_list, potential_segment_letters):
	for i in range(len(output_segments_list)):
		for after, before in potential_segment_letters.items():
			output_segments_list[i] = sort(output_segments_list[i].replace(before[0], after))


def map_output_letters_to_digits(output_segments_list):
	letters_pair_digits = {
		"ABCEFG": 0,
		"CF": 1,
		"ACDEG": 2,
		"ACDFG": 3,
		"BCDF": 4,
		"ABDFG": 5,
		"ABDEFG": 6,
		"ACF": 7,
		"ABCDEFG": 8,
		"ABCDFG": 9
	}

	return [letters_pair_digits[output_segments] for output_segments in output_segments_list]


def digits_to_num(digits):
	num = 0
	for digit in digits:
		num = num * 10 + digit
	return num


def main():
	lines_input_output = utils.parse("8", parse) # TODO: Change to "8"

	total = 0

	for mixed_input_segments_list, output_segments_list in lines_input_output:
		unique_segments_list, non_unique_segments_list = get_sorted_segments(mixed_input_segments_list)

		potential_segment_letters = get_potential_segment_letters_from_unique(unique_segments_list)

		filter_using_non_unique(potential_segment_letters, non_unique_segments_list)

		# TODO: May not always work?
		potential_segment_letters["A"].remove(potential_segment_letters["G"][0])

		remap_output_digits(output_segments_list, potential_segment_letters)

		digits = map_output_letters_to_digits(output_segments_list)

		num = digits_to_num(digits)
		total += num

	print(total)


if __name__ == "__main__":
	main()
