class Solution:
    def numSubarraysWithSum(self, nums: [int], goal: int) -> int:
        left = counter = cur_sum = 0

        subarrays = []

        for right in range(len(nums)):
            cur_sum += nums[right]

            while cur_sum >= goal:
                valid = nums[left:right + 1]
                print(valid)
                subarrays.append(valid)
                left += 1
                break


t1 = [1, 0, 1, 0, 1]
t2 = [0, 0, 0, 0, 0]
g1 = 2
g2 = 0

# print(Solution().numSubarraysWithSum(t1, g1))
print(Solution().numSubarraysWithSum(t2, g2))
print("###")