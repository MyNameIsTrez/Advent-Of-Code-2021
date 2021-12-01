import utils


if __name__ == "__main__":
	data = utils.parse("1", int)

	print(sum([a > b for a, b in zip(data[1:], data)]))
