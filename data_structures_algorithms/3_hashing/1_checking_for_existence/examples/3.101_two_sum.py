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



# 1. culture: friends at work. non-judmental, 
# 2. personalities: ...
# 3. projects: ...
# 4. hybrid: in office TWTh; work 7 days / wk.
# 5. 


# attract the opportunity to you.


# time complexity: ...
# space complexity: ...




a = list(range(6))
b = 8
print(two_sum(a, b))
