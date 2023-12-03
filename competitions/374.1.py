from typing import *

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        # find local max (ensure integers to the left and right are less than 'peak' integer)
        result = []

        for i in range(len(mountain) - 2):
            if mountain[i + 1] > mountain[i] and mountain[i + 2] < mountain[i + 1]:
                result.append(i + 1)

        return result

print(Solution().findPeaks([1, 4, 3, 8, 5]))
print(Solution().findPeaks([2, 4, 4]))