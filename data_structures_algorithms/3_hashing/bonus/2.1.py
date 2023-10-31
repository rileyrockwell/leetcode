from collections import Counter

class Solution:
    def sumOfUnique(self, nums: [int]) -> int:
        # determine the unique elements of nums
        frequency_dic = Counter(nums)
        unique_elements = [i for i in nums if frequency_dic[i] == 1]
        return sum(unique_elements)

nums = [1, 2, 3, 1]
print(Solution().sumOfUnique(nums))