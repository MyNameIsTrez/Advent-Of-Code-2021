import utils


def parse(line):
	return list(map(int, line.strip().split(",")))


def init_schedules(days, init_fishes):
	schedules = [0] * (days + 9) # Children go from 8 to 0, so + 9

	for fish in init_fishes:
		schedules[fish] += 1

	return schedules


def update(day, schedules, days):
	added_fish_count = schedules[day]
	schedules[day + 7] += added_fish_count # Move parents
	schedules[day + 9] += added_fish_count # Create children
	return added_fish_count


if __name__ == "__main__":
	days = 256

	init_fishes = utils.parse_line("6", parse)

	fish_count = len(init_fishes)

	schedules = init_schedules(days, init_fishes)

	for day in range(days):
		fish_count += update(day, schedules, days)

	print(fish_count)
