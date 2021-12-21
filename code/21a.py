import utils


def main():
	data = utils.parse("21", parse)

	player_1_pos = player_pos_string_to_int(1, data)
	player_2_pos = player_pos_string_to_int(2, data)
	# print(player_1_pos, player_2_pos)

	player_1_score = 0
	player_2_score = 0

	die_side = 0

	rolls = 0

	while True:
		for _ in range(ROLLS_PER_TURN):
			die_side = (die_side % DIE_SIDES) + 1
			# print(f"Die side: {die_side}")
			player_1_pos = ((player_1_pos + (die_side - 1)) % MAX_POS) + 1
			# print(f"Player 1 pos: {player_1_pos}")

		rolls += 3

		player_1_score += player_1_pos
		# print(f"Player 1 score: {player_1_score}")

		if player_1_score >= WIN_SCORE:
			print(f"Player 1 won!")
			print(f"The losing player 2 has {player_2_score} score with {rolls} rolls.")
			print(f"The final result is {player_2_score * rolls}")
			break


		for _ in range(ROLLS_PER_TURN):
			die_side = (die_side % DIE_SIDES) + 1
			# print(f"Die side: {die_side}")
			player_2_pos = ((player_2_pos + (die_side - 1)) % MAX_POS) + 1
			# print(f"Player 2 pos: {player_2_pos}")

		rolls += 3

		player_2_score += player_2_pos
		# print(f"Player 2 score: {player_2_score}")

		if player_2_score >= WIN_SCORE:
			print(f"Player 2 won!")
			print(f"The losing player 1 has {player_1_score} score with {rolls} rolls.")
			print(f"The final result is {player_1_score * rolls}")
			break


def parse(line):
	return line.rstrip()


def player_pos_string_to_int(player, data):
	return int(data[player - 1].replace(f"Player {player} starting position: ", ""))


if __name__ == "__main__":
	DIE_SIDES = 100
	MAX_POS = 10
	ROLLS_PER_TURN = 3
	WIN_SCORE = 1000

	main()
