from enum import Enum, auto


class MoveDirection(Enum):
	UP = auto()
	DOWN = auto()
	LEFT = auto()
	RIGHT = auto()


def control_sequence(seq):
	print(f"\033[{seq}", end="")

def clear_rest_of_line():
	control_sequence("0K")

def clear_beginning_of_line():
	control_sequence("1K")

def clear_line():
	control_sequence("2K")

def move_cursor(dir, n=1):
	match dir:
		case MoveDirection.UP:
			control_sequence(f"{n}A")
		case MoveDirection.DOWN:
			control_sequence(f"{n}B")
		case MoveDirection.RIGHT:
			control_sequence(f"{n}C")
		case MoveDirection.LEFT:
			control_sequence(f"{n}D")

def replace_lines(str, n=0):
	move_cursor(MoveDirection.UP, n)
	lines = str.split("\n")
	[print(line, end="\033[0K\n") for line in lines]
	move_cursor(MoveDirection.DOWN, n - len(lines))

def replace_bottom(str):
	lines = str.split("\n")
	move_cursor(MoveDirection.UP, len(lines))
	[print(line, end="\033[0K\n") for line in lines]
