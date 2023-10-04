# Collaborator: Alan.

def findMaxAverage(nums, k):
	"""
	nums: [int]
	k: int
	return: float

	objective: Find a contiguous subarray whose length is equal to k that 
	has the maximum average value and return this value.
	"""
	curr = 0

	# left iteration
	for i in range(k):
		# find average value of all elements up to k
		curr += nums[i]

	ans = curr

	# right iteration
	for i in range(k, len(nums)):
		curr += nums[i] - nums[i - k]
		ans = max(ans, curr)

	return ans / k

nums = [1, 12, -5, -6, 50, 3]
k = 4
print(findMaxAverage(nums, k))

nums = [0, 2, 4, 6]
k = 3
print(findMaxAverage(nums, k))