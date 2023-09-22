def find_best_subarray(nums, k):
	curr_sum = 0
	for i in range(k):
		curr_sum += nums[i]

	answer = curr_sum

	for i in range(k, len(nums)):
		curr_sum += nums[i] - nums[i - k]
		answer = max(answer, curr_sum)

	return answer

print(list(range(6)))
print(find_best_subarray(list(range(6)), 4))

# example functions
def find_length(nums, k):
	# use sliding window technique
	left = curr = ans = 0

	for right in range(len(nums)):
		curr += nums[right]

		while curr > k:
			curr -= nums[left]
			left += 1

		ans = max(ans, right - left + 1)

	return ans


def find_length1(s):
	# how to set up the sliding window?
	# do the video explanations do anything for you?
	# least effecitve (greatest time suck): reading
	# most effective: learning w/ other people
	# 
	pass


def numSubarrayProductLessThanK(nums, k):
	return 1

def find_best_subarray(nums, k):
	return 1

#		time complexity			space complexity
# (1).	...						...
# (2).	...						...
# (3).  ...						...
# (4).  ...						...



### 9.20: 02:45 ###

# ex 1
def find_length(nums, k):
	left = curr_sum = ans = 0
	for right in range(len(nums)):
		curr_sum += nums[right]
		while curr_sum > k:
			curr_sum -= nums[left]
			left += 1
		ans = max(ans, right - left + 1)

	return ans



"""
do not move on until mastered. one step at a time. but broski: have fun along the way. it's okay to have fun while you are working.
be of service and make an effort to cotnribute more than you consume. it brings far more mental wellbeing.
"""


### 9.20: 09:00 ###
def find_length(nums, k):
	left = curr_sum = answer = 0

	# k: length of the sliding window?
	for right in range(len(nums)):
		curr_sum += nums[right]
		
		# ideally we stay at curr_sum <= k; if not reduce the size of the sliding window from the left
		while curr_sum > k:
			curr_sum -= nums[left]
			left += 1

			answer = max(answer, right - left + 1)

	return answer


def find_length(nums, k):
	# return: length of the longest subarray whose sum is less than or equal to k

	left = curr_sum = answer = 0

	for right in range(len(nums)):
		curr_sum += nums[right]

		# ideally curr_sum is <= k, in which case nums does not have any negative integers?
		while curr_sum > k:
			curr_sum -= nums[left]
			left += 1

		answer = max(answer, right - left + 1)

	return answer


def find_lengths(nums, k):
	left = curr_sum = answer = 0

	for right in range(len(nums)):
		curr_sum += nums[right]

		# if current sliding window sums to an integer larger than k, reduce the size of the sliding window from the left?
		while curr_sum > k:
			curr_sum -= nums[left]
			left -= 1

		answer = max(answer, right - left + 1)

	return answer

def find_length(nums, k):
	left = curr_sum = answer = 0

	for right in range(len(nums)):
		curr_sum += nums[right]

		while curr_sum > k:
			# reduce the size of the sliding window from the left, so that the sum stays under the upper bound, k
			curr_sum -= nums[left]
			left += 1

		# length > sum | of nums
		print(answer, right - left + 1)

		answer = max(answer, right - left + 1)

	return answer


nums = list(range(10))
k = 7
print(find_length(nums, k))


### 9.20 | 11:37 ###
def find_length(s):
	left = curr_sum = answer = 0
	for right in range(len(s)):
		pass

### 9.20 | 16:24 ###
def find_length(s):
	pass

### 9.20 | 17:06 ###
def find_best_subarray(nums, k):
	curr_sum = 0
	for i in range(k):
		curr_sum += nums[i]

	answer = curr_sum
	for i in range(k, len(nums)):
		curr_sum += nums[i] - nums[i - k]
		answer = max(answer, curr_sum)

	return answer

print("###")

nums = list(range(6))
k = 3
print(find_best_subarray(nums, k))