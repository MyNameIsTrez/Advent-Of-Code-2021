import utils


def get_diff_side(diff, side):
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


if __name__ == "__main__":
	data = utils.parse_line_csv("7")

	data.sort() # TODO: It should be possible to get rid of this by letting get_diff_side() use abs()

	diff = [l2_el - l1_el for l1_el, l2_el in zip(data, data[1:])]


	diff_left = get_diff_side(diff, "left")
	# print(diff_left)
	diff_right = get_diff_side(diff, "right")
	# print(diff_right)


	scores = [l + r for l, r in zip(diff_left, diff_right)]
	print(min(scores))
