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


def find_length(nums, k):
	left = curr_sum = answer = 0

	for right in range(len(nums)):
		curr_sum += nums[right]

		# ideally curr_sum <= k; make adjustments to the sliding window if this is not the case
		while curr_sum > k:
			curr_sum -= nums[left]
			left += 1

		answer = max(answer, right - left + 1)

	return answer

print(list(range(6)))
print(find_length(list(range(6)), 6))

def find_length(nums, k):
	left = curr_sum = answer = 0

	for right in range(len(nums)):
		while curr_sum > k:
			curr_sum -= 1

###

def find_length(s):
	left = curr_sum = answer = 0

	for right in range(len(s)):
		if s[right] == "0":
			curr_sum += 1

		while curr_sum > 1:
			if s[left] == "0":
				curr_sum -= 1
			left += 1

		answer = max(answer, right - left + 1)

	return answer

print(find_length("11110110"))


def find_length(s):
	left = curr_sum = answer = 0
	for right in range(len(s)):
		if s[right] == "0":
			curr_sum += 1

		while curr_sum > 1:
			if s[left] == "0":
				curr_sum -= 1

			left += 1

		answer = max(answer, right - left + 1)

	return answer


def find_length(s):
	# using the sliding window techinque
	# notice, the only thing that has changes is the data structure (string rather than list)
	# q: what is the objective? what are we find the length with respect to? what are the constraints?

	"""
	Objective: You may choose up to one "1" and flip it to a "0". What is the length of the longest substring
	achievable that contains only "1"?

	Objective B/c you can flip one "0" to a "1", what is the longest substring that contains at most one "0".
	"""

	left = answer = curr_sum = 0

	for right in range(len(s)):
		# explain...
		if s[right] == "0":
			# turn on the dumby variable
			curr_sum += 1

			while curr_sum > 1:
				# explain...
				if s[left] == "0":
					# turn off the dumby variable
					curr_sum -= 1

				# b/c left is not iterating
				left += 1

			# recall: answer = 0, to begin with
			# right - left + 1: right b/c ...; left b/c ...; + 1 b/c range(len(s))?
			answer = max(answer, right - left + 1)

	return curr_sum
print(find_length("00110100"))



def find_length1(s):
	left = curr = answer = 0

	for right in range(len(s)):
		if s[right] == "0":
			# activate binary variable b/c we can flip from "0" to "1"
			curr += 1

		# if the binary variable is activated, ensure that the element
		# to the left of the frist identified "0" is not another "0"
		while curr > 1:
			if s[left] == "0":
				# indicate that the length of the "examined" subarray
				# is no longer the maximum subarray
				curr -= 1 
				# b/c we are not iterating
			left += 1

			# explain: right - left + 1
			answer = max(answer, right - left + 1)

	return answer

s = "00110100"
print("###")
print(find_length1(s))

# objective: find the longest substring that contains at most one "0"


###

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


###

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