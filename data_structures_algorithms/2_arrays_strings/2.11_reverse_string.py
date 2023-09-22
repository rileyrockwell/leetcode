def reverseString(s):
	"""
	s: list(str)
	return: None

	Do not return anything, modify s in-place instead.
	
	Write a function that reverses a string. The input string is given as an array of
	characters 's'. You must do this by modifying the input array in-place with O(1)
	extra memory.

	"""
	# use the concepts presented; do not move on until mastered
	left = 0
	right = len(s) - 1

	while left < len(s) - 1:
		temp_element = s[left]

		s[left] = s[right]

		s[right] = temp_element

		left += 1
		right -= 1

	return s




print(reverseString(["a", "b"]))
print(reverseString(["b", "a"]))

print(reverseString(["h", "a", "n", "n", "a", "h"]))

print(reverseString(["a", "b", "c"]))