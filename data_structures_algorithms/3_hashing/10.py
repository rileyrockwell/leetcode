# https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/705/hashing/4690/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # building a seperate substring 
        subset = []
        result = 0
        respective_lengths = 0

        # sliding window / two pointers

        left, right = 0, 1
        max_subset_length = 0

        while right < len(s):
            if s[left] != s[right]:
                right += 1
                max_subset_length += 1

            elif s[left] == s[right]:
                left += 1
                max_subset_length = max(max_subset_length, right - left + 1)


        return max_subset_length



s = "abcabcbb"
s = "bbbbb"
s = "pwwkew"
print(Solution().lengthOfLongestSubstring(s))