# 100% understanding. 100% certainty.

class Solution:
    def findIndices(self, nums: list[int], indexDifference: int, valueDifference: int) -> list[int]:
    	left = ans = 0
    	for right in range(len(nums)):

    		# implement a counter (but does it necessarily need to be the sum? conceptual > memorization)
    		cur_sum += nums[right]

    		while cur_sum > abs(nums[right] - nums[left]):
    			# something...

    		if right - left > indexDifference:
    			if nums[right] - nums[left] >= valueDifference:
    				return [left, right]
    			left += 1

    	return [-1, -1]


nums = [0, 2, 4, 6]
indexDifference = 2
valueDifference = 4
print(Solution().findIndices(nums, indexDifference, valueDifference))

nums = [5, 1, 4, 1]
indexDifference = 2
valueDifference = 4
print(Solution().findIndices(nums, indexDifference, valueDifference))

nums = [2, 1]
indexDifference = 0
valueDifference = 0
print(Solution().findIndices(nums, indexDifference, valueDifference))

nums = [1, 2, 3]
indexDifference = 2
valueDifference = 4
print(Solution().findIndices(nums, indexDifference, valueDifference))

# notes:
# went well:
# have fun (white claw + instrumental music, zero music w/ lyrics)
# pen + paper, before touching sublime
# clearly defined objective
# zoned-in for 30 min, 5 min BREAK
# strictly instrumental (frequency) music. learn from experience. please.
# SO EXTREMELY PROUD OF YOU. EXCELLENT JOB TONIGHT!