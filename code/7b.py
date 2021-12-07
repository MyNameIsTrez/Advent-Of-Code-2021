import utils
import math


# sum(4) = (1 + 4) * (4 / 2)
# sum(5) = (1 + 5) * (5 / 2)
def summation(n):
	return int((1 + n) * (n / 2))


if __name__ == "__main__":
	data = utils.parse_line_csv("7_example")

	minimum, maximum = min(data), max(data)

	best_fuel = float('inf')
	for cur in range(minimum, maximum):
		fuel = 0
		for datum in data:
			fuel += summation(abs(cur - datum))
		if fuel < best_fuel:
			best_fuel = fuel
	print(best_fuel)


# 0 0 0 0 0 0 0 0 100
#         ^
# 0 0 0 0 (0) 0 0 0 100
# 0 0 0 0  0  0 0 0 100

# 3  3  3  3  3  3  3  3  100
# 39 39 39 39 39 39 39 39 58

#  3  3  3  3  3  3  3  3          100
# -1 -1 -1 -1 -1 -1 -1 -1          +1


# -1 * left_count + 1 * right_count
