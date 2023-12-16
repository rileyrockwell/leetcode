class Solution:
	def numJewelsInStones(self, jewels: str, stones: str) -> int:
		# for each stone, check if it is a jewel
		count = 0
		for stone in list(stones):
			if stone in list(jewels):
				count += 1

		return count


jewels = "aA"
stones = "aAAbbbb"
print(Solution().numJewelsInStones(jewels, stones))

jewels = "z"
stones = "ZZ"
print(Solution().numJewelsInStones(jewels, stones))