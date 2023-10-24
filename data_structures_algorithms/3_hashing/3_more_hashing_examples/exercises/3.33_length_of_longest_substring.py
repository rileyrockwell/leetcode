class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # use a hashmap...
        # use a set?
        # check uniqueness among the next letter in the sequence
        temp_list = [letter for letter in s]

        # HORRIBLE HABITS. DO NOT MAKE THE SITUATION WORSE. RECTIFY BAD HABITS.
        sub_list = []
        sub_set = set()
        for letter in temp_list:
            sub_list.append(letter)
            sub_set.add(letter)
            # duplicate exists
            if len(sub_list) != len(sub_set):
                return len(sub_set)

        # sliding window?
        


s = "abcabcbb"
print(Solution().lengthOfLongestSubstring(s))

s = "bbbbb"
print(Solution().lengthOfLongestSubstring(s))

s = "pwwkew"
print(Solution().lengthOfLongestSubstring(s))