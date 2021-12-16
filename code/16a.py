import utils

from collections import deque

from enum import Enum, auto

class PacketType(Enum):
	LITERAL_VALUE = 4
	OPERATOR = 6


def main():
	data = utils.parse_line('16_example_1', parse)
	# print(data)

	bits = get_hex_to_bits(data)
	print(f"Bits: {bits}")

	packet_version = get_packet_version(bits)
	print(f"Packet version: {packet_version}")

	packet_type = get_packet_type(bits)
	print(f"Packet type: {packet_type}")

	match packet_type:
		case PacketType.LITERAL_VALUE:
			parse_literal(bits)


def parse(line):
	return line.rstrip()


def get_hex_to_bits(data):
	bits_string = bin(int(data, 16))[2:]
	return deque(map(int, bits_string))


def get_packet_version(bits):
	return popleft_n_bits_to_num(bits, 3)


def popleft_n_bits(bits, n):
	sub_bits = [str(bits.popleft()) for _ in range(n)]
	return sub_bits


def popleft_n_bits_to_num(bits, n):
	sub_bits = popleft_n_bits(bits, n)
	return sub_bits_to_num(sub_bits)


def sub_bits_to_num(sub_bits):
	return int("".join(sub_bits), 2)


def get_packet_type(bits):
	packet_type_num = popleft_n_bits_to_num(bits, 3)
	return PacketType(packet_type_num)


def parse_literal(bits):
	literal_bit_string = get_literal_bit_string(bits)

	value = sub_bits_to_num(literal_bit_string)
	print(f"Literal value: {value}")


def get_literal_bit_string(bits):
	literal_bit_string = []

	while True:
		is_last_group_var = is_last_group(bits)
		# print(f"Is last group: {is_last_group_var}")

		four_bits_string = popleft_n_bits(bits, 4)
		# print(f"Four bits string: {four_bits_string}")

		literal_bit_string.extend(four_bits_string)
		# print(f"Literal bit string: {literal_bit_string}")

		if is_last_group_var:
			return literal_bit_string


def is_last_group(bits):
	return bits.popleft() == 0


if __name__ == '__main__':
	main()
