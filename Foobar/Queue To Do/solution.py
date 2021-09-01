import math


def solution(start, length):
	# XOR value
	counter = 0
	size = int(math.ceil(math.log(start + (length**2)/2, 2)))
	binary = bin(start)
	print(binary)
	bits = []
	# XORs first 'l' IDs in each line, `l` counts down
	for y in range(1, size + 1):
		x = False
		s = start
		for l in range(length, 0, -1):
			for i in range(s, (s + l) % 2**y):
				x ^= i
			s = s + length
		bits.append(x)
	print(bits)


print(solution(0, 3))  # 2
print(solution(17, 4))  # 14