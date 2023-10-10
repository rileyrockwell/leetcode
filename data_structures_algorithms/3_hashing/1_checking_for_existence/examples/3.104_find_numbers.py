def find_numbers(nums):
	"""
	given an integer array "nums", find all numbers x in nums that satisfy
	the following: x + 1 is not in "nums" and x - 1 is not in "nums".
	"""

	ans = []
	nums = set(nums)

	for num in nums:
		if (num + 1 not in nums) and (num - 1 not in nums):
			ans.append(num)

	return ans


nums = [0, 1, 0, 2, 3, 4]
print(find_numbers(nums))
