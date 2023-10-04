nums = list(range(4))

def answer_queries(nums, queries, limit):
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])

    return prefix
    
print(answer_queries(nums, 1, 1))



def answer_queries(nums, queries, limit):
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])

    ans = []
    for x, y in queries:
        curr_sum = prefix[y] - prefix[x] + nums[x]
        ans.append(curr_sum < limit)

    return ans

nums = list(range(10))
queries = [[0, 3], [1, 4], [2, 5], [3, 6]]
limit = 7

print(answer_queries(nums, queries, limit))


nums = [1, 6, 3, 2, 7, 2]
queries = [[0, 3], [2, 5], [2, 4], [0, 5]]
limit = 13

print(answer_queries(nums, queries, limit))
