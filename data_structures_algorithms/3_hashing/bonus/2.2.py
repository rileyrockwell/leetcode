from collections import Counter

class Solution:
    def findLucky(self, arr: [int]) -> int:
        temp_dict = Counter(arr)

        temp_list = []

        for key, value in temp_dict.items():
            if key == value:
                temp_list.append(key)

        if len(temp_list) > 0:
            return max(temp_list)

        return -1
        

arr = [2, 2, 3, 4]
print(Solution().findLucky(arr))

arr = [1, 2, 2, 3, 3, 3]
print(Solution().findLucky(arr))

arr = [2, 2, 2, 3, 3]
print(Solution().findLucky(arr))