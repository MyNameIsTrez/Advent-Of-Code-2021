import utils


def main():
	enhancement, input_image = parse()

	print(enhancement)
	print(input_image)


def parse():
	enhancement = ""
	input_image = []

	reading_enhancement = True

	with open("../inputs/20_example.txt") as f:
		lines = f.read().splitlines()
	for line in lines:
		if line == "":
			reading_enhancement = False
			continue

		binary_string = characters_to_binary_string(line)
		if reading_enhancement:
			enhancement += binary_string
		else:
			input_image.append(binary_string)

	return enhancement, input_image


def characters_to_binary_string(line):
	return line.replace(".", "0").replace("#", "1")


if __name__ == "__main__":
	main()
