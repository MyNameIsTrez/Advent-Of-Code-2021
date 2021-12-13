import math

import numpy as np


def main():
	coordinates, folds = parse("13")
	# coordinates, folds = parse("13")

	# print(coordinates)
	# print(folds)

	matrix = get_empty_matrix(coordinates)
	# print(matrix)

	fill_matrix(matrix, coordinates)
	# print(matrix)

	for fold in folds:
		# print(fold)
		matrix = get_folded(fold, matrix)
		# print(np.count_nonzero(matrix))
		# print(matrix)

	for row in matrix:
		# print("".join(list(str(row))))
		print(np.array2string(row, separator="").replace("0", " ").replace("1", "#"))
	# print(np.count_nonzero(matrix))


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
				x, y = line.split(",")
				coordinates.append({ "x": int(x), "y": int(y) })
			else:
				axis, value = line.split("=")
				folds.append({ "axis": axis[-1], "value": int(value) })

	return coordinates, folds


def get_empty_matrix(coordinates):
	bottom_right = get_bottom_right(coordinates)
	# print(bottom_right)

	width = bottom_right["x"] + 1
	height = bottom_right["y"] + 1
	# print(width, height)

	matrix = np.zeros((height, width), dtype=int)

	return matrix


def get_bottom_right(coordinates):
	max_x = minimum_y = 0
	for coordinate in coordinates:
		if coordinate["x"] > max_x:
			max_x = coordinate["x"]
		if coordinate["y"] > minimum_y:
			minimum_y = coordinate["y"]
	return { "x": max_x, "y": minimum_y }


def fill_matrix(matrix, coordinates):
	for coordinate in coordinates:
		# print(matrix[coordinate["y"]][coordinate["x"]])
		# print(coordinate)
		matrix[coordinate["y"]][coordinate["x"]] = 1


def get_folded(fold, matrix):
	value = fold["value"]
	return fold_lr(value, matrix) if fold["axis"] == "x" else fold_ud(value, matrix)


def fold_ud(y, matrix):
	return matrix[:y] | np.flipud(matrix[y+1:])

def fold_lr(x, matrix):
	return matrix[:,:x] | np.fliplr(matrix[:,x+1:])

if __name__ == "__main__":
	main()
