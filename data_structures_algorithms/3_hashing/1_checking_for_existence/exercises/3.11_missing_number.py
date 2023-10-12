class Solution:
    def missing_number(self, nums: list[int]) -> int:
        # given an array of integers, return the missing integer in the range.
        a = len(nums)
        b = [num for num in nums]

        for num in range(a + 1):
            if num not in b:
                return num




        

        








nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
print(Solution().missing_number(nums))

nums = [0, 1]
print(Solution().missing_number(nums))

nums = [3, 0, 1]
print(Solution().missing_number(nums))