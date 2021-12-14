import utils

from collections import Counter


def main():
	polymer_template, pair_insertion_rules = parse("14")

	# print(polymer_template)
	# print(pair_insertion_rules)

	# print(f"Template: {polymer_template}")

	length = len(polymer_template)

	final_length = get_final_length(length)
	# print(f"Final length: {final_length}")

	characters = [None] * final_length
	enter_polymer_template(characters, polymer_template)

	# print(characters)

	for step in range(STEPS):
		new_length = length * 2 - 1

		for i in range(length - 1, 0, -1):
			# print(f"step: {step}, i: {i}, new_i: {i * 2}")
			characters[i * 2] = characters[i]
			characters[i * 2 - 1] = pair_insertion_rules[characters[i - 1] + characters[i]]
			# print(characters)

		length = new_length
			# left = characters[i - 1]
			# right = characters[i]

			# for left, right in zip(characters, characters[1:]):
			# 	new = pair_insertion_rules[left + right]
			# 	old_left_and_new.append(left)
			# 	old_left_and_new.append(new)

			# print("".join(old_left_and_new) + polymer_template[-1:])

		print(f"Step: {step + 1}")

	polymer_counter = Counter(characters)
	commonness = polymer_counter.most_common()
	# print(commonness)
	name_pair_most_common = commonness[0]
	# print(name_pair_most_common)
	name_pair_least_common = commonness[-1]
	# print(name_pair_least_common)
	score = name_pair_most_common[1] - name_pair_least_common[1]
	print(score)


def parse(day):
	pair_insertion_rules = {}

	with open("../inputs/" + day + ".txt") as f:
		polymer_template = f.readline().rstrip()

		next(f) # Skips a newline

		for ln in f:
			line = ln.rstrip()
			# print(line)
			left, right = line.split(" -> ")
			pair_insertion_rules[left] = right

	return polymer_template, pair_insertion_rules


def get_final_length(length):
	for step in range(STEPS):
		length = length * 2 - 1
	return length


def enter_polymer_template(characters, polymer_template):
	for i, character in enumerate(polymer_template):
		characters[i] = character


if __name__ == "__main__":
	STEPS = 40

	main()
