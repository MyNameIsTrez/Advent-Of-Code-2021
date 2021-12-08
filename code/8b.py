import utils


def parse(line):
	return list(map(lambda x : "".join(sorted(x)), line[:-1].split(" | ")[0].split(" ")))


def get_easy_mappings(line):
	segment_count_pair_mixed_segments = {
		2: None, # digit 1
		4: None, # digit 4
		3: None, # digit 7
		7: None  # digit 8
	}

	unsorted_mixed_segments = []

	for segments in line:
		l = len(segments)

		if l in segment_count_pair_mixed_segments:
			segment_count_pair_mixed_segments[l] = segments
		else:
			unsorted_mixed_segments.append(segments)

	return segment_count_pair_mixed_segments, unsorted_mixed_segments


"""
 AAAA
B    C
B    C
 DDDD
E    F
E    F
 GGGG
"""
def foo(segment_count_pair_mixed_segments):
	segment_letter_pair_potential_segment_letters = {
		'A': [],
		'B': [],
		'C': [],
		'D': [],
		'E': [],
		'F': [],
		'G': []
	}

	segment_count_pair_digit_segment_letters = {
		0: "ABCEFG",
		1: "CF",
		2: "ACDEG",
		3: "ACDFG",
		4: "BCDF",
		5: "ABDFG",
		6: "ABDEFG",
		7: "ACF",
		8: "ABCDEFG",
		9: "ABCDFG"
	}

	for segment_count, segments in segment_count_pair_mixed_segments.items():
		for digit_segment_letter in segment_count_pair_digit_segment_letters[segment_count]:
			for segment in segments:
				if segment not in segment_letter_pair_potential_segment_letters[digit_segment_letter]:
					segment_letter_pair_potential_segment_letters[digit_segment_letter].append(segment)

	for potential_segment_letters in segment_letter_pair_potential_segment_letters.values():
		potential_segment_letters.sort()

	# for potential_segment_letters in segment_letter_pair_potential_segment_letters.values():
	# 	for c in "abcdefg":
	# 		potential_segment_letters.append(c)

	print(segment_letter_pair_potential_segment_letters)


if __name__ == "__main__":
	data = utils.parse("8_example", parse)

	# print(data)

	for line in data:
		segment_count_pair_mixed_segments, unsorted_mixed_segments = get_easy_mappings(line)

		# foo(segment_count_pair_mixed_segments)

		print(segment_count_pair_mixed_segments)
		break
		# print(unsorted_mixed_segments)
