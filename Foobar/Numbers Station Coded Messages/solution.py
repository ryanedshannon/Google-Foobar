# Solution for 'Numbers Station Coded Messages.py'
def solution(l, t):
	for index, first in enumerate(l):
		start_index = end_index = index
		temp_sum = first
		while temp_sum < t:
			end_index = end_index + 1
			if end_index == len(l):
				break
			temp_sum = temp_sum + l[end_index]
		if temp_sum == t:
			return start_index, end_index
	return -1, -1
