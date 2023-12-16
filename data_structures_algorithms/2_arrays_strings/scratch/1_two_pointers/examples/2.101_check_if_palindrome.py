def check_if_palindrome(s):
	left = 0

	right = len(s) - 1

	while left < right:
		if s[left] != s[right]:
			return False

		left += 1
		right -= 1

	return True

print(check_if_palindrome("hannah"))
print(check_if_palindrome("hanna"))
print(check_if_palindrome("anna"))

# Time:		O(x)	0.48
# Space:	O(x)	0.92