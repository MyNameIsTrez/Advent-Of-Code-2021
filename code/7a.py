import utils


def get_side_costs(diff, side):
	diff_side = [0]

	for i in range(len(diff)):
		diff_index = i if side == "left" else (-i - 1)
		cur_diff = diff[diff_index]
		added = cur_diff * (i + 1)
		# print(f"i: {i}, cur_diff: {cur_diff}, added: {added}")

		prev_diff = diff_side[i]
		# print(f"prev_diff: {prev_diff}, prev_diff + added: {prev_diff + added}")

		diff_side.append(prev_diff + added)

	if side == "right":
		diff_side.reverse()

	return diff_side


def solution1(data):
	data.sort() # TODO: It should be possible to get rid of this by letting get_side_costs() use abs()

	diff = [l2_el - l1_el for l1_el, l2_el in zip(data[:-1], data[1:])]


	left_costs = get_side_costs(diff, "left")
	# print(left_costs)
	right_costs = get_side_costs(diff, "right")
	# print(right_costs)


	scores = [l + r for l, r in zip(left_costs, right_costs)]
	print(min(scores))


# This uses the fact that for [1, 2, 10, 100] it costs an equal amount of fuel to go to 2/3/4.../9/10
# [4, 5, 10, 100, 0, 0, 0, 0, 0]
def solution2(data):
	data.sort()

	alignment_avg = data[int((len(data))/2)] # If there are 4 numbers this returns the 3rd number at index 2
	# print(alignment_avg)

	fuel = 0
	for hor in data:
		fuel += abs(alignment_avg - hor)
	print(fuel)


if __name__ == "__main__":
	data = utils.parse_line_csv("7")

	# solution1(data.copy())
	solution2(data.copy())
