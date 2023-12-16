def check_if_palindrome(s):
    """
    s: str
    return: bool
    """

    # left == "left pointer"
    left = 0

    # right == "right pointer"
    right = (len(s) - 1)

    while left < right:
        if s[left] != s[right]:
            return False

        left += 1
        right -= 1

    return True

print(check_if_palindrome("able was i ere i saw elba"))
print(check_if_palindrome("hannah"))
def check_for_target(nums, target):
    """
    nums: list
    target: int
    return: bool
    """

    left = 0
    right = len(nums) - 1

    while left < right:
        curr = nums[left] + nums[right]

        if curr == target:
            return True

        if curr > target:
            right -= 1
        else:
            left += 1

    return False

nums = [1, 2, 4, 6, 8, 9, 14, 15]
print(check_for_target(nums, 13))


def combine(arr1, arr2):
    ans = []
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            ans.append(arr1[i])
            i += 1
        else:
            ans.append(arr2[j])
            j += 1

    while i < len(arr1):
        ans.append(arr1[i])
        i += 1

    while j < len(arr2):
        ans.append(arr2[j])
        j += 1

    return ans

arr1 = [i for i in range(10) if i % 2 == 0]
arr2 = [i for i in range(10) if i % 2 == 1]

print(combine(arr1, arr2))


def is_subsequence(s, t):
    """
    s: str; subsequence
    t: str; sequence 
    return: bool
    """
    i = j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            # gain a "point"
            i += 1

            # else: no "point"
        
        # move onto the next element of the larger string
        j += 1

    return i == len(s)

print(is_subsequence("ace", "abcde"))
print(is_subsequence("abcde", "ace"))


### time complexity ###
# is_palindrome             O(n)
# check_if_target           ...
# combine                   ...
# is_subsequence            ...


### space complexity ###
# is_palindrome             ...
# check_if_target           ...
# combine                   ...
# is_subsequence            ...