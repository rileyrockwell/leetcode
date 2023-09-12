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
	##
	# square the elements of the entire array; sort the entire array
	# squares = [i**2 for i in nums]
	# squares.sort()

	# return squares

	##
	# note: i**2 will increase runtime
	squares = [i*i for i in nums]
	squares.sort()

	return squares

	##
	# note: b/c data structure is a list, call sorted on the list comprehension
	# return sorted([i*i for i in nums])



nums = [-7, -3, 2, 3, 11]
print(sortedSquares(nums))
nums = [-4, -1, 0, 3, 10]
print(sortedSquares(nums))