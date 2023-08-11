# 6316. Rearrange Array to Maximize Prefix Score
'''
nums = [2,-1,0,1,-3,3,-3]

objective: rearrange nums in whatever order the user determines: nums = [...]

constraints:
1 <= nums.length <= 105
-106 <= nums[i] <= 106
'''

nums = [2,-1,0,1,-3,3,-3]

def rearrange(nums):
    pass

def prefix(rearranged_nums):
    # i-th sum equals the 0 to i-th element of rearranged_nums, using recurrsion?
    new_list = []
    ith_sum = 0
    # base case
    for i in range(len(rearranged_nums)):    
        # base case
        if i == 0:
            ith_sum = i
            new_list.append(ith_sum)
        # recursive case
        else:
            ith_sum = rearranged_nums[i] + prefix(rearranged_nums[:i-1])
            new_list.append(ith_sum)

    return new_list

print(prefix(nums))