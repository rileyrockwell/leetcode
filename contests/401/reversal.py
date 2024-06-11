from typing import *

def reversal(n: int, k: int) -> int:
	"""
	return: the number of the child who recieves the ball after k seconds
	"""
	
	# initial array
	a = [i for i in range(n)]

	# initialize the reverse state
	reversal = 0

	# initialize the starting index
	i = 0

		
	while k >= 0:

		# if no reversal (i.e. iterate left to right)
		if reversal == 0:

			# if the current index is less than the upper bound of the array
			if i < (n - 1):
				
				# continue iterating from left to right
				reversal = 0

				# increase the index by one increment
				i += 1

			# if the current index is equal to the upper bound of the array
			else:

				# reverse the iteration
				reversal = 1

				# decrease the index by one increment
				i -= 1

			# decase total number of seconds by one unit
			k -= 1

		# if reversal (i.e. iterate right to left)
		if reversal == 1:

			# if the current index is greater than the lower bound of the array
			if i > 0:
				
				# continue iterating from right to left
				reversal = 1

				# decrease the index by one increment
				i -= 1

			# if the current index is equal to the lower bound of the array
			else:

				# reverse the iteration
				reverse = 1

				# increase the index by one increment
				i += 1

			# decrease total number of seconds by one unit
			k -= 1


	# return the index at which the iteration runs out of time
	return a[i]


