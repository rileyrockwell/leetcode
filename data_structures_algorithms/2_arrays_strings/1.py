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