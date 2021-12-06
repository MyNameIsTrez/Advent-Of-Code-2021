import utils


def parse(line):
	fro, to = line.strip().split(" -> ") # "fro" because "from" is a reserved Python keyword
	fro_x, fro_y = fro.split(",")
	to_x, to_y = to.split(",")

	return {"from": {"x": int(fro_x), "y": int(fro_y)}, "to": {"x": int(to_x), "y": int(to_y)}}


def get_step(diff):
    if diff > 0:
        return 1
    return 0 if diff == 0 else -1


def get_pair_points(pair):
	fro, to = pair["from"], pair["to"]
	fro_x, fro_y = fro["x"], fro["y"]
	to_x, to_y = to["x"], to["y"]

	x_diff, y_diff = to_x - fro_x, to_y - fro_y

	x_step = get_step(x_diff)
	y_step = get_step(y_diff)

	x, y = fro_x, fro_y

	while not (x == to_x and y == to_y):
		yield x, y
		
		x += x_step
		y += y_step

	yield x, y # This yield makes sure the "to" coord is included


def parse_coords(data):
	coords = {} # format is { 821: { 820: 2 } }, where 821 is x, 820 is y and 2 is the number of overlaps

	for pair in data:
		for x, y in get_pair_points(pair):
			if x not in coords:
				coords[x] = {}

			if y not in coords[x]:
				coords[x][y] = 1
			else:
				coords[x][y] += 1

	return coords


def get_overlap_count(coords):
	overlap_count = 0

	for _, x in coords.items():
		for _, y in x.items():
			if y > 1:
				overlap_count += 1

	return overlap_count


if __name__ == "__main__":
	data = utils.parse("5", parse)

	coords = parse_coords(data)

	overlap_count = get_overlap_count(coords)

	print(overlap_count)