import utils


def main():
	data = utils.parse("1", parse)

	print(sum([r > l for r, l in zip(data[1:], data)]))


def parse(line):
	return int(line)


if __name__ == "__main__":
	main()
