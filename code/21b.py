import utils


def main():
	data = utils.parse("21_example", parse) # TODO: Don't use the example!

	player_1_pos = player_pos_string_to_int(1, data)
	player_2_pos = player_pos_string_to_int(2, data)
	# print(player_1_pos, player_2_pos)

	player_1_score = 0
	player_2_score = 0
	# print(player_1_score, player_2_score)


	states = get_empty_states()

	states[player_1_pos - 1] = 1
	# states[7] = 1
	print(states)


	for _ in range(15):
		new_states = get_empty_states()

		for state_index, state_count in enumerate(states):
			# TODO: I'm not sure whether the die should be rolled more than once
			for offset in range(1, DIE_SIDES + 1):
				new_state_index = (state_index + offset) % MAX_POS
				new_states[new_state_index] += state_count

		print(new_states)

		states = new_states


def parse(line):
	return line.rstrip()


def player_pos_string_to_int(player, data):
	return int(data[player - 1].replace(f"Player {player} starting position: ", ""))


def get_empty_states():
	return [0] * 10


if __name__ == "__main__":
	DIE_SIDES = 3
	MAX_POS = 10
	WIN_SCORE = 21

	main()
