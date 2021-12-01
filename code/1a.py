import utils


if __name__ == "__main__":
	data = utils.parse("1", int)

	print(sum([r > l for r, l in zip(data[1:], data)]))
