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
	# base case, 1 b/c of multiplcation
	if k <= 1:
		return 1

	left = ans = 0
	curr = 0

	# implement sliding window technique
	for right in range(len(nums)):
		# increase current sum by each iteration of the right bound of the sliding window
		curr = curr * nums[right]

		# to ensure sliding window fits the parameter constraints
		while curr >= k:
			# explain...do not move on until understood.
			curr = curr // nums[left]

			# move to a new starting elment for the window
			left += 1

		answer = max(answer, right - left + 1)



def numSubarrayProductLessThanK(nums, k):
	left = answer = 0
	curr = 1 # b/c of multiplication

	for right in range(len(nums)):
		# ideally k < curr
		curr = curr * nums[right]

		# not ideal condition
		while curr >= k:
			# do the opposite of curr = curr * nums[right]
			curr = curr // nums[right]

			# b/c you are not iterating over left
			left += 1

	# right - left + 1: right (ending index of the window), left (starting index of the window), + 1 (b/c range(len(nums)))

	# right - left: e.g. right = 10, left = 3; right - left = 7; + 1 b/c ...
		answer = max(answer, right - left + 1)

	return answer


nums = list(range(6))
k = 3

print(nums)
print(numSubarrayProductLessThanK(nums, k))



def numSubarrayProductLessThanK(nums, k):
	if k <= 1:
		return 0

	left = answer = 0
	curr = 1

	for right in range(len(nums)):
		curr *= curr[right]

		# when the window is broken
		while curr >= k:
			# perform the inverse
			# curr = curr // nums[right]
			curr //= nums[right]

			# redefine the left bound of the sliding window, b/c constraint was broken (while loop)
			left += 1

		# "once we know that the windows is valid, we know that the number of subarrays that end at the current index is right - left + 1"
		answer += right - left + 1

	return answer







"""
if you fix the right bound, the left bound can take any value of the current window.
therefore, the size of the window is the number of valid subarrrays.

