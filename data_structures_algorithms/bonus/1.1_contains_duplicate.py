class Solution:
    def containsDuplicate(self, nums: [int]) -> bool:
        #if duplicate, return True
        return len(nums) != len(set(nums))

nums = [1, 2, 3, 1]
print(Solution().containsDuplicate(nums))

nums = list(range(1, 5))
print(Solution().containsDuplicate(nums))

nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
print(Solution().containsDuplicate(nums))