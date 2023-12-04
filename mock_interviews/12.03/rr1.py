"""
https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true

Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: false

Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
Output: true

Constraints:
1 <= word1.length, word2.length <= 103
1 <= word1[i].length, word2[i].length <= 103
1 <= sum(word1[i].length), sum(word2[i].length) <= 103
word1[i] and word2[i] consist of lowercase letters.
"""


# O(n2)
def isValid(word1, word2):
    compare_str1 = ""
    for string in word1:
        compare_str1 += string

    compare_str2 = ""
    for string in word2:
        compare_str2 += string

    return compare_str1 == compare_str2


word1 = ["ab", "c"]
word2 = ["a", "bc"]

word1 = ["a", "cb"]
word2 = ["ab", "c"]

word1  = ["abc", "d", "defg"]
word2 = ["abcddefg"]


print(isValid(word1, word2))