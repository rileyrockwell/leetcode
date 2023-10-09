class Solution:
	def repeated_character(self, s: str) -> str:
		"""
		given a string "s", return the first character to appear twice.
		it is guarenteed that the input will have a duplicate character.
		"""
		for i in range(len(s)):
			# evalute the individual element of s
			c = s[i]
			# loop over all element sup to the i-1 index
			for j in range(i):
				# [explanation]
				if s[j] == c:
					# [explanation]
					return c

		return ""

s = "xyzabcxyz"
print(Solution().repeated_character(s))


# time:		O(n**2)
# space:	