def main():
	map = parse()
	print(f"Initial state:")
	draw_map(map)

	step = 1

	while True:
	# for _ in range(3):
		print(f"After {step} steps:")

		map_after_moving_right, cucumber_moved = move_cucumbers(map)

		map = map_after_moving_right
		
		# draw_map(map)

		if not cucumber_moved:
			break

		step += 1


def parse():
	with open("../inputs/25.txt") as f:
		map = []

		for line in f:
			map.append([])
			row = map[-1]
			
			line = line.rstrip()

			for character in line:
				row.append(character)
		
		return map


def draw_map(map):
	for row in map:
		line = "".join(row)
		print(line)
	
	print()


def move_cucumbers(map):
	cucumber_moved = False

	map_after_moving_right = get_map_copy(map)

	width = len(map[0])

	for x, y, character in character_generator(map):
		next_x = (x + 1) % width
		if character == ">" and map[y][next_x] == ".":
			map_after_moving_right[y][x]      = "."
			map_after_moving_right[y][next_x] = ">"

			cucumber_moved = True

	map_after_moving_down = get_map_copy(map_after_moving_right)

	height = len(map)
	
	for x, y, character in character_generator(map_after_moving_right):
		next_y = (y + 1) % height
		if character == "v" and map_after_moving_right[next_y][x] == ".":
			map_after_moving_down[y][x]      = "."
			map_after_moving_down[next_y][x] = "v"

			cucumber_moved = True

	map = map_after_moving_down

	return map, cucumber_moved


def get_map_copy(map):
	map_copy = [ row.copy() for row in map ]

	return map_copy


def character_generator(map):
	for y, row in enumerate(map):
		for x, character in enumerate(row):
			yield x, y, character


if __name__ == "__main__":
	STEPS = 4

	main()
