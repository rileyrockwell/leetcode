class Solution:
    def sumOfUnique(self, nums: [int]) -> int:
        dic = {}

        # build the dictionary
        for i in nums:
            dic[i] = len(list(x for x in nums if x == i))

        # evaluate the sum of the unique integers
        counter = 0
        for key, value in dic.items():
            if value == 1:
                counter += key

        return counter


nums = [1, 2, 3, 1]
print(Solution().sumOfUnique(nums))