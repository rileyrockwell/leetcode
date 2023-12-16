class Solution:
	def repeated_character(self, s: str) -> str:
		# intialize a set
		seen = set()
		for c in s:
			if c in seen:
				return c
			seen.add(c)


s = "xyzabcxyz" # should return s
print(Solution().repeated_character(s))

# time:		O(n)
# space:	...