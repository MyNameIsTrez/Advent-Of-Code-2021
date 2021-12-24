import utils


def main():
	instructions = utils.parse("24_example_2", parse)

	state = {
		"w": 0,
		"x": 0,
		"y": 0,
		"z": 0,
	}

	digits = get_digits_from_int(13)

	for instruction in instructions:
		match instruction["type"]:
			case "input":
				input_variable = instruction["input_variable"]
				most_significant_digit = digits.pop(0)
				state[input_variable] = most_significant_digit
			case "operation":
				operator = instruction["operator"]
				operand_left = instruction["operand_left"]
				operand_right = instruction["operand_right"]
				operand_right_value = state[operand_right] if type(operand_right) == str else operand_right
				
				match operator:
					case "add":
						state[operand_left] += operand_right_value
					case "mul":
						state[operand_left] *= operand_right_value
					case "div":
						state[operand_left] //= operand_right_value # TODO: Might need to round up towards zero when negative
					case "mod":
						state[operand_left] %= operand_right_value
					case "eql":
						state[operand_left] = 1 if state[operand_left] == operand_right_value else 0

	print(state)


def parse(line):
	split = line.split() # Splits spaces and removes newline

	if len(split) == 2:
		return {
			"type": "input",
			"input_variable": split[1],
		}
	else:
		return {
			"type": "operation",
			"operator": split[0],
			"operand_left": attempt_convert_to_int(split[1]),
			"operand_right": attempt_convert_to_int(split[2]),
		}


def attempt_convert_to_int(string):
	return int(string) if string.lstrip("-").isdecimal() else string


def get_digits_from_int(integer):
	return list(map(int, str(integer)))


if __name__ == "__main__":
	main()
