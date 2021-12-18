import utils

from collections import deque

from enum import Enum, auto

class PacketType(Enum):
	LITERAL_VALUE = 4
	OPERATOR = auto()


class LengthType(Enum):
	SUBPACKETS_LENGTH = 0
	SUBPACKET_COUNT = 1


def main():
	data = utils.parse_line('16', parse)

	bits = get_hex_to_bits(data)

	solve(bits)


def solve(bits):
	global PACKET_VERSION_SUM

	packet_version = get_packet_version(bits)
	PACKET_VERSION_SUM += packet_version

	packet_type = get_packet_type(bits)

	match packet_type:
		case PacketType.LITERAL_VALUE:
			return get_literal_value(bits)
		case PacketType.OPERATOR:
			length_type = get_length_type(bits)

			operands = []

			match length_type:
				case LengthType.SUBPACKETS_LENGTH:
					subpackets_length = get_subpackets_length(bits)

					starting_bits_length = len(bits)
					while True:
						new_bits_length = len(bits)
						bits_read = starting_bits_length - new_bits_length

						if bits_read == subpackets_length:
							break

						operand = solve(bits)
						operands.append(operand)
				case LengthType.SUBPACKET_COUNT:
					subpacket_count = get_subpacket_count(bits)

					for _ in range(subpacket_count):
						operand = solve(bits)
						operands.append(operand)


def parse(line):
	return line.rstrip()


def get_hex_to_bits(data):
	# Adds leading "1" and removes it with [3:] to keep leading zeros
	bits_string_list = bin(int("1" + data, 16))[3:]
	return deque(map(int, bits_string_list))


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
	packet_type = PacketType.LITERAL_VALUE if packet_type_num == 4 else PacketType.OPERATOR
	return packet_type


def get_literal_value(bits):
	literal_bit_string = get_literal_bit_string(bits)

	literal_value = sub_bits_to_num(literal_bit_string)
	return literal_value


def get_literal_bit_string(bits):
	literal_bit_string = []

	while True:
		is_last_group_var = is_last_group(bits)

		four_bits_string = popleft_n_bits(bits, 4)

		literal_bit_string.extend(four_bits_string)

		if is_last_group_var:
			return literal_bit_string


def is_last_group(bits):
	return bits.popleft() == 0


def get_length_type(bits):
	length_type_id_bit = bits.popleft()
	length_type = LengthType(length_type_id_bit)
	return length_type


def get_subpackets_length(bits):
	return popleft_n_bits_to_num(bits, 15)


def get_subpacket_count(bits):
	return popleft_n_bits_to_num(bits, 11)


if __name__ == '__main__':
	PACKET_VERSION_SUM = 0

	main()

	print(f"Packet version sum: {PACKET_VERSION_SUM}")