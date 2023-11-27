class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
    	jewels = list(jewels)

    	counter = 0
    	for element in stones:
    		if element in jewels:
    			counter += 1

    	return counter

jewels = "aA"
stones = "aAAbbbb"


jewels = "z"
stones = "ZZ"

print(Solution().numJewelsInStones(jewels, stones))


