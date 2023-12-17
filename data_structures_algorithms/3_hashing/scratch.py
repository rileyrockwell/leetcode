# semi-copied from GPT
# hashing: counting

class Solution:
    def countContiguousSubarrays(self, arr):
        n = len(arr)
        counter = 0

        # build individual subarrays (omiting the trivial subset / subarray)
        # note: upper bound is len(arr) b/c range is 0-indexed and list[i] is 0-indexed for retrieval
        for index in range(1, n + 1):
            # build a new subarray for each iteration
            subarray = arr[:index]
            k = len(subarray)

            print("index:", index, ";", "subarray:", subarray)
            print(subarray, k)
            
            a = sorted(subarray)
            if subarray == a:
                counter += 1

        return counter


# Example usage
arr = [0, 1]
arr = [0, 1, 0]
arr = [6, 3 ,4, 8, 10, 5, 7, 1, 9, 2]
# arr = [1, 2, -3, 4, -1, 2, 1, -5, 4]
result = Solution().countContiguousSubarrays(arr)

print("Number of contiguous subarrays:", result)