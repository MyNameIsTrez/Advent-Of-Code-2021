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
			"operand_left": split[1],
			"operand_right": split[2],
		}


if __name__ == "__main__":
	main()
