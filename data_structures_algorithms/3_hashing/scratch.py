
class Solution:        
    def is_consecutive_increasing(self, subset):
        n = len(subset)
        for i in range(1, n):
            if subset[i] != subset[i-1] + 1:
                return False
        return True

    def findMaxLength(self, arr):
        n = len(arr)
        count = 0

        # Generate all possible subsets
        for i in range(1 << n):
            subset = [arr[j] for j in range(n) if (i & (1 << j)) > 0]

            # Check if the subset is in consecutive increasing order
            if self.is_consecutive_increasing(subset):
                count += 1

        return count


# always start w/ the most basic "case"
arr = [0, 0]

arr = [0, 1]
arr = [1, 0]

arr = [0, 1, 0]
# arr = [1, 0, 1]
# arr = [6, 3 ,4, 8, 10, 5, 7, 1, 9, 2]
# arr = [1, 2, -3, 4, -1, 2, 1, -5, 4]
result = Solution().findMaxLength(arr)
print(result)