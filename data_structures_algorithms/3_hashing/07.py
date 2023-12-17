# semi-copied from GPT
# hashing: counting
# copied from GPT

# PLEASE: GO SLOW AND DO IT RIGHT THE FIRST TIME.

class Solution:
    def countContiguousSubarrays(self, arr):
        n = len(arr)

        # sliding window?

        # assume arr constaint as least 1 element
        counter = 1

        # intitialize left bound on window
        left = 0

        # assumes arr contains at least 1 element
        for right in range(1, n + 1):
            window = arr[left:right]

            print(window)
            for index in range(len(window)):
                # under what conditions is the window not a contiguous subarray?
                if arr[index + 1] <= arr[index]:
                    # break out of the for-loop and build a new window
                    print(window)
                    left += 1
                else:
                    counter += 1


                
        return counter


    def findMaxLength(self, nums):
        m,c=0,0
        d={0:-1}
        for i in range(len(nums)):
            if nums[i]==0:
                c-=1
            else:
                c+=1
            if c in d:
                m=max(m,i-d[c])
            else:
                d[c]=i
        return m


# Example usage

# always start w/ the most basic "case"
arr = [0, 0]

# arr = [0, 1]
# arr = [1, 0]

# arr = [0, 1, 0]
#arr = [0, 1, 1]
# arr = [1, 0, 1]
# arr = [6, 3 ,4, 8, 10, 5, 7, 1, 9, 2]
# arr = [1, 2, -3, 4, -1, 2, 1, -5, 4]
result = Solution().findMaxLength(arr)

print("Number of contiguous subarrays:", result)