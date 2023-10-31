from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        dict_freq = Counter(s)

        return dict_freq

        return_string = ""
        for key, value in temp_list:
            return_string += key * value
    
        return return_string



print(Solution().frequencySort("zraaeayederex"))


# print(Solution().frequencySort("tree"))
# print(Solution().frequencySort("cccaaa"))
# print(Solution().frequencySort("Aabb"))
