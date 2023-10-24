class Solution:
    def largest_unique_number(self, nums: [int]) -> int:
        """
        return: largest int in nums that occurs only once.
        """
        # build dictionary (int: frequency)
        dic = {}
        temp_array = []

        for element in nums:
            dic[element] = len([i for i in nums if i == element])

        for key in dic.keys():
            if dic[key] == 1:
                temp_array.append(key)

        if len(temp_array) > 1:
            return max(temp_array)

        return -1

    def largest_unique_number(self, nums: [int]) -> int:
        return 1


nums = [5, 7, 3, 9, 4, 9, 8, 3, 1]
print(Solution().largest_unique_number(nums))

nums = [9, 9, 8, 8]
print(Solution().largest_unique_number(nums))