def numberOfPoints(nums):

	return_set = set()

	for pair in nums:
		temp_list = [i for i in range(pair[0], pair[1] + 1)]
		return_set = return_set.union(temp_list)
		
	return len(return_set)

nums = [[0, 2], [1, 3], [3, 4]]
print(numberOfPoints(nums))

nums = [[0, 4], [1, 4]]
print(numberOfPoints(nums))