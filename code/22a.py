import utils


def main():
	data = utils.parse("22_example_1", parse)

	print(data)


def parse(line):
	state, coordinates = line.split()

	x_coordinates, y_coordinates, z_coordinates = coordinates.split(",")

	x_start, x_end = get_start_and_end(x_coordinates)
	y_start, y_end = get_start_and_end(y_coordinates)
	z_start, z_end = get_start_and_end(z_coordinates)

	return {
		"state": state,
		"x_start": x_start, "x_end": x_end,
		"y_start": y_start, "y_end": y_end,
		"z_start": z_start, "z_end": z_end
	}


def get_start_and_end(coordinates):
	start_string, end_string = coordinates.split("..")
	start = int(start_string[2:])
	end = int(end_string)
	return start, end


if __name__ == "__main__":
	main()
