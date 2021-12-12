import utils

from collections import defaultdict
from collections import deque


def main():
	data = utils.parse("12_example_1", parse)

	# print(data)

	# TODO: Find a more Pythonic way to do this
	connections = get_connections(data)

	print(connections)

	solve(connections)


def parse(line):
	return line[:-1].split("-")


def get_connections(data):
	connections = defaultdict(list)

	for fro, to in data:
		connections[fro].append(to)
		if fro != "start" and to != "end": # Prevents retreading the start or end
			connections[to].append(fro)

	return dict(connections)


def solve(connections):
	queue = deque(["start"])

	path_count = 0

	# path = [] # TODO: Store the path per node

	visited_small_caves = []

	while len(queue) > 0:
		node = queue.pop()
		print(node)

		is_node_small_cave = is_small_cave(node)

		if is_node_small_cave:
			if node in visited_small_caves:
				# path.pop()
				if prev_node_was_small_cave:
					visited_small_caves.pop()
				continue

			visited_small_caves.append(node)

		# path.append(node)

		if node == "end":
			# print(",".join(path))
			# path.pop()
			# visited_small_caves = []

			path_count += 1

			continue

		for node_parent in connections[node]:
			queue.append(node_parent)

		prev_node_was_small_cave = is_node_small_cave

	print(path_count)


def is_small_cave(node):
	return len(node) == 1 and node.islower()


if __name__ == "__main__":
	main()
