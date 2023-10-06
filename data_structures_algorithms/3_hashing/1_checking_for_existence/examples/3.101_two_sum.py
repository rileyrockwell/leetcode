def two_sum(nums, target):
	dic = {}

	for i in range(len(nums)):
		num = nums[i]
		complement = target - num
		if complement in dic:
			return [i, dic[complement]]
		dic[num] = i
	return [-1, -1]

# 0.05

def two_sum(nums, target):
	dic = {}

	for i in range(len(nums)):
		num = nums[i]
		complement = target - num
		if complement in dic:
			return [i, dic[complement]]
		dic[num] = i

	return [-1, -1]

# 0.05

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



# time complexity: ...
# space complexity: ...




a = list(range(6))
b = 8
print(two_sum(a, b))