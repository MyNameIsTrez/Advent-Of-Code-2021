import utils, copy

from collections import defaultdict, deque


def main():
	data = utils.parse("12", parse)

	# print(data)

	# TODO: Find a more Pythonic way to do this
	connections = get_connections(data)

	# print(connections)

	solve(connections)


def parse(line):
	return line[:-1].split("-")


def get_connections(data):
	connections = defaultdict(list)

	# The conditions prevent retreading the start or the end
	for fro, to in data:
		if fro != "end" and to != "start":
			connections[fro].append(to)
		if to != "end" and fro != "start":
			connections[to].append(fro)

	return dict(connections)


def solve(connections):
	path_count = 0

	stack = deque([ ["start", [], ["start"], None] ])

	while len(stack) > 0:
		popped = stack.pop()

		node = popped[0]
		prev_small_cave_visited_twice = popped[3]

		for node_parent in connections[node]:
			visited_small_caves, path = copy.copy(popped[1]), copy.copy(popped[2])

			small_cave_visited_twice = prev_small_cave_visited_twice

			if node_parent in visited_small_caves:
				if prev_small_cave_visited_twice != None:
					continue
				small_cave_visited_twice = node_parent

			path.append(node_parent)

			if node_parent == "end":
				# print(",".join(path))
				path.pop()
				path_count += 1
				continue

			if is_small_cave(node_parent):
				visited_small_caves.append(node_parent)

			stack.append([node_parent, copy.copy(visited_small_caves), copy.copy(path), small_cave_visited_twice])

			small_cave_visited_twice = prev_small_cave_visited_twice

	print(path_count)


def is_small_cave(node):
	return node.islower() and node not in ("start", "end")


if __name__ == "__main__":
	main()
