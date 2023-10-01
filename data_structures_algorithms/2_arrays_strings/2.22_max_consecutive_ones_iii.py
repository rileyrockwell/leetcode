def longestOnes(nums, k):
	"""
	nums: [int]
	k: int
	return: int
	
	objective: Given a binary array nums and an integer k, return the maximum number of
	consecutive "1" elements in the array if you can flip at most k "0" elements.
	"""
	left = right = answer = 0

	# set up the sliding window
	for right in range(len(nums)):
		pass

		for right in range(len(nums)):
		# when we hit a "0", decrement k:
		if nums[right] == 0:
			if k == 0:
				if nums[left] == 0:
					k += 1
					left += 1
		answer = max(answer, right - left)

	return answer

	# in each iteration of the loop, answer is the max of right - left, or answer.


nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(longestOnes(nums, k))
