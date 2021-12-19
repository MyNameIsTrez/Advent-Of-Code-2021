import utils

import json, math


def main():
	with open("../inputs/18.txt") as f:
		lines = f.readlines()
		lines = [ json.loads(line) for line in lines]

	first_line_data = lines[0]
	data = first_line_data
	print(f"First line         : {first_line_data}")

	for line in lines[1:]:
		line_data = line
		print(f"Adding line        : {line_data}")

		data = [ data, line_data ]

		print(f"Data after adding  : {data}")

		explode_and_split(data)

	magnitude = get_magnitude(data)
	print(f"Magnitude: {magnitude}")


def explode_and_split(data):
	global PREV_VALUE_LIST, PREV_VALUE_INDEX, REMAINING_EXPLODED_RIGHT_VALUE, EXPLODED_ONE, SPLITTED_ONE

	while True:
		# TODO: Don't use globals
		PREV_VALUE_LIST = None
		PREV_VALUE_INDEX = None

		REMAINING_EXPLODED_RIGHT_VALUE = None


		EXPLODED_ONE = False
		explode_all(data)

		if not EXPLODED_ONE:
			SPLITTED_ONE = False
			split_one(data)

			if not SPLITTED_ONE:
				break
			else:
				print(f"After splitting one: {data}")
		else:
			print(f"After exploding all: {data}")


def explode_all(sub_data, depth=0):
	global PREV_VALUE_LIST, PREV_VALUE_INDEX, REMAINING_EXPLODED_RIGHT_VALUE, EXPLODED_ONE

	for i, sub_item in enumerate(sub_data):
		if type(sub_item) == list:
			if depth + 1 == 4:
				if REMAINING_EXPLODED_RIGHT_VALUE:
					sub_item[0] += REMAINING_EXPLODED_RIGHT_VALUE

					REMAINING_EXPLODED_RIGHT_VALUE = None

				EXPLODED_ONE = True
				exploded_left, exploded_right = sub_item

				# TODO: What if there's already something in the globals?
				if PREV_VALUE_LIST:
					PREV_VALUE_LIST[PREV_VALUE_INDEX] += exploded_left

					PREV_VALUE_LIST = None
					PREV_VALUE_INDEX = None

				REMAINING_EXPLODED_RIGHT_VALUE = exploded_right

				sub_data[i] = 0

				PREV_VALUE_LIST = sub_data
				PREV_VALUE_INDEX = i
			else:
				exploded = explode_all(sub_item, depth + 1)
		else:
			if REMAINING_EXPLODED_RIGHT_VALUE:
				sub_data[i] += REMAINING_EXPLODED_RIGHT_VALUE

				REMAINING_EXPLODED_RIGHT_VALUE = None

			PREV_VALUE_LIST = sub_data
			PREV_VALUE_INDEX = i


def split_one(sub_data, depth=0):
	global SPLITTED_ONE

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


def get_magnitude(sub_data):
	combined_sub_magnitudes = 0

	for i, sub_item in enumerate(sub_data):
		if type(sub_item) == list:
			sub_magnitude = get_magnitude(sub_item)
			if i == 0: # Left
				combined_sub_magnitudes += 3 * sub_magnitude
			elif i == 1: # Right
				combined_sub_magnitudes += 2 * sub_magnitude
		elif i == 0: # Left
			combined_sub_magnitudes += 3 * sub_item
		elif i == 1: # Right
			combined_sub_magnitudes += 2 * sub_item

	return combined_sub_magnitudes


if __name__ == "__main__":
	main()
