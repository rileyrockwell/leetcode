from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # using a hashmap w/in the context of a sliding window
        chars = Counter()

        left = right = 0

        result = 0

        while right < len(s):
            r = s[right]
            chars[r] += 1

            while chars[r] > 1:
                l = s[left]
                chars[l] -= 1
                left += 1

            result = max(result, right - left + 1)

            right += 1

        return result



s = "abcabcbb"
print(Solution().lengthOfLongestSubstring(s))

s = "bbbbb"
print(Solution().lengthOfLongestSubstring(s))

s = "pwwkew"
print(Solution().lengthOfLongestSubstring(s))