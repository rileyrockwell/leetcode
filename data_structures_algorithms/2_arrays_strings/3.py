def numSubarrayProductLessThanK(nums, k):
	if k <= 1:
		return 0

	answer = left = 0
	curr_sum = 1

	for right in range(len(nums)):
		curr_sum *= nums[right]

		while curr_sum >= k:
			curr_sum //= nums[left]
			left += 1

		answer += right - left + 1

	return answer

k = 2
nums = [i for i in range(6)]
print("nums:", nums)
print("k:", k)
print("print all subarrays...")
print(numSubarrayProductLessThanK(nums, k))


def numSubarrayProductLessThanK(nums, k):
	left = curr_sum = answer = 0

	for right in range(len(nums)):

		# number of subarray products less than k?
		curr_sum = curr_sum * nums[right]

		while curr_sum > k:
			curr_sum = curr_sum // nums[left]
			left += 1

		answer += right - left + 1

	return answer


print(list(range(10)))
print(numSubarrayProductLessThanK(list(range(10)), 3))


def numSubarrayProductLessThanK(nums, int):
	if k <= 1:
		return 0

	ans = left = 0
	# b/c multiplication
	curr = 1

	for right in range(len(nums)):
		curr = curr * nums[right]
		while curr >= k:
			curr = curr // nums[left]
			left += 1

		ans = ans + right - left + 1

	return ans



def numSubarrayProductLessThanK(nums, k):
	pass