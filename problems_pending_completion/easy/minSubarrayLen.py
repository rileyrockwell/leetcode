def minSubarrayLen(target, nums):
	# sliding window
	left = curr_sum = counter = 0

	for right in range(len(nums)):
		curr_sum += nums[right]

		counter += 1
		# adjust sliding window bounds if not within constraint
		while curr_sum < target:
			# adjust the window from the left
			counter -= 1
			left += 1
			break

	return counter

nums = list(range(10))
print(minSubarrayLen(5, nums))