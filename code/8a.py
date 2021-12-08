import utils


def parse(line):
	return line[:-1].split(" | ")[1]


def count_unique(line):
	count = 0
	for segment in line.split(" "):
		# len 2 == digit 1
		# len 4 == digit 4
		# len 3 == digit 7
		# len 7 == digit 8
		if len(segment) in (2, 4, 3, 7):
			count += 1
	return count


if __name__ == "__main__":
	data = utils.parse("8", parse)

	# print(data)

	total_count = 0
	for line in data:
		count = count_unique(line)
		total_count += count
		print(line)
		print(count)
	print(total_count)
