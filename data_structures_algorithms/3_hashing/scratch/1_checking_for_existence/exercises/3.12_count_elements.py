class Solution:
    def count_elements(self, arr: list[int]) -> int:
        occurences = 0
        dic = {}

        # build the dictionary
        for num in arr:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1

        keys_list = sorted(list(dic.keys()))

        for index in range(1, len(keys_list)):
            if keys_list[index] - keys_list[index - 1] == 1:
                # if constraint is satisfied and there is a corresponding duplicate value
                if dic[keys_list[index]] == dic[keys_list[index - 1]]:
                    occurences += dic[keys_list[index]]
                # if constraint is satisfied but there is no corresponding duplicate value, use the frequency of x (not x + 1)
                else:
                    occurences += dic[keys_list[index - 1]]

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

nums = [1, 1, 2, 2]
print(Solution().count_elements(nums))

nums = [1, 1, 2]
print(Solution().count_elements(nums))