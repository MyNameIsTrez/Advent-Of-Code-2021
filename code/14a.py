import utils

from collections import Counter


def main():
	polymer_template, pair_insertion_rules = parse("14")

	# print(polymer_template)
	# print(pair_insertion_rules)

	# print(f"Template: {polymer_template}")

	for step in range(STEPS):
		polymer_template = grow_polymer(polymer_template, pair_insertion_rules)
		# print(f"After step {step+1}: {polymer_template}")

	polymer_counter = Counter(polymer_template)
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


def grow_polymer(polymer_template, pair_insertion_rules):
	old_left_and_new = []

	for left, right in zip(polymer_template, polymer_template[1:]):
		new = pair_insertion_rules[left + right]
		old_left_and_new.append(left)
		old_left_and_new.append(new)

	# print("".join(old_left_and_new) + polymer_template[-1:])
	return "".join(old_left_and_new) + polymer_template[-1:]


if __name__ == "__main__":
	STEPS = 10

	main()
