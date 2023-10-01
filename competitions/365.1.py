def mtv(nums):
	# value of a triplet != sum(i, j, k)

	# value of a triplet == (nums[i] - nums[j]) * nums[k]
	temp_list = []

	total = 0
	for index in range(2, len(nums)):
		i = index - 2
		j = index - 1
		k = index
		temp_list.append((nums[i] - nums[j]) * nums[k])

	counter = 0
	for i in temp_list:
		if i < 0:
			counter += 1

	if counter == len(temp_list):
		return 0

	return temp_list


nums = [12, 6, 1, 2, 7]
print(mtv(nums))

# ALWAYS FOLLOW THE CLOCK ON THE SECOND HAND.