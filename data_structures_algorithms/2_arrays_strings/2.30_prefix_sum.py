# prefix sum

nums = [i for i in range(6)]

def testing_prefix_sum(nums):
	

print(testing_prefix_sum(nums))


# prefix[j] - prefix[i - 1]

# prefix[j] - prefix[i] + nums[i]



# concepts
# pre-processing

def answer_queries(nums, queries, limit):
	# using prefix sum concept
	# O(1)
	prefix = [nums[0]]
	for i in range(1, len(nums)):
		prefix.append(nums[i] + prefix[-1])


	ans = []
	for x, y in queries:
		curr = prefix[y] - prefix[x] + nums[x]
		ans.append(curr < limit)

	return ans


a = [i for i in range(6)]
b = [[0, 3], [1, 4], [2, 5]]
c = 6

print(answer_queries(a, b, c))


def waysToSplitArray(nums):
	prefix = [nums[0]]
	for i in range(1, len(nums)):
		prefix.append(nums[i] + prefix[-1])

	# prefix sum array completed

	# use the prefix sum to determine if splits are valid
	ans = 0
	for i in range(len(nums) - 1):
		# b/c we have prefix[-1] => len(nums) - 1
		left_section = prefix[i]
		right_section = prefix[-1] - prefix[i]
