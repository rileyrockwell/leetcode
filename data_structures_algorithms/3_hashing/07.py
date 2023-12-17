from typing import *

class Solution:
    def findMaxLength(self, arr: List[int]) -> int:
        n = len(arr)
        answer = n
        
        for start in range(n):
            for end in range(start, n):
                # build each individual subarray (including the trivial subarray)
                subarray = arr[start:end + 1]
                # for visualization: print(subarray)
                answer += 1

        return answer


nums = list(range(6))
print(Solution().findMaxLength(nums))