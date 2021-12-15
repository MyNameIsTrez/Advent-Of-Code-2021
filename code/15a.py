import utils, cursor

import time, heapq

import numpy as np


def main():
	data = utils.parse("15", parse)



	data[0][0] = 0

	world = get_world_from_data(data)
	# print(world)

	end_node = get_end_node(data)
	# print(end_node)

	# replace_risk_levels_with_black_squares(data)

	# print(stringify_data(data))

	solve(data, world, end_node)


def replace_risk_levels_with_black_squares(data):
	for i, row in enumerate(data):
		# row = len(row) * "⬛"
		for i in range(len(row)):
			row[i] = "⬛"


def parse(line):
	return list(map(int, line.rstrip()))


def stringify_data(data):
	stringified_data = ""

	for row in data:
		for c in row:
			stringified_data += str(c)
		# print(row)
		# stringified_data += "".join(row)
		stringified_data += "\n"

	return stringified_data


def get_world_from_data(data):
	world = { (x, y): risk_level for y, row in enumerate(data) for x, risk_level in enumerate(row) }
	return world


def get_end_node(data):
	x = len(data[0]) - 1
	y = len(data) - 1

	return ( x, y )


def solve(data, world, end_node):
	start_node = ( 0, 0 )

	hq = []
	heapq.heappush(hq, (0, start_node))

	visited = [ start_node ]

	while len(hq) > 0:
		node_risk_level, node = heapq.heappop(hq)

		# node_x = node[0]
		# node_y = node[1]
		# data[node_y][node_x] = "⬜"

		# time.sleep(0.0001)

		# cursor.replace_bottom(stringify_data(data))

		if node[0] == end_node[0] and node[1] == end_node[1]:
			print(node_risk_level)
			break

		neighbors = ( (node[0], node[1]-1), (node[0], node[1]+1), (node[0]-1, node[1]), (node[0]+1, node[1]) ) # up, down, left, right

		for neighbor in neighbors:
			if neighbor in world and neighbor not in visited:
				# print(neighbor)
				score = get_score(neighbor, end_node, node_risk_level, world)
				heapq.heappush(hq, (score, neighbor))
				visited.append(neighbor)


def get_score(neighbor, end_node, node_risk_level, world):
	neighbor_risk_level = node_risk_level + world[neighbor]

	taxicab_cost_to_end = get_taxicab_cost_to_end(neighbor, end_node)

	return neighbor_risk_level + taxicab_cost_to_end


def get_taxicab_cost_to_end(neighbor, end_node):
	x_diff = abs(end_node[0] - neighbor[0])
	y_diff = abs(end_node[1] - neighbor[1])

	return (x_diff + y_diff) * 0


if __name__ == "__main__":
	main()
