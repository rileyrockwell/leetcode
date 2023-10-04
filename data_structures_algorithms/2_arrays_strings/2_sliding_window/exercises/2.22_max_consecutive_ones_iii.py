def longestOnes(nums, k):
	"""
	nums: [int]
	k: int
	return: int
	
	objective: Given a binary array nums and an integer k, return the maximum number of
	consecutive "1" elements in the array if you can flip at most k "0" elements.
	"""
	# using sliding window techinque
	

	left = curr_sum = answer = 0

	for right in range(len(nums)):
		curr_sum += nums[right]

	# edm == fantasy == isolation == despair

	# live in reality i.e. people in your room, constantly, writing software and making things happen.

	# you should get to a point where you are having parties in your room. every night of the week. 100% agree. 7 nights / wk. parties in your room 7 nights / wk.

	# in each iteration of the loop, answer is the max of right - left, or answer.

	return curr_sum


nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(longestOnes(nums, k))