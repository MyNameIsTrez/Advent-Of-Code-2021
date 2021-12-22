import utils


def main():
	scanners = parse()

	print(scanners)


def parse():
	scanners = []

	with open("../inputs/19_example_2d_1.txt") as f:
		for line in f.readlines():
			line = line.rstrip()

			if "--" in line: # If this line announces a new scanner number
				scanners.append([])
			elif line != "":
				x, y = line.split(",")
				beacon_coordinate = (int(x), int(y))
				scanners[-1].append(beacon_coordinate)

	return scanners


def get_distance_squared(beacon_1, beacon_2):
	return ((beacon_1[0] - beacon_2[0]) ** 2 +
			(beacon_1[1] - beacon_2[1]) ** 2)


if __name__ == "__main__":
	main()
