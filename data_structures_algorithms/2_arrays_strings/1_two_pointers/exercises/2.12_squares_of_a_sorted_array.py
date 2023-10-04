def sortedSquares(nums):
	"""
	nums: [int]
	return: [int]
	
	constraints:
	1 <= nums.length <= 10**4
	-10**4 <= nums[i] <= 10**4
	nums is sorted in non-decreasing order

	time complexity: O(n)
	"""
	# you must use the two pointers method
	left = 0
	right = len(nums) - 1

	# work for a len(nums) % 2 == 0
	while left <= right:
		if left < right:
			nums[left] = nums[left]**2
			nums[right] = nums[right]**2
		else:
			nums[left] = nums[right]**2

		left += 1
		right -= 1

	return sorted(nums)


nums = [-4, -1, 3, 3, 10]
print(sortedSquares(nums))
nums = [-7, -3, 2, 3, 11]
print(sortedSquares(nums))

nums = [4]
print(sortedSquares(nums))

nums = [0, -1, -2, 3]
print(sortedSquares(nums))