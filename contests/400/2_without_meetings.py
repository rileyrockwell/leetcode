from typing import *

def countDays(days: int, meetings: List[List[int]]) -> int:
	a = [0]*days

	for l_u_bounds in meetings:
		l_bound = l_u_bounds[0]
		u_bound = l_u_bounds[1]

		for i in range(l_bound, u_bound + 1):
			a[i - 1] = 1

	return len(a) - sum(a)


days = 10
meetings = [[5, 7], [1, 3], [9, 10]]
print(countDays(days, meetings))

days = 5
meetings = [[2, 4], [1, 3]]
print(countDays(days, meetings))

days = 6
meetings = [[1, 6]]
print(countDays(days, meetings))

# O(n^2) does not scale effectively...