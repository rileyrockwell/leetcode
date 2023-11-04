import math

class Solution:
    def combination(self, n, r):
        if n >= r:
            return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))
        return 0

    def numIdenticalPairs(self, nums: [int]) -> int:
        # Create a dictionary where keys are unique integers and values are lists of their indices
        # *COPIED FROM GPT*
        dic = {value: [i for i, x in enumerate(nums) if x == value] for value in set(nums)}

        return list(dic.values())

        # set up a combination to determine the numebr of ways to order the values
        counter = 0
        for index_array in dic.values():
            counter += self.combination(len(index_array), 2)

        return int(counter)



t1 = [1, 2, 3, 1, 1, 3]
t2 = [1, 1, 1, 1]
t3 = [1, 2, 3]

for nums in [t1, t2, t3]:
    print(Solution().numIdenticalPairs(nums))