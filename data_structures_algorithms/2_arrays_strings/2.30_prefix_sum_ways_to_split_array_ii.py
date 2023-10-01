def waysToSplitArray(nums):
	n = len(nums)

	prefix = [nums[0]]

	for i in range(1, n):
		prefix.append(nums[i] + prefix[-1])

	return prefix

nums = list(range(5))
print(waysToSplitArray(nums))