# semi-copied from GPT
# hashing: counting
# copied from GPT

class Solution:
    def countContiguousSubarrays(self, arr):
        n = len(arr)
        counter = 0

        # sliding window...
        valid_subarray = 0

        left = 0


        for right in range(1, n + 1):
            window = arr[:right]

            # determine if integers of window are in consecutive increasing order
            for index in range(len(window)):
                if arr[i] <= arr[i - 1]:
                # if s_n <= s_n-1, forget about that window; break and redefine the window
                    break
                else:
                    valid_subarray += 1

            # under what conditions will left increasing by 1?
            left += 1


# Example usage

# always start w/ the most basic "case"
arr = [0, 0]

# arr = [0, 1]
# arr = [0, 1, 0]
# arr = [6, 3 ,4, 8, 10, 5, 7, 1, 9, 2]
arr = [1, 2, -3, 4, -1, 2, 1, -5, 4]
result = Solution().countContiguousSubarrays(arr)

print("Number of contiguous subarrays:", result)