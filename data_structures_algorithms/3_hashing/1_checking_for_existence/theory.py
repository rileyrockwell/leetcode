def find_numbers(nums):
	ans = []

	nums = set(nums)

	for element in nums:
		if (element + 1 not in nums) and (element - 1 not in nums):
			ans.append(element)

	return ans


nums = [0, 1, 3, 5, 7, 5]
print(find_numbers(nums))