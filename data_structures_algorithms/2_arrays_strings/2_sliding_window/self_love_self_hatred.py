# 1. find_length(nums, k)
def find_length_nums(nums, k):
	left = curr = answer = 0

	for right in range(len(nums)):
		curr += nums[right]

		while curr > k:
			curr -= nums[left]
			left += 1

		answer = max(answer, right - left + 1)

	return answer


print(find_length_nums([4, 2, 3], 3))


# 2. find_length(s)
def find_length(s):
	left = curr = answer = 0
	
	for right in range(len(s)):
		if s[right] == "0":
			curr += 1

		while curr > 1:
			if s[left] == "0":
				curr -= 1
			left += 1

		answer = max(answer, right - left + 1)

	return answer


# 3. numSubarrayProductLessThanK(nums, k)
def numSubarrayProductLessThanK(nums, k):
	if k <= 1:
		return 1

	answer = left = 0
	curr = 1

	for right in range(len(nums)):
		curr *= nums[right]
		while curr >= k:
			curr //= nums[left]
			left += 1
		answer += right - left + 1

	return answer


# 4. find_best_subarray(nums, k):
def find_best_subarray(nums, k):
	curr = 0
	for i in range(k):
		curr += nums[i]

	answer = curr
	for i in range(k, len(nums)):
		curr += nums[i] - nums[i - k]
		answer = max(answer, curr)

	return answer

###
print(find_length_nums([0, 1, 2, 3], 4))
print(find_length("11001011"))
print(numSubarrayProductLessThanK([2, 4], 8))
print(find_best_subarray([0, 1, 2, 3], 4))


### 
# (1). O(n) | O(1)
# objective: find the length of the longest substring (window) with sum is <= k.

# (2). O(n) | O(1)
# objective: find the longest subarray of at most one "0" element. (b/c we can flip at most one "0" to a "1").

# (3). O(n) | O(1)
# objective: find the number of subarrays s.t. the product of the elements in the subarray is < k.

# (4). O(n) | O(1)
# objective: find the subarray with the largest sum whose length == k.

### 	10:30		11:30		12:00
# (1). 	0.35		0.60
# (2). 	0.20		...
# (3). 	0.20		...
# (4). 	0.10		...