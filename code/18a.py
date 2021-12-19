import utils

import json, math


def main():
	global EXPLODED_ONE, SPLITTED_ONE

	# data = utils.parse("18_example_explode_4", parse)
	data = utils.parse("18_example_addition_1", parse)

	while True:
		print(data)

		EXPLODED_ONE = False
		# print(EXPLODED_ONE)
		explode_all(data)
		# print(EXPLODED_ONE)

		if not EXPLODED_ONE:
			SPLITTED_ONE = False
			# print(SPLITTED_ONE)
			split_one(data)
			# print(SPLITTED_ONE)

			if not SPLITTED_ONE:
				break


def parse(line):
	return json.loads(line)


def explode_all(sub_data, depth=0):
	global PREV_VALUE_LIST, PREV_VALUE_INDEX, REMAINING_EXPLODED_RIGHT_VALUE, EXPLODED_ONE

	# print(sub_data)
	if depth == 4:
		return sub_data
	for i, sub_item in enumerate(sub_data):
		if type(sub_item) == list:
			exploded = explode_all(sub_item, depth + 1)

			if exploded:
				EXPLODED_ONE = True
				exploded_left, exploded_right = exploded
				# print(exploded_left, exploded_right)

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

	# print(sub_data)
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
