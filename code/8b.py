import utils


def parse(line):
	return line.strip().split(" | ")[1]


def get_easy_mappings(data):
	unique_mappings = {
		2: 1,
		3: 7,
		4: 4,
		7: 8
	}

	mappings = [None] * 10 # So digit strings can be inserted in any order
	unsorted = []

	total_count = 0
	for line in data:
		for segment in line.split(" "):
			l = len(segment)

			# Note that adding a check for mappings[l] == None wouldn't work, as it'd fill up the list "unsorted" with known segments.
			if l in unique_mappings:
				mappings[unique_mappings[l]] = segment
			else:
				unsorted.append(segment)

	return mappings, unsorted


if __name__ == "__main__":
	data = utils.parse("8_example", parse)

	# print(data)

	mappings, unsorted = get_easy_mappings(data)

	print(mappings)
	print(unsorted)
