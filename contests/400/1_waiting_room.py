from typing import *

def minimumChairs(s: str) -> int:
	counter = 0
	max_val = 0

	for i in range(len(s)):

		if s[i] == "E":
			counter += 1

			if counter > max_val:
				max_val = counter

		elif s[i] == "L":
			counter -= 1

	return max_val


s = "EEEEEEE"
print(minimumChairs(s))

s = "ELELEEL"
print(minimumChairs(s))