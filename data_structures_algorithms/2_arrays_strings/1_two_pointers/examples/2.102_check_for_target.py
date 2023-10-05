def check_for_target(nums, target):
	left = 0
	right = len(nums)

	while left < right:
		curr_sum = nums[left] + nums[right]

		if curr_sum == target:
			return True

		if curr_sum > target:
			right -= 1
		else:
			left += 1

	return False