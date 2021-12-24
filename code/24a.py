import utils


def main():
	instructions = utils.parse("24", parse)

	minimum_model_number = get_minimum_model_number()
	model_number = minimum_model_number
	# model_number = 13579246899999

	while "0" in str(model_number) or is_valid_model_number(model_number, instructions):
		model_number += 1
	
	print(f"The largest model number accepted by MONAD is {model_number - 1}")


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


def get_minimum_model_number():
	"""
	Submarine model numbers are always fourteen-digit numbers
	consisting only of digits 1 through 9.
	The digit 0 cannot appear in a model number.
	"""
	return int("1" * 14)


def is_valid_model_number(model_number, instructions):
	state = {
		"w": 0,
		"x": 0,
		"y": 0,
		"z": 0,
	}

	digits = get_digits_from_int(model_number)

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
						# state[operand_left] = math.fmod(state[operand_left], operand_right_value)
					case "eql":
						state[operand_left] = 1 if state[operand_left] == operand_right_value else 0

	return state["z"] == 0


def get_digits_from_int(integer):
	return list(map(int, str(integer)))


if __name__ == "__main__":
	main()
