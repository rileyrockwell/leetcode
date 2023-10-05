def find_length(nums, k):
	# objective: find longest subarray (window) with sum less than or equal to k
	left = curr = answer = 0

	for right in range(len(nums)):
		curr += nums[right]

		# if window is invalid
		while curr > k:
			# shorten the window from the left bound, to get a sum less than k (satisfy the constraint)
			curr -= nums[left]

			# increase the left bound of the window 'manually'
			left += 1

		# update the return value for each iteration, where 'right - left + 1' is the 
		answer = max(answer, right - left + 1)

	return answer

def find_length(nums, k):
	# objective: find the longest subarray with sum less than or equal to k

	left = curr = answer = 0

	for right in range(len(nums)):
		curr += nums[right]

		# window broken (does not satisfy constraint)
		while curr > k:
			curr -= nums[left]
			left += 1

		# update answer for each iteration, where 'right - left + 1' is the length of the window
		answer = max(answer, right - left + 1)

	return answer

def find_length(nums, k):
	left = curr = answer = 0

	for right in range(len(nums)):
		curr += nums[right]

		while curr > k:
			curr -= nums[left]
			left += 1

		answer = max(answer, right - left + 1)

	return answer

def find_length(nums, k):
	left = curr = answer = 0

	for right in range(len(nums)):
		# sum all elements of the subarray such the sum (curr) is less than or equal to k
		curr += nums[right]

		while curr > k:
			# 'pop off' the left element
			curr -= nums[left]

			# increase the left bound 'manually'
			left += 1

		# note: 'curr' is a variable to determine length; 'curr' is not part of the answer b/c we are determining length
		# note: right - left + 1: length of the window b/c when counting inclusive elements we always add 1 (e.g. range = max - min + 1)
		answer = max(answer, right - left + 1)

	return answer


def find_length(nums, k):
	# objective: find longest subarray (window) with sum less than or equal to k
	left = curr = answer = 0

	for right in range(len(nums)):
		curr += nums[right]

		# if window is invalid
		while curr > k:
			# shorten the window from the left bound, to get a sum less than k (satisfy the constraint)
			curr -= nums[left]

			# increase the left bound of the window 'manually'
			left += 1

		# update the return value for each iteration, where 'right - left + 1' is the 
		answer = max(answer, right - left + 1)

	return answer

def find_length(nums, k):
	# objective: find the longest subarray with sum less than or equal to k

	left = curr = answer = 0

	for right in range(len(nums)):
		curr += nums[right]

		# window broken (does not satisfy constraint)
		while curr > k:
			curr -= nums[left]
			left += 1

		# update answer for each iteration, where 'right - left + 1' is the length of the window
		answer = max(answer, right - left + 1)

	return answer

def find_length(nums, k):
	left = curr = answer = 0

	for right in range(len(nums)):
		curr += nums[right]

		while curr > k:
			curr -= nums[left]
			left += 1

		answer = max(answer, right - left + 1)

	return answer
	

def find_length(nums, k):
	left = curr = answer = 0

	for right in range(len(nums)):
		# sum all elements of the subarray such the sum (curr) is less than or equal to k
		curr += nums[right]

		while curr > k:
			# 'pop off' the left element
			curr -= nums[left]

			# increase the left bound 'manually'
			left += 1

		# note: 'curr' is a variable to determine length; 'curr' is not part of the answer b/c we are determining length
		# note: right - left + 1: length of the window b/c when counting inclusive elements we always add 1 (e.g. range = max - min + 1)
		answer = max(answer, right - left + 1)

	return answer

def find_length(nums, k):
	left = curr = answer = 0

	for right in range(len(nums)):
		curr += nums[right]

		while curr > k:
			curr -= nums[left]
			left += 1

		answer = max(answer, right - left + 1)

	return answer
