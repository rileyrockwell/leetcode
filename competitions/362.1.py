def numberOfPoints(nums):
	"""
	nums: [[int]]
	return: int
	"""

	# keep track of the integers that have cars "ontop"
	return_set = set()

	# use a set to keep track of membership
	for pair in nums:
		temp_list = [i for i in range(pair[0], pair[1] + 1)]
		
		return_set = return_set.union(temp_list)

	# if each integer is associated with 1 point
	return len(return_set)


nums = [[3,6],[1,5],[4,7]]
print(numberOfPoints(nums))

nums = [[1, 3], [5, 8]]
print(numberOfPoints(nums))

nums = [[0, 3], [2, 3]]
print(numberOfPoints(nums))

nums = [[0, 1], [3, 4]]
print(numberOfPoints(nums))
