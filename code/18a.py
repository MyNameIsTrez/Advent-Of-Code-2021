import utils

import json, math


def main():
	global EXPLODED_ONE, SPLITTED_ONE

	data = parse()

	print(f"After adding all lines: {data}")

	while True:
		EXPLODED_ONE = False
		explode_all(data)

		if not EXPLODED_ONE:
			SPLITTED_ONE = False
			split_one(data)

			if not SPLITTED_ONE:
				break
			else:
				print(f"After splitting one   : {data}")
		else:
			print(f"After exploding all   : {data}")


def parse():
	with open("../inputs/18_example_addition_1.txt") as f:
		first_line = f.readline()
		data = json.loads(first_line)

		for line in f:
			line_data = json.loads(line)
			data = [ data, line_data ]

		return data


def explode_all(sub_data, depth=0):
	global PREV_VALUE_LIST, PREV_VALUE_INDEX, REMAINING_EXPLODED_RIGHT_VALUE, EXPLODED_ONE

	if depth == 4:
		return sub_data
	for i, sub_item in enumerate(sub_data):
		if type(sub_item) == list:
			exploded = explode_all(sub_item, depth + 1)

			if exploded:
				EXPLODED_ONE = True
				exploded_left, exploded_right = exploded

				# TODO: What if there's already something in the globals?
				if PREV_VALUE_LIST:
					PREV_VALUE_LIST[PREV_VALUE_INDEX] += exploded_left

					PREV_VALUE_LIST = None
					PREV_VALUE_INDEX = None

				REMAINING_EXPLODED_RIGHT_VALUE = exploded_right

				sub_data[i] = 0
		else:
			if REMAINING_EXPLODED_RIGHT_VALUE:
				sub_data[i] += REMAINING_EXPLODED_RIGHT_VALUE

				REMAINING_EXPLODED_RIGHT_VALUE = None

			PREV_VALUE_LIST = sub_data
			PREV_VALUE_INDEX = i


def split_one(sub_data, depth=0):
	global PREV_VALUE_LIST, PREV_VALUE_INDEX, REMAINING_EXPLODED_RIGHT_VALUE, SPLITTED_ONE

	for i, sub_item in enumerate(sub_data):
		if type(sub_item) == list:
			splitted = split_one(sub_item, depth + 1)
			if splitted:
				return True
		elif sub_item >= 10:
			SPLITTED_ONE = True

			split_divided_by_two = sub_item / 2
			split_left = math.floor(split_divided_by_two)
			split_right = math.ceil(split_divided_by_two)

			sub_data[i] = [ split_left, split_right ]

			return True


if __name__ == "__main__":
	# TODO: Don't use globals
	PREV_VALUE_LIST = None
	PREV_VALUE_INDEX = None

	REMAINING_EXPLODED_RIGHT_VALUE = None

	EXPLODED_ONE = False
	SPLITTED_ONE = False

	main()
