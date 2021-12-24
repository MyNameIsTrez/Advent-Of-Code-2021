import utils


def main():
	data = utils.parse("24_example", parse)

	print(data)


def parse(line):
	split = line.split() # Splits spaces and removes newline

	if len(split) == 2:
		return {
			"type": "input",
			"input": split[1],
		}
	else:
		return {
			"type": "operator",
			"operator": split[0],
			"operand_left": attempt_convert_to_int(split[1]),
			"operand_right": attempt_convert_to_int(split[2]),
		}


def attempt_convert_to_int(string):
	return int(string) if string.lstrip("-").isdecimal() else string


if __name__ == "__main__":
	main()
