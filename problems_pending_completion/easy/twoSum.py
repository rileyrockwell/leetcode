def twoSum(nums, target):
	"""
	nums: [int]
	target: int
	return: [int, int]
	"""
	for i in range(len(nums)):
		for j in [k for k in range(len(nums)) if k != i]:
			if nums[i] + nums[j] == target:
				return [i, j]

print(twoSum([2, 7, 11, 15], 9))
print(twoSum([3, 2, 4], 6))
print(twoSum([3, 3], 6))