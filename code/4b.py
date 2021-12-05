def parse():
	with open("../inputs/4.txt") as f:
		drawn = [int(num) for num in f.readline().split(",")]

		# Reads the boards
		boards = []
		board = []
		for line in f:
			if line == "\n":
				boards.append(board)
				board = []
			else:
				board.append([int(num) for num in line.split(" ") if num != ""])

		boards = boards[1:] # Removes the first, empty list
	
	return drawn, boards


# Marks drawn numbers on a board by setting them to None
def draw(draw_num, board):
	for row in board:
		for i, num in enumerate(row):
			if num == draw_num:
				row[i] = None
				#return # TODO: Can the same number appear multiple times on a board in 4.txt?


def check_bingo(board):
	# Horizontal bingo checking
	for row in range(5):
		bingo = True
		for col in range(5):
			if board[row][col] != None:
				bingo = False
		if bingo:
			return True

	# Vertical bingo checking
	for col in range(5):
		bingo = True
		for row in range(5):
			if board[row][col] != None:
				bingo = False
		if bingo:
			return True


def get_board_sum(board):
	sum = 0
	for row in board:
		for num in row:
			if num:
				sum += num
	return sum


def main():
	drawn, boards = parse()

	bingo_board_indices = []
	final_bingo_nums = []

	for draw_num in drawn:
		for i, board in enumerate(boards):
			if i in bingo_board_indices: # get_board_sum requires no more None values to be placed on bingo boards
				continue

			draw(draw_num, board)

			if i not in bingo_board_indices and check_bingo(board):
				bingo_board_indices.append(i)
				final_bingo_nums.append(draw_num)

	print(get_board_sum(boards[bingo_board_indices.pop()]) * final_bingo_nums.pop())


if __name__ == "__main__":
	main()