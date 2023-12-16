# Collaborators: Discord

def getAverages(nums, k):
	ans = [-1]*len(nums)

	n = len(nums)

	prefix = [nums[0]]

	# build prefix_sum list
	for i in range(n):
		prefix.append(nums[i] + prefix[-1])

	for i in range(k, n - k):
		left = i - k
		right = i + k

		subarray_sum = prefix[right + 1] - prefix[left]

		subarray_length = 2 * k + 1

		ans[i] = subarray_sum // subarray_length

	return ans

# prefix_list = [7, 11, 14, 23, 24, 32, 37, 39, 45]

# print(prefix_list[6] - 0)
# print(prefix_list[7] - prefix_list[0])
# print(prefix_list[8]- prefix_list[1])

nums = [7, 4, 3, 9, 1, 8, 5, 2, 6]
k = 3
print(getAverages(nums, k))

# keep writing. keep working. keep building. in the booth.