import utils


if __name__ == "__main__":
	data = utils.parse("1", int)

	windows = [sum(data[i:i+3]) for i in range(len(data))]
	print(sum([a > b for a, b in zip(windows[1:], windows)]))
