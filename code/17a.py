import utils


def main():
	target = utils.parse_line("17_example_1", parse)

	x_velocity = 7
	y_velocity = 2
	probe = get_new_probe(x_velocity, y_velocity)

	steps = []

	while True:
		step(probe)
		probe_position = get_probe_position(probe)
		steps.append(probe_position)

		is_probe_in_target_area_bool = is_probe_in_target_area(probe_position, target)
		is_probe_outside_map_bool = is_probe_outside_map(probe_position, target)

		if is_probe_in_target_area_bool or is_probe_outside_map_bool:
			break

	world = get_world(target, steps)

	draw_world(world)


def parse(line):
	left, right = line.rstrip().split(", y=")

	start_index = len("target area: x=")
	left_without_name = left[start_index:]

	min_x, max_x = get_split_min_and_max(left_without_name)
	min_y, max_y = get_split_min_and_max(right)

	target = {
		"min_x": min_x,
		"max_x": max_x,
		"min_y": min_y,
		"max_y": max_y,
	}
	return target


def get_split_min_and_max(string):
	min_string, max_string = string.split("..")
	min_ = int(min_string)
	max_ = int(max_string)

	return min_, max_


def get_new_probe(x_velocity, y_velocity):
	probe = {
		"x": 0,
		"y": 0,
		"x_velocity": x_velocity,
		"y_velocity": y_velocity
	}
	return probe


def get_probe_position(probe):
	probe_position = {
		"x": probe["x"],
		"y": probe["y"],
	}
	return probe_position


def step(probe):
	probe["x"] += probe["x_velocity"]
	probe["y"] += probe["y_velocity"]
	probe["x_velocity"] -= sign(probe["x_velocity"])
	probe["y_velocity"] -= 1


def sign(n):
    return (n > 0) - (n < 0)


def is_probe_in_target_area(probe_position, target):
	return (target["min_x"] <= probe_position["x"] <= target["max_x"] and
			target["min_y"] <= probe_position["y"] <= target["max_y"])


def is_probe_outside_map(probe_position, target):
	return probe_position["x"] <= target["max_x"] and probe_position["y"] <= target["max_y"]


def get_world(target, steps):
	world_min_x, world_max_x, world_max_y, world_min_y = get_world_bounds(target, steps)

	world = get_empty_world(world_min_x, world_max_x, world_max_y, world_min_y)

	world[world_max_y][0] = "S"

	add_target_area_to_world(target, world, world_max_y)

	add_steps_to_world(steps, world_max_y, world)

	return world


def get_empty_world(world_min_x, world_max_x, world_max_y, world_min_y):
	world_width = world_max_x - world_min_x + 1
	world_height = world_max_y - world_min_y + 1

	empty_world = [ ["."] * world_width for _ in range(world_height) ]

	return empty_world


def get_world_bounds(target, steps):
	world_min_x = 0
	world_max_x = target["max_x"]

	world_max_y = get_world_max_y(steps)
	world_min_y = target["min_y"]

	return world_min_x, world_max_x, world_max_y, world_min_y


def get_world_max_y(steps):
	max_y_step = max(steps, key=lambda step_: step_["y"])
	world_max_y = max_y_step["y"]
	return world_max_y


def add_steps_to_world(steps, world_max_y, world):
	for probe_position in steps:
		x = probe_position["x"]
		y = world_y_to_list_y(probe_position["y"], world_max_y)
		world[y][x] = "#"


def world_y_to_list_y(probe_position_y, world_max_y):
	return world_max_y + 0 - probe_position_y


def add_target_area_to_world(target, world, world_max_y):
	for world_y in range(target["max_y"], target["min_y"] - 1, -1):
		for x in range(target["min_x"], target["max_x"] + 1):
			y = world_y_to_list_y(world_y, world_max_y)
			world[y][x] = "T"


def draw_world(world):
	for row in world:
		print("".join(row))


if __name__ == "__main__":
	main()
