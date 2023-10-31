from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        dict_freq = Counter(s)

        

print(Solution().frequencySort("tree"))
print(Solution().frequencySort("cccaaa"))
print(Solution().frequencySort("Aabb"))