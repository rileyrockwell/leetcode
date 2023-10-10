from collections import defaultdict

def find_longest_substring(s, k):
    counts = defaultdict(int)
    left = ans = 0
    for right in range(len(s)):
        counts[s[right]] += 1
        while len(counts) > k:
            counts[s[left]] -= 1
            if counts[s[left]] == 0:
                del counts[s[left]]
            left += 1
        
        ans = max(ans, right - left + 1)
    
    return ans

print(find_longest_substring("eceba", 2))

# 0.00

def find_longest_substring(s, k):
    counts = defaultdict(int)
    # intialize left and answer
    left = ans = 0
    # loop over the parameter, s
    for right in range(len(s)):
        # sliding window?
        counts[s[right]] += 1
        while len(counts) > k:
            counts[s[left]] -= 1
            if counts[s[left]] == 0:
                del counts[s[left]]
            left += 1

        ans = max(ans, right - left + 1)

    return ans

# 0.05

def find_longest_substring(s, k):
    counts = defaultdict(int)

    left = ans = 0

    for right in range(len(s)):
        counts[s[right]] += 1
        while len(counts) > k:
            counts[s[left]] -= 1
            if counts[s[left]] == 0:
                del counts[s[left]]
            left += 1

        ans = max(ans, right - left + 1)

    return ans


def find_longest_substring(s, k):
    counts = defaultdict(int)

    left = ans = 0

    for right in range(len(s)):
        # ???
        counts[s[right]] += 1

        while len(counts) > k:
            counts[s[left]] -= 1
            if counts[s[left]] == 0:
                del counts[s[left]]
            left += 1

        ans = max(ans, right - left + 1)

    return ans


def find_longest_substring(s, t):
    counts = defaultdict(int)

    left = ans = 0

    for right in range(len(s)):
        counts[s[right]] += 1
        if counts[s[left]] == 0:
            del counts[s[left]]
        left += 1

        ans = max(ans, right - left + 1)

    return ans


def find_longest_substring(s, t):
    counts = defaultdict(int)

    left = ans = 0

    for right in range(len(s)):
        counts[s[right]] += 1
        if counts[s[left]] == 0:
            




s = "eceba"
k = 2
print(find_longest_substring(s, k))