class Solution:
    def missing_number(self, nums: list[int]) -> int:
        # given an array of integers, return the missing integer in the range.

        # temp_set = {i for i in range(len(nums) + 1)}

        # return list(temp_set - set(nums))[0]

        # a = sum(list(range(len(nums) + 1)))

        a = sum(range(len(nums) + 1))

        b = sum(nums)

        return a - b

        # return sum([i for i in range(len(nums) + 1)]) - sum(nums)




nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
print(Solution().missing_number(nums))

nums = [0, 1]
print(Solution().missing_number(nums))

nums = [3, 0, 1]
print(Solution().missing_number(nums))