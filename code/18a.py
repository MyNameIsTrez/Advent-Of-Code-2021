import utils

import json


def main():
	# data = utils.parse("18_example_explode_4", parse)
	data = utils.parse("18_example_addition_1", parse)

	solve(data)


def parse(line):
	return json.loads(line)


def solve(sub_data, depth=0):
	global PREV_VALUE_LIST, PREV_VALUE_INDEX, REMAINING_EXPLODED_RIGHT_VALUE

	print(sub_data)
	if depth == 4:
		return sub_data
	for i, sub_item in enumerate(sub_data):
		if type(sub_item) == list:
			exploded = solve(sub_item, depth + 1)

			if exploded:
				exploded_left, exploded_right = exploded
				print(exploded_left, exploded_right)

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

			# TODO: Don't use globals
			PREV_VALUE_LIST = sub_data
			PREV_VALUE_INDEX = i


if __name__ == "__main__":
	PREV_VALUE_LIST = None
	PREV_VALUE_INDEX = None
	REMAINING_EXPLODED_RIGHT_VALUE = None

	main()
