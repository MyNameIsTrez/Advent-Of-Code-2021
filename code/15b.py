import utils, cursor

import time, heapq

import numpy as np
import threading
import math


def main():
	data_small = utils.parse("15_example", parse)

	data = get_data_large(data_small)

	data[0][0] = 0

	world = get_world_from_data(data)
	# print(world)

	end_node = get_end_node(data)
	# print(end_node)

	replace_risk_levels_with_black_squares(data)

	print(stringify_data(data))

	solve(data, world, end_node)


def replace_risk_levels_with_black_squares(data):
	for i, row in enumerate(data):
		# row = len(row) * "██"
		for i in range(len(row)):
			row[i] = "██"


def parse(line):
	return list(map(int, line.rstrip()))


def get_data_large(data_small):
	data = [None] * len(data_small) * SCALE
	for i in range(len(data_small) * SCALE):
		data[i] = [None] * len(data_small[0]) * SCALE

	for i in range(len(data_small)):
		for j in range(len(data_small[0])):
			data[i][j] = data_small[i][j]

	# print(np.array2string(np.array(data)))

	for i in range(len(data_small) * (SCALE - 1)):
		for j in range(len(data_small[0])):
			data[i + len(data_small)][j] = (data[i][j] % 9) + 1
	for i in range(len(data_small) * SCALE):
		for j in range(len(data_small[0]) * (SCALE - 1)):
			data[i][j + len(data_small[0])] = (data[i][j] % 9) + 1

	# print(np.array2string(np.array(data)))

	return data


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
	world = { (SCALE, y): risk_level for y, row in enumerate(data) for SCALE, risk_level in enumerate(row) }
	return world


def get_end_node(data):
	SCALE = len(data[0]) - 1
	y = len(data) - 1

	return ( SCALE, y )


stop_loop = False


def solve(data, world, end_node):
	global stop_loop
	start_node = ( 0, 0 )

	hq = []
	heapq.heappush(hq, (0, start_node))

	visited = set([0])

	printit(data)
	i = 0
	while len(hq) > 0:
		node_risk_level, node = heapq.heappop(hq)

		node_x = node[0]
		node_y = node[1]
		data[node_y][node_x] = "  "

		time.sleep(SLEEP_TIME)

		# if node[0] == end_node[0] and node[1] == end_node[1]:
		# 	for line in data:
		# 		for i in range(len(line)):
		# 			line[i] = "  "
		# 	stop_loop = True
		# 	print(node_risk_level)
		# 	break

		neighbors = ( (node[0], node[1]-1), (node[0], node[1]+1), (node[0]-1, node[1]), (node[0]+1, node[1]) ) # up, down, left, right

		for neighbor in neighbors:
			neighbor_index = neighbor[0] + neighbor[1] * len(data[0])
			if neighbor in world and neighbor_index not in visited:
				# print(neighbor)
				score = get_score(neighbor, end_node, node_risk_level, world)
				heapq.heappush(hq, (score, neighbor))
				visited.add(neighbor_index)
		i += 1
	stop_loop = True


def get_score(neighbor, end_node, node_risk_level, world):
	neighbor_risk_level = node_risk_level + world[neighbor]

	taxicab_cost_to_end = get_taxicab_cost_to_end(neighbor, end_node)
	dist_to_end = get_dist_to_end(neighbor, end_node)

	return neighbor_risk_level * NEIGHBOR_FACTOR + taxicab_cost_to_end * TAXI_FACTOR + dist_to_end * DIST_FACTOR


def get_taxicab_cost_to_end(neighbor, end_node):
	x_diff = abs(end_node[0] - neighbor[0])
	y_diff = abs(end_node[1] - neighbor[1])

	return (x_diff + y_diff)


def get_dist_to_end(neighbor, end_node):
	x_diff = abs(end_node[0] - neighbor[0])
	y_diff = abs(end_node[1] - neighbor[1])

	return math.sqrt(x_diff * x_diff + y_diff * y_diff)


def printit(data):
	if not stop_loop:
		threading.Timer(0.020, printit, [data]).start()
	cursor.replace_bottom(stringify_data(data))


if __name__ == "__main__":
	SCALE = 10
	SLEEP_TIME = 0.002

	NEIGHBOR_FACTOR = 1
	TAXI_FACTOR = -1
	DIST_FACTOR = 1

	main()
