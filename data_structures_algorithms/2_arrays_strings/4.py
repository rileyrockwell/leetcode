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