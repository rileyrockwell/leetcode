def reverseString(s):
	"""
	mutate the parameter; modify the input array in place
	do not copy parameter b/c it violates the O(1) extra memory contraint
	"""

	left = 0
	right = len(s) - 1

	while left < right:
		temp_element = s[left]

		s[left] = s[right]

		s[right] = temp_element

		left += 1
		right -= 1

	return s


s = ["a", "b", "c", "d", "e"]
# s = ["a", "b", "c"]
# s = ["a", "b", "c", "d"]

print(reverseString(s))
