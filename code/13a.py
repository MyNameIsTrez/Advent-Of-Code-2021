def main():
	coordinates, folds = parse("13")

	print(coordinates)
	print(folds)


def parse(day):
	coordinates = []
	folds = []

	reading_type = "coordinates"

	with open("../inputs/" + day + ".txt") as f:
		for ln in f:
			line = ln.rstrip()

			if line == "":
				reading_type = "folds"
				continue

			if reading_type == "coordinates":
				left, right = line.split(",")
				coordinates.append([int(left), int(right)])
			else:
				left, right = line.split("=")
				folds.append([left[-1], int(right)])

	return coordinates, folds


if __name__ == "__main__":
	main()
