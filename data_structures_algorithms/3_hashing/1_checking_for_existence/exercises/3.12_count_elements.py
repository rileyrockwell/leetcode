class Solution:
    def count_elements(self, arr: list[int]) -> int:
        # x + 1 is also in array
        # set of dictionary?
        # map integer to frequecy of integer
        # determine if, given integer, integer + 1 also exists.
        dic = {}
        occurences = 0

        # map, lambda

        for num in arr:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1

        # recall: sorted return a list of all key values in numeric order

        list_keys = sorted(dic)

        # return list_keys
    
        for i in range(1, len(list_keys)):
            # if, given x in arr, x + 1 is also in arr
            if list_keys[i] - list_keys[i - 1] == 1:
                occurences += 1

        return occurences



nums = [1, 2, 3]
print(Solution().count_elements(nums))


nums = [1, 1, 3, 3, 5, 5, 7, 7]
print(Solution().count_elements(nums))

nums = [1,3,2,3,5,0]
print(Solution().count_elements(nums))

nums = [1, 1, 2, 2]
print(Solution().count_elements(nums))

nums = [1, 1, 2, 2, 3, 3]
print(Solution().count_elements(nums))