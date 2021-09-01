# Solution for 'Hey, I Already Did That!.py'
def solution(n, b):
	k = len(n)
	id_list = [n]
	while True:
		y = "".join(sorted(id_list[-1]))
		x = y[::-1]
		y_int = int(y, b)
		x_int = int(x, b)
		z_int = x_int - y_int
		z = change_base(z_int, b, k)
		if z in id_list:
			return len(id_list) - id_list.index(z)
		id_list.append(z)


def change_base(x, b, k):
	digits = []
	while x:
		digits.append(str(x % b))
		x //= b
	digits = digits[::-1]
	while len(digits) < k:
		digits.append('0')
	return "".join(digits)
