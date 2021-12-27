def main():
	map = parse()
	print(f"Step: Start")
	draw_map(map)

	for step in range(1, STEPS + 1):
		move_cucumbers(map)
		print(f"Step: {step}")
		draw_map(map)


def parse():
	with open("../inputs/25_example_2.txt") as f:
		map = []

		for line in f:
			map.append([])
			row = map[-1]
			
			line = line.rstrip()

			for character in line:
				row.append(character)
		
		return map


def move_cucumbers(map):
	pass


def draw_map(map):
	for row in map:
		line = "".join(row)
		print(line)
	
	print()


if __name__ == "__main__":
	STEPS = 1

	main()
