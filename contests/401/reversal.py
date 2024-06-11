from typing import *

def reversal(n: int, k: int) -> int:
	"""
	return: the index of the child who recieves the ball after k seconds
	"""
	
	# initial array
	a = [i for i in range(n)]

	# initialize direction of iteration
	left_to_right = 1

	# initialize the starting index
	i = 0

		
	while k > 0:

		# if no reversal (i.e. iterate left to right)
		if left_to_right == 1:

			# if the current index is less than the upper bound of the array
			if i < (n - 1):
				
				# continue iterating from left to right
				left_to_right = 1

				# increase the index by one increment
				i += 1
		

			# if the current index is equal to the upper bound of the array
			else:

				# reverse the iteration
				left_to_right = 0

				# ensure the terminal index is not at the reversal state; if so, return index
				if k == 0:
					return a[i]

				# decrease the index by one increment
				i -= 1
				

			# decrease total number of seconds by one unit
			k -= 1

		# if reversal (i.e. iterate right to left)
		elif left_to_right == 0:

			# if the current index is greater than the lower bound of the array
			if i > 0:
				
				# continue iterating from right to left
				left_to_right = 0

				# decrease the index by one increment
				i -= 1
				
	
			# if the current index is equal to the lower bound of the array
			else:

				# reverse the iteration
				left_to_right = 0

				# ensure the terminal index is not at the reversal state; if so, return index
				if k == 0:
					return a[i]

				# increase the index by one increment
				i += 1
				

			# decrease total number of seconds by one unit
			k -= 1


	# return the index at which the iteration runs out of time
	return a[i]


# NOT MY SOLUTION
def reversal(n: int, k: int) -> int:
	n -= 1
	rounds = k // n
	remainder = k % n

	if rounds % 2 == 0:
		return remainder

	else:
		return n - remainder


# ^ALWAYS GO W/ INITIAL INTUITION. TRUST YOUR INTUITION. DON'T SECOND-GUESS YOURSELF. NO MORE TANGENTS. PLEASE.

n, k = 3, 5
print(reversal(n, k))

n, k = 5, 6
print(reversal(n, k))

n, k = 4, 2
print(reversal(n, k))

n, k = 2, 2
print(reversal(n, k), "expected: 0")

n, k = 3, 3
print(reversal(n, k), "expected: 1")

n, k = 4, 4
print(reversal(n, k), "expected: 2")

n, k = 3, 6
print(reversal(n, k), "expected: 2")