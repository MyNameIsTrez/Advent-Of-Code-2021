import utils


def main():
	data = utils.parse("1", int)

	print(sum([r > l for r, l in zip(data[1:], data)]))


if __name__ == "__main__":
	main()
