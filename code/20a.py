import utils, math


"""
AN EXAMPLE OF INFINITE BEHAVIOR WITH THE IMAGE ENHANCEMENT ALGORITHM FROM 20.txt
000-000-000 IS 1
111-111-111 IS 0
STARTING CELL ALIVE = 11, STARTING CELL DEAD = 00, ALIVE CELL = ██, DEAD CELL = EMPTY SPACE

START:

  11


AFTER STEP 1:
████████████
████████████
██████  ████
████00██████
████████████
████████████

THIS ONE ISN'T CORRECT YET:
AFTER STEP 2:
████████████
████████████
██████  ████
████11██████
████████████
████████████
"""
def main():
	enhancement, input_image = parse()
	# print(enhancement)
	# print(input_image)


	# enhancement_index = int("000000001", 2)
	# next_cell_state = enhancement[enhancement_index]
	# print(f"Top-left of starting cell state after step 1: {next_cell_state}")

	# enhancement_index = int("000000010", 2)
	# next_cell_state = enhancement[enhancement_index]
	# print(f"Top of starting cell state after step 1: {next_cell_state}")

	# enhancement_index = int("000000100", 2)
	# next_cell_state = enhancement[enhancement_index]
	# print(f"Top-right of starting cell state after step 1: {next_cell_state}")

	# enhancement_index = int("000001000", 2)
	# next_cell_state = enhancement[enhancement_index]
	# print(f"Left of starting cell state after step 1: {next_cell_state}")

	# enhancement_index = int("000010000", 2)
	# next_cell_state = enhancement[enhancement_index]
	# print(f"Starting cell state after step 1: {next_cell_state}")

	# enhancement_index = int("000100000", 2)
	# next_cell_state = enhancement[enhancement_index]
	# print(f"Right of starting cell state after step 1: {next_cell_state}")

	# enhancement_index = int("001000000", 2)
	# next_cell_state = enhancement[enhancement_index]
	# print(f"Bottom-left of starting cell state after step 1: {next_cell_state}")

	# enhancement_index = int("010000000", 2)
	# next_cell_state = enhancement[enhancement_index]
	# print(f"Bottom of starting cell state after step 1: {next_cell_state}")

	# enhancement_index = int("100000000", 2)
	# next_cell_state = enhancement[enhancement_index]
	# print(f"Bottom-right of starting cell state after step 1: {next_cell_state}")


	# enhancement_index = int("111101011", 2)
	# next_cell_state = enhancement[enhancement_index]
	# print(f"Top-right of starting cell state after step 2: {next_cell_state}")

	# enhancement_index = int("110101111", 2)
	# next_cell_state = enhancement[enhancement_index]
	# print(f"Starting cell state after step 2: {next_cell_state}")


	alive = initialize_alive(input_image)
	# print(alive)

	print("Step: Start")
	print(f"Alive cells: {len(alive)}")
	print_grid(alive)

	for step in range(1, STEPS + 1):
		alive = get_next_alive(alive, enhancement, step)

		print(f"Step: {step}")
		print(f"Alive cells: {len(alive)}")
		print_grid(alive)


def parse():
	enhancement = ""
	input_image = []

	reading_enhancement = True

	# with open("../inputs/20_example.txt") as f:
	with open("../inputs/20_infinity_test.txt") as f:
		lines = f.read().splitlines()
	for line in lines:
		if line == "":
			reading_enhancement = False
			continue

		binary_string = characters_to_binary_string(line)

		if reading_enhancement:
			enhancement += binary_string
		else:
			input_image.append(binary_string)

	return enhancement, input_image


def characters_to_binary_string(line):
	return line.replace(".", "0").replace("#", "1")


def initialize_alive(input_image):
	alive = set()

	for y in range(len(input_image)):
		for x in range(len(input_image[0])):
			if input_image[y][x] == "1":
				alive.add( (x, y) )

	return alive


def print_grid(alive):
	min_x, min_y, max_x, max_y = get_grid_dimensions(alive)
	# print(min_x, min_y, max_x, max_y)

	width  = max_x - min_x + 1
	height = max_y - min_y + 1
	# print(width, height)

	grid = get_empty_grid(width, height)

	set_alive_cells(alive, grid, min_x, min_y)

	for row in grid:
		line = "".join(row)
		print(line)
	print()



def get_grid_dimensions(alive):
	min_x = math.inf
	min_y = math.inf
	max_x = 0
	max_y = 0

	for cell in alive:
		cell_x = cell[0]
		cell_y = cell[1]

		min_x = min(min_x, cell_x)
		min_y = min(min_y, cell_y)

		max_x = max(max_x, cell_x)
		max_y = max(max_y, cell_y)

	print(min_x, min_y, max_x, max_y)

	return min_x, min_y, max_x, max_y


def get_empty_grid(width, height):
	return [ ["."] * width for _ in range(height) ]


def set_alive_cells(alive, grid, min_x, min_y):
	for cell in alive:
		cell_x = cell[0]
		cell_y = cell[1]

		grid[cell_y - min_y][cell_x - min_x] = "#"


def get_next_alive(alive, enhancement, step):
	inspectable_cells = get_inspectable_cells(alive)
	# print(inspectable_cells)

	next_alive = set()

	for cell in inspectable_cells:
		next_cell_state = get_next_cell_state(cell, alive, enhancement, step, inspectable_cells)

		if next_cell_state == "1":
			next_alive.add(cell)

	return next_alive


def get_inspectable_cells(alive):
	inspectable_cells = set()

	for cell in alive:
		for neighbor_x, neighbor_y in neighbors_iterator(cell, alive):
			if (neighbor_x, neighbor_y) not in inspectable_cells:
				inspectable_cells.add( (neighbor_x, neighbor_y) )

	return inspectable_cells


def neighbors_iterator(cell, alive):
	cell_x = cell[0]
	cell_y = cell[1]

	for neighbor_y in range(cell_y - 1, cell_y + 2):
		for neighbor_x in range(cell_x - 1, cell_x + 2):
			yield neighbor_x, neighbor_y


def get_next_cell_state(cell, alive, enhancement, step, inspectable_cells):
	neighbors_string = ""

	for neighbor_x, neighbor_y in neighbors_iterator(cell, alive):
		if (neighbor_x, neighbor_y) in alive:
			neighbors_string += "1"
		else:
			if (neighbor_x, neighbor_y) in inspectable_cells:
				neighbors_string += "0"
			else:
				neighbors_string += "0" if step % 2 == 1 else "1"

	enhancement_index = int(neighbors_string, 2)
	next_cell_state = enhancement[enhancement_index]

	return next_cell_state


if __name__ == "__main__":
	STEPS = 2

	main()
