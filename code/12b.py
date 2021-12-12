import utils

from collections import defaultdict
import copy


def main():
	data = utils.parse("12", parse)

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

	# The conditions prevent retreading the start or the end
	for fro, to in data:
		if fro != "end" and to != "start":
			connections[fro].append(to)
		if to != "end" and fro != "start":
			connections[to].append(fro)

	return dict(connections)


def solve(connections, node="start", visited_small_caves=[], path=["start"], prev_small_cave_visited_twice=None):
	global PATH_COUNT

	for node_parent in connections[node]:
		small_cave_visited_twice = prev_small_cave_visited_twice

		if node_parent in visited_small_caves:
			if prev_small_cave_visited_twice != None:
				continue
			small_cave_visited_twice = node_parent

		path.append(node_parent)

		if node_parent == "end":
			print(",".join(path))
			path.pop()
			PATH_COUNT += 1
			continue

		if is_small_cave(node_parent):
			visited_small_caves.append(node_parent)

		solve(connections, node_parent, visited_small_caves, path, small_cave_visited_twice)

		small_cave_visited_twice = prev_small_cave_visited_twice

		if is_small_cave(node_parent):
			visited_small_caves.pop()

		path.pop()


def is_small_cave(node):
	return node.islower() and node not in ("start", "end")


if __name__ == "__main__":
	PATH_COUNT = 0

	main()
