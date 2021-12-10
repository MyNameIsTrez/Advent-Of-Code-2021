import utils


def main():
	data = utils.parse("9", parse)

	width = len(data[0])
	height = len(data)

	# print(data)

	sum = 0

	for y in range(height):
		for x in range(width):
			if x > 0 and data[y][x-1] <= data[y][x]:
				continue
			if x + 1 < width and data[y][x+1] <= data[y][x]:
				continue

			if y > 0 and data[y-1][x] <= data[y][x]:
				continue
			if y + 1 < height and data[y+1][x] <= data[y][x]:
				continue

			sum += 1 + data[y][x]

	print(sum)


def parse(line):
	return list(map(int, list(line[:-1])))


if __name__ == "__main__":
	main()