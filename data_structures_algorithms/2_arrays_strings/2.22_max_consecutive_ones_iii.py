def longestOnes(nums, k):
	"""
	nums: [int]
	k: int
	return: int
	
	objective: Given a binary array nums and an integer k, return the maximum number of
	consecutive "1" elements in the array if you can flip at most k "0" elements.
	"""
	left = right = answer = 0

	for right in range(len(nums)):
		# when we hit a "0", decrement k:
		if nums[right] == 0:
			if k == 0:
				if nums[left] == 0:
					k += 1
					left += 1
		answer = max(answer, right - left)

	return answer

	# in each iteration of the loop, answer is the max of right - left, or answer.

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(longestOnes(nums, k))

# you could have been doing this at age 10. pick people that pick you. don't force things. let things unfold naturally.
# let the unvierse drive and do 50% of the work. you still need to do the other 50% of the work.