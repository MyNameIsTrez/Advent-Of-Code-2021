import utils


def main():
	target = utils.parse_line("17", parse)

	best_steps = None

	valid_velocity_values_count = 0

	highest_x_velocity = 0

	lowest_y_velocity = float("inf")
	highest_y_velocity = 0

	for y_velocity in range(STARTING_Y_VELOCITY, ENDING_Y_VELOCITY):
		for x_velocity in range(STARTING_X_VELOCITY, ENDING_X_VELOCITY):
			steps = run(x_velocity, y_velocity, target)

			if steps:
				best_steps = steps
				valid_velocity_values_count += 1

				highest_x_velocity = max(highest_x_velocity, x_velocity)

				lowest_y_velocity = min(lowest_y_velocity, y_velocity)
				highest_y_velocity = max(highest_y_velocity, y_velocity)

	world = get_world(target, best_steps)

	draw_world(world)

	print(f"Highest X velocity: {highest_x_velocity}")

	print(f"Lowest Y velocity: {lowest_y_velocity}")
	print(f"Highest Y velocity: {highest_y_velocity}")

	print(f"Highest Y value reached: {get_highest_y_value(best_steps)}")
	print(f"Valid velocity values count: {valid_velocity_values_count}")


def run(starting_x_velocity, starting_y_velocity, target):
	probe = get_new_probe(starting_x_velocity, starting_y_velocity)

	steps = []

	while True:
		step(probe)
		probe_position = get_probe_position(probe)

		if is_probe_outside_map(probe_position, target):
			return False

		steps.append(probe_position)

		if is_probe_in_target_area(probe_position, target):
			return steps


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
		"x": START_X,
		"y": START_Y,
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
	return (probe_position["x"] > target["max_x"] or
			probe_position["y"] < target["min_y"])


def get_world(target, steps):
	world_min_x, world_max_x, world_max_y, world_min_y = get_world_bounds(target, steps)

	world = get_empty_world(world_min_x, world_max_x, world_max_y, world_min_y)

	world[world_y_to_list_y(START_Y, world_max_y)][START_X] = "S"

	add_target_area_to_world(target, world, world_max_y)

	add_steps_to_world(steps, world_max_y, world)

	return world


def get_empty_world(world_min_x, world_max_x, world_max_y, world_min_y):
	world_width = world_max_x - world_min_x + 1
	world_height = world_max_y - world_min_y + 1

	empty_world = [ ["."] * world_width for _ in range(world_height) ]

	return empty_world


def get_world_bounds(target, steps):
	world_min_x = START_X
	world_max_x = target["max_x"]

	world_max_y = get_world_max_y(steps)
	world_min_y = target["min_y"]

	return world_min_x, world_max_x, world_max_y, world_min_y


def get_world_max_y(steps):
	steps_with_start = [ { "x": START_X, "y": START_Y }, *steps ]
	max_y_step = max(steps_with_start, key=lambda step_: step_["y"])
	world_max_y = max_y_step["y"]
	return world_max_y


def add_steps_to_world(steps, world_max_y, world):
	for probe_position in steps:
		x = probe_position["x"]
		y = world_y_to_list_y(probe_position["y"], world_max_y)
		world[y][x] = "#"


def world_y_to_list_y(probe_position_y, world_max_y):
	return world_max_y - probe_position_y


def add_target_area_to_world(target, world, world_max_y):
	for world_y in range(target["max_y"], target["min_y"] - 1, -1):
		for x in range(target["min_x"], target["max_x"] + 1):
			y = world_y_to_list_y(world_y, world_max_y)
			world[y][x] = "T"


def draw_world(world):
	for row in world:
		print("".join(row))


def get_highest_y_value(best_steps):
	best_step = max(best_steps, key=lambda x : x["y"])
	highest_y_value = best_step["y"]
	return highest_y_value


if __name__ == "__main__":
	STARTING_X_VELOCITY = 0
	STARTING_Y_VELOCITY = -200

	ENDING_X_VELOCITY = 100
	ENDING_Y_VELOCITY = 500

	START_X = 0
	START_Y = 0

	main()
