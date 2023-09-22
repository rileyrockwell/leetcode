def some_function(nums, k):
	left = curr = 0
	answer = 0
	right = 0
	for i in range(len(nums)):
		curr += nums[right]

		while curr > k:
			curr -= nums[left]
			left += 1

		answer = max(answer, right - left + 1)

	return answer

print(some_function(list(range(5)), 3))


# add elements from the right
# continue utnil contraint is broken
# remove elements from the left

def find_length(nums, k):
	left = curr = ans = 0
	for right in range(len(nums)):
		curr += nums[right]
		while curr > k:
			curr -= nums[left]
			left += 1

		ans = max(ans, right - left + 1)

	return ans

nums = [3, 1, 2, 7, 4, 2, 1, 1, 5]
k = 8

print(find_length(nums, k))

def find_length(s: str) -> int:
	left = curr = ans = 0
	for right in range(len(s)):
		if s[right] == "0":
			curr += 1

		while curr > 1:
			if s[left] == "0":
				curr -= 1

			left += 1

		ans = max(ans, right - left + 1)

	return ans

print(find_length("11001011"))


def numSubarrayProductLessThankK(nums: [int], k: int) -> int:
	if k <= 1:
		return 0

	ans = left = 0
	curr = 1

	for right in range(len(nums)):
		# explain what 'curr' stands for
		curr = curr * nums[right]
		# k is the maximum product constraint
		while curr >= k:
			# explain why
			curr = curr // nums[left]
			left += 1

		ans += right - left + 1

	return ans


# test case of previous function

def findBestSubarray(nums, k):
	curr = 0
	for i in range(k):
		curr += nums[i]

	ans = curr

	for i in range(k, len(nums)):
		curr = curr + nums[i] - nums[i - k]

		ans = max(ans, curr)

	return ans

nums = [3, -1, 4, 12, -8, 5, 6]
k = 4
print(findBestSubarray(nums, k))

# 4.1
def findBestSubarray(nums, k):
	"""
	nums: [], integer elements
	k: int, size of the window

	return: int, greatest sum of length 4 subarrays
	"""

	curr_sum = 0

	# iterate over the length of the subarray
	for i in range(k):
		curr_sum += nums[i]

	answer = curr_sum

	# iterate over the rest of the subarray windows
	for i in range(k, len(nums)):
		curr_sum = curr_sum + nums[i] - nums[i - k]

		# update the answer at each iteration
		answer = max(answer, curr_sum)

	# once we have gone through all windows, return the answer
	return answer


###

# 1.1
def findLength(nums, k):
	left = curr = ans = 0

	for right in range(len(nums)):

		curr_sum += nums[right]

		while curr_sum > k:

			curr_sum = curr_sum - nums[left]
			left += 1

		answer = max(answer, right - left + 1)

	return answer