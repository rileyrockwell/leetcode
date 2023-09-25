def findMaxAverage(nums, k):
	"""
	nums: [int]
	k: int
	return: float
	"""
	# find best subarray
	curr = 0

	# left iteration
	for i in range(k):
		# find the average of the left window
		curr += nums[i]

	avg = curr / k

	# right iteration
	for i in range(k, len(nums)):
		# find the average of the right window
		curr += nums[i] - nums[i - k]

	answer = max(avg, curr / k)

	return answer


nums = [1, 12, -5, -6, 50, 3]
k = 4
print(findMaxAverage(nums, k))