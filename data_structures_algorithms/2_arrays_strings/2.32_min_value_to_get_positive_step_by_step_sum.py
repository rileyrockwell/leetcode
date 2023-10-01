def minStartValue(nums):
	# start w/ an initial positive value

	n = len(nums)

	# if no positive value to begin w/
	prefix = [nums[0]]

	for i in range(1, n):
		prefix.append(nums[i] + prefix[i - 1])

	return prefix


	# find all positive values in nums
	positives = [i for i in nums if i > 0]

	# return positives

	# b/c no specific parameter on which pos element to select, select the first element
	startValue = positives

	# return startValue

nums = [-3, 2, -3, 4, 2]
print(minStartValue(nums))