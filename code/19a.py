import utils


def main():
	data = utils.parse("19_example_2d_1", parse)

	print(data)


def parse(line):
	return line.rstrip()


if __name__ == "__main__":
	main()
