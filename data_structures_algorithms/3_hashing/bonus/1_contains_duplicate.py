class Solution:
	def contains_duplicate(self, nums: [int]) -> bool:
		temp_set = set(nums)

		return len(nums) != len(temp_set)

nums = [1, 2, 3, 1]
print(Solution().contains_duplicate(nums))

nums = [1, 2, 3, 4]
print(Solution().contains_duplicate(nums))

nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
print(Solution().contains_duplicate(nums))