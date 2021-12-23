import utils


def main():
	data = utils.parse("21", parse) # TODO: Don't use the example!

	player_1_pos = player_pos_string_to_int(1, data)
	player_2_pos = player_pos_string_to_int(2, data)
	# print(player_1_pos, player_2_pos)

	player_1_score = 0
	player_2_score = 0
	# print(player_1_score, player_2_score)

	player_1_wins, player_2_wins = solve(player_1_pos, player_1_score, player_2_pos, player_2_score, 1)
	print(player_1_wins, player_2_wins)


def parse(line):
	return line.rstrip()


def player_pos_string_to_int(player, data):
	return int(data[player - 1].replace(f"Player {player} starting position: ", ""))


def solve(player_1_pos, player_1_score, player_2_pos, player_2_score, player_turn):
	arguments = (player_1_pos, player_1_score, player_2_pos, player_2_score, player_turn)

	if arguments in cache:
		return cache[arguments]


	player_1_wins = 0
	player_2_wins = 0

	next_player_turn = 2 if player_turn == 1 else 1

	for triple_die_total in triple_die_total_generator():
		if player_turn == 1:
			next_player_1_pos = ((player_1_pos + (triple_die_total - 1)) % MAX_POS) + 1
			next_player_1_score = player_1_score + next_player_1_pos

			if next_player_1_score >= WIN_SCORE:
				player_1_wins += 1
			else:
				additional_player_1_wins, additional_player_2_wins = solve(next_player_1_pos, next_player_1_score, player_2_pos, player_2_score, next_player_turn)
				player_1_wins += additional_player_1_wins
				player_2_wins += additional_player_2_wins
		else:
			next_player_2_pos = ((player_2_pos + (triple_die_total - 1)) % MAX_POS) + 1
			next_player_2_score = player_2_score + next_player_2_pos

			if next_player_2_score >= WIN_SCORE:
				player_2_wins += 1
			else:
				additional_player_1_wins, additional_player_2_wins = solve(player_1_pos, player_1_score, next_player_2_pos, next_player_2_score, next_player_turn)
				player_1_wins += additional_player_1_wins
				player_2_wins += additional_player_2_wins

	cache[arguments] = (player_1_wins, player_2_wins)

	return cache[arguments]


def triple_die_total_generator():
	for die_side_1 in range(1, DIE_SIDES + 1):
		for die_side_2 in range(1, DIE_SIDES + 1):
			for die_side_3 in range(1, DIE_SIDES + 1):
				triple_die_total = die_side_1 + die_side_2 + die_side_3
				yield triple_die_total


if __name__ == "__main__":
	DIE_SIDES = 3
	MAX_POS = 10
	WIN_SCORE = 21

	cache = dict()

	main()
