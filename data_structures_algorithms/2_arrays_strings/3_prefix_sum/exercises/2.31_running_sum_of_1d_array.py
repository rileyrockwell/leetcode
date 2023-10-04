def runningSum(nums):
	
	# apply prefix sum

	n = len(nums)

	prefix = [nums[0]]

	for i in range(1, n):
		prefix.append(nums[i] + prefix[i - 1])

	return prefix

nums = list(range(1, 5))
print(runningSum(nums))

nums = [1]*5
print(runningSum(nums))

nums = [3, 1, 2, 10, 1]
print(runningSum(nums))