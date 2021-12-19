import utils

import json, math


def main():
	lines = get_lines()

	data = lines[0]

	for line in lines[1:]:
		data = [ data, line ]

		explode_and_split(data)

	magnitude = get_magnitude(data)

	print(f"Magnitude: {magnitude}")


def get_lines():
	with open("../inputs/18.txt") as f:
		lines = f.readlines()
		lines = [ json.loads(line) for line in lines]
	return lines


def explode_and_split(data):
	global PREV_VALUE_LIST, PREV_VALUE_INDEX, REMAINING_EXPLODED_RIGHT_VALUE, EXPLODED_ONE

	while True:
		# TODO: Don't use globals
		PREV_VALUE_LIST = None
		PREV_VALUE_INDEX = None

		REMAINING_EXPLODED_RIGHT_VALUE = None


		EXPLODED_ONE = False
		explode_all(data)

		if not EXPLODED_ONE:
			splitted_one = split_one(data)

			if not splitted_one:
				break


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
	for i, sub_item in enumerate(sub_data):
		if type(sub_item) == list:
			splitted = split_one(sub_item, depth + 1)
			if splitted:
				return True
		elif sub_item >= 10:
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
			combined_sub_magnitudes += get_scaled_sub_magnitude(sub_magnitude, i)
		else:
			combined_sub_magnitudes += get_scaled_sub_magnitude(sub_item, i)

	return combined_sub_magnitudes


def get_scaled_sub_magnitude(sub_magnitude, i):
	if i == 0: # Left
		return 3 * sub_magnitude
	elif i == 1: # Right
		return 2 * sub_magnitude


if __name__ == "__main__":
	main()
