def minStartValue(nums):
	# start w/ an initial positive value

	n = len(nums)

	# if no positive value to begin w/
	prefix = [nums[0]]

	for i in range(1, n):
		prefix.append(nums[i] + prefix[i - 1])

	return prefix


	# find all positive values in nums
	positives = [i for i in nums if i > 0]

	# return positives

	# b/c no specific parameter on which pos element to select, select the first element
	startValue = positives

	# return startValue

def min_start_value(nums):
	"""
	return: minimum positive value of startValue, s.t. that step-by-step sum is never less than 1
	
	hint: find the minimum prefix sum
	"""
	n = len(nums)

	# prefix sum

	ans = 0
	cur_sum = 0

	for right in range(n):
		cur_sum += nums[right]
		ans = min(ans, cur_sum)

	return -ans + 1

nums = [i for i in range(6)]
print("expected: [0, 1, 3, 6, 10, 15]")
print("returned:", minStartValue(nums))


nums = [-3, 2, -3, 4, 2]
print(min_start_value(nums))

nums = [1, 2]
print(min_start_value(nums))

nums = [1, -2, -3]
print(min_start_value(nums))

### provided solution ###

# class Solution:
#     def minStartValue(self, nums: List[int]) -> int:
#         # Let n be the length of the array "nums", m be the absolute value 
#         # of the lower boundary of the element. In this question we have m = 100.
#         n = len(nums)
#         m = 100

#         # Set left and right boundaries according to left = 1, right = m * n + 1.
#         left = 1
#         right = m * n + 1

#         while left < right:
#             # Get the middle index "middle" of the two boundaries, let the start value 
#             # be "middle". The initial step-by-step total "total" equals to middle as well.
#             # Use boolean parameter "is_valid" to record whether the total 
#             # is greater than or equal to 1.
#             middle = (left + right) // 2
#             total = middle
#             is_valid = True

#             # Iterate over the array "nums".
#             for num in nums:

#                 # In each iteration, calculate "total" plus the element "num" in the array.
#                 total += num

#                 # If "total" is less than 1, we shall try a larger start value,
#                 # we mark "is_valid" as "false" and break the current iteration.
#                 if total < 1:
#                     is_valid = False
#                     break

#             # Check if middle is valid, and reduce the search space by half.
#             if is_valid: 
#                 right = middle
#             else:
#                 left = middle + 1

#         # When the left and right boundaries coincide, we have found
#         # the target value, that is, the minimum valid startValue.
#         return left

# class Solution:
#     def minStartValue(self, nums: List[int]) -> int:
#         # We use "total" for current step-by-step total, "min_val" for minimum 
#         # step-by-step total among all sums. Since we always start with 
#         # startValue = 0, therefore the initial current step-by-step total is 0, 
#         # thus we set "total" and "min_val" be 0. 
#         min_val = 0
#         total = 0

#         # Iterate over the array and get the minimum step-by-step total.
#         for num in nums:
#             total += num
#             min_val = min(min_val, total)

#         # We have to change the minimum step-by-step total to 1, 
#         # by increasing the startValue from 0 to -min_val + 1, 
#         # which is just the minimum startValue we want.
#         return -min_val + 1

