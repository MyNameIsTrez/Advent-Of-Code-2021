import utils, copy

from collections import defaultdict
from collections import deque


def main():
	data = utils.parse("12_example_2", parse)

	# print(data)

	# TODO: Find a more Pythonic way to do this
	connections = get_connections(data)

	# print(connections)

	solve(connections)

	print(PATH_COUNT)


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
	global PATH_COUNT

	stack = deque([ ["start", [], []] ])

	# print(node)

	while len(stack) > 0:
		node, visited_small_caves, path = stack.pop()

		if is_small_cave(node):
			if node in visited_small_caves:
				continue

			visited_small_caves.append(node)

		path.append(node)

		if node == "end":
			print(",".join(path))
			PATH_COUNT += 1
			continue

		for node_parent in connections[node]:
			stack.append([node_parent, copy.copy(visited_small_caves), copy.copy(path)])


def is_small_cave(node):
	return len(node) == 1 and node.islower()


if __name__ == "__main__":
	PATH_COUNT = 0

	main()
