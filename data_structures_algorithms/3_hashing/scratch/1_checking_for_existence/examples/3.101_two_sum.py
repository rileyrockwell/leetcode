class Solution:
	def two_sum(self, nums: [int], target: int) -> [int]:
		dic = {}

		for i in range(len(nums)):
			num = nums[i]
			complement = target - num
			if complement in dic:
				return [i, dic[complement]]

			# else: put the current element (i) in the hashmap and move on to future elements
			dic[num] = i

		# if no two elements of nums sum to target, return [-1, -1]
		return [-1, -1]

nums = [0, 1, 2, 3, 2, 1, 0]
nums = [1, 2, 4
, 2]
target = 4
print(Solution().two_sum(nums, target))