import utils

from collections import Counter


def main():
	polymer_template, pair_insertion_rules = parse("14")

	pair_counts = get_initial_pair_counts(polymer_template, pair_insertion_rules)

	unique_characters = set(char for pair_name in pair_insertion_rules for char in pair_name)

	for _ in range(STEPS):
		new_pair_counts = pair_counts.copy()

		for pair_name, pair_count in pair_counts.items():
			new_char = pair_insertion_rules[pair_name]
			new_pair_counts[pair_name[0] + new_char] += pair_count
			new_pair_counts[new_char + pair_name[1]] += pair_count
			new_pair_counts[pair_name] -= pair_count

		pair_counts = new_pair_counts

	chars_left = { char: 0 for char in unique_characters }
	chars_right = { char: 0 for char in unique_characters }

	for pair_name, pair_count in pair_counts.items():
		chars_left[pair_name[0]] += pair_count
		chars_right[pair_name[1]] += pair_count

	combined_char_counts = {}

	for char in unique_characters:
		combined_char_counts[char] = max(chars_left[char], chars_right[char])

	polymer_counter = Counter(combined_char_counts)
	commonness = polymer_counter.most_common()

	name_pair_most_common = commonness[0]
	name_pair_least_common = commonness[-1]

	score = name_pair_most_common[1] - name_pair_least_common[1]
	print(score)


def parse(day):
	pair_insertion_rules = {}

	with open("../inputs/" + day + ".txt") as f:
		polymer_template = f.readline().rstrip()

		next(f) # Skips a newline

		for ln in f:
			line = ln.rstrip()
			left, right = line.split(" -> ")
			pair_insertion_rules[left] = right

	return polymer_template, pair_insertion_rules


def get_initial_pair_counts(polymer_template, pair_insertion_rules):
	pair_counts = { k: 0 for k in pair_insertion_rules.keys() }

	for left, right in zip(polymer_template, polymer_template[1:]):
		new = pair_insertion_rules[left + right]
		pair_counts[left + right] += 1

	return pair_counts


if __name__ == "__main__":
	STEPS = 40

	main()
