import utils

from collections import Counter


def main():
	polymer_template, pair_insertion_rules = parse("14_example_1")

	# print(polymer_template)
	# print(pair_insertion_rules)

	print(f"Template: {''.join(polymer_template)}")

	for step in range(STEPS):
		# for i, (left, right) in reversed(list(enumerate(zip(polymer_template, polymer_template[1:])))):
		for i in range(len(polymer_template) - 1, -1, -1):
			left = polymer_template[i - 1]
			right = polymer_template[i]
			new = pair_insertion_rules[left + right]
			polymer_template.insert(i, new)
			# print(f"i: {i}, left: {left}, right: {right}, new: {new}, New polymer: {polymer_template}")

		# print(f"After step {step+1}: {polymer_template}")

	# polymer_counter = Counter(polymer_template)
	# commonness = polymer_counter.most_common()
	# # print(commonness)
	# name_pair_most_common = commonness[0]
	# # print(name_pair_most_common)
	# name_pair_least_common = commonness[-1]
	# # print(name_pair_least_common)
	# score = name_pair_most_common[1] - name_pair_least_common[1]
	# print(score)


def parse(day):
	pair_insertion_rules = {}

	with open("../inputs/" + day + ".txt") as f:
		polymer_template = list(f.readline().rstrip())

		next(f) # Skip newline

		for ln in f:
			line = ln.rstrip()
			# print(line)
			left, right = line.split(" -> ")
			pair_insertion_rules[left] = right

	return polymer_template, pair_insertion_rules


if __name__ == "__main__":
	STEPS = 20

	main()
