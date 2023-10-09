def find_numbers(nums):
	ans = []
	nums = set(nums)

	for num in nums:
		if (num + 1 not in nums) and (num - 1 not in nums):
			ans.append(num)

	return ans

nums = [0, 1, 0, 2, 3, 4]
print(find_numbers(nums))