def answer_queries(nums, queries, limit):
	# prefix sum
	prefix = [nums[0]]

	for i in range(1, len(nums)):
		prefix.append(nums[i] + prefix[-1])

	ans = []

	for x, y in queries:
		curr = prefix[y] - prefix[x] + nums[x]
		ans.append(curr < limit)

	return ans

nums = list(range(5))
queries = [[0, 2], [1, 3], [2, 4]]
limit = 9

print(answer_queries(nums, queries, limit))