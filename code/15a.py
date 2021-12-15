import utils

from collections import deque
import numpy as np


def main():
	data = utils.parse("15_example", parse)

	# print(np.array(data))

	world = get_world_from_data(data)
	# print(world)

	end_node = get_end_node(data)
	# print(end_node)

	solve(world, end_node)


def parse(line):
	return list(map(int, line.rstrip()))


def get_world_from_data(data):
	world = { (x, y): risk_level for y, row in enumerate(data) for x, risk_level in enumerate(row) }
	return world


def get_end_node(data):
	x = len(data[0]) - 1
	y = len(data) - 1

	return ( x, y )


def solve(world, end_node):
	start_node = ( 0, 0 )
	stack = deque([ start_node ])

	while len(stack) > 0:
		node = stack.pop()

		if node[0] == end_node[0] and node[1] == end_node[1]:
			break

		neighbors = ( (node[0], node[1]-1), (node[0], node[1]+1), (node[0]-1, node[1]), (node[0]+1, node[1]) ) # up, down, left, right

		for neighbor in neighbors:
			if neighbor in world:
				stack.append(neighbor)


if __name__ == "__main__":
	main()
