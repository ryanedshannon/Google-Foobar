import math


# Solution for 'Solar Doomsday.py'
def solution(area):
	squares = []
	while 1 <= area <= 1000000:
		square = int(math.floor(area**.5)**2)
		squares.append(square)
		area -= square
	return squares
