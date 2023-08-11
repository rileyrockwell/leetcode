class Solution:
    def search(self, nums: [int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1



nums = [-1,0,3,5,9,12]
target = 9
print(Solution().search(nums, target))

nums = [-1,0,3,5,9,12]
target = 2
print(Solution().search(nums, target))