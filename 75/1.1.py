class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        counter = 0
        return_list = []
        for i in nums:
            counter += i
            return_list.append(counter)

        return return_list