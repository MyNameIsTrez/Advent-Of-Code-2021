import utils


def parse(line):
	return list(map(lambda x : "".join(sorted(x)), line[:-1].split(" | ")[0].split(" ")))


def get_easy_mappings(line):
	mappings = {
		2: None, # digit 1
		4: None, # digit 4
		3: None, # digit 7
		7: None  # digit 8
	}

	unsorted = []

	for segments in line:
		l = len(segments)

		if l in mappings:
			mappings[l] = segments
		else:
			unsorted.append(segments)

	return mappings, unsorted


"""
 AAAA
B    C
B    C
 DDDD
E    F
E    F
 GGGG
"""
def foo(mappings):
	bar = {
		'A': [],
		'B': [],
		'C': [],
		'D': [],
		'E': [],
		'F': [],
		'G': []
	}

	segment_letters = {
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

	for segment_count, segments in mappings.items():
		for segment_letter in segment_letters[segment_count]:
			for segment in segments:
				if segment not in bar[segment_letter]:
					bar[segment_letter].append(segment)

	for v in bar.values():
		v.sort()

	# for v in bar.values():
	# 	for c in "abcdefg":
	# 		v.append(c)

	print(bar)


if __name__ == "__main__":
	data = utils.parse("8_example", parse)

	# print(data)

	for line in data:
		mappings, unsorted = get_easy_mappings(line)

		foo(mappings)

		print(mappings)
		break
		# print(unsorted)
