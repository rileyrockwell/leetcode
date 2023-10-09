def two_sum(nums, target):
	dic = {}

	for i in range(len(nums)):
		num = nums[i]
		complement = target - num
		if complement in dic:
			return [i, dic[complement]]
		dic[num] = i
	return [-1, -1]

def two_sum(nums, target):
	dic = {}

	for i in range(len(nums)):
		num = nums[i]
		complement = target - num
		if complement in dic:
			return [i, dic[complement]]
		dic[num] = i
	return [-1, -1]


def two_sum(nums, target):
	dic = {}

	for i in range(len(nums)):
		num = nums[i]
		complement = target - num
		if complement in dic:
			return [i, dic[complement]]
		dic[num] = i
	return [-1, -1]


# 41.2
def two_sum(nums, target):
	# using a hashmap (i.e. dictionary)
	dic = {}
	for i in range(len(nums)):
		num = nums[i]
		complement = target - num
		if complement in dic:
			return [i, dic[complement]]

		dic[num] = i

def two_sum(nums, target):
	dic = {}
	for i in range(len(nums)):
		num = nums[i]
		complement = target - num
		if complement in dic:
			return [i, dic[complement]]

		dic[num] = i

class Solution:
	def two_sum(self, nums: list[int], target: int) -> list[int]:
		# intialize the hashmap
		dic = {}

		# loop over the elements of the array
		for i in range(len(nums)):
			# evaluate the current element of the array
			num = nums[i]
			# determine if the num we are evaluating is already in the hashmap
			complement = target - num
			if complement in dic:
				return [i, dic[complement]]

			dic[num] = i

		return [-1, -1]

class Solution:
	def two_sum(self, nums: list[int], target: int) -> list[int]:
		dic = {}

		# iterate over every elment of the array (nums) provided in the parameter
		for i in range(len(nums)):
			# evalute the specific element of the array
			num = nums[i]
			# calculate the complement
			complement = target - num
			# evalute whether the difference if already in the hashmap
			if complement in dic:
				return [i, dic[complement]]

			dic[num] = i

		return [-1, -1]

nums = [5, 2, 7, 10, 3, 9]
target = 8
print(Solution().two_sum(nums, target))



# 1. culture: friends at work. non-judmental, 
# 2. personalities: ...
# 3. projects: ...
# 4. hybrid: in office TWTh; work 7 days / wk.
# 5. training / growth opportunities. desire to stay at organization for at least 5 years?
# 6. upside earnings

# 85/6: most accomplished b/c i enjoyed the process; process was completed with others.

# attract the opportunity to you, by contributing in a stable and strong way.

# time:		...
# space:	...

# 13:10: retention: 0.00
# build something elementary exhibiting an understanding of the concept (e.g. Checking for Existence)
# do not move on until mastered.
# stop w/ the clock; go as slow as possible (so that you don't have to come back)

def two_sum(nums, target):
	# using a hashmap
	dic = {}

	for i in range(len(nums)):
		num = nums[i]

		# what forces you to truly "think": c.s. more than math (at this stage)
		# self-seeking is the opposite direction an engineer moves in.
		# always contributing		