def repeated_character(s):
	# initialize the hashmap
	seen = set()

	for char in s:
		if char in seen:
			return char
		seen.add(char)

	return "no repeated characters"

print(repeated_character("testing"))
print(repeated_character("tesing"))

# time:		O(1) b/c of set
# space:	...


def find_numbers(nums):
	ans = []
	nums = set(nums)

	for element in nums:
		if (element + 1 not in nums) and (element - 1 not in nums):
			ans.append(element)

	return ans




nums = [0]
nums1 = [0, 1]
nums2 = [1, 0, 1]

nums = [1, 1]
nums1 = [1, 1, 0]
nums2 = [0, 1, 1]

nums = list(range(6))
nums1 = [5]*5
nums2 = [i for i in range(10) if i % 2 == 0]


# i have not been this energized since 5th grade.

print(find_numbers(nums))
print(find_numbers(nums1))
print(find_numbers(nums2))

# objective: construct the problem statement for find_numbers