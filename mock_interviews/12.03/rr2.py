"""
https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.


Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6


Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
"""

from collections import Counter

def doesFit(lhs, rhs):
    for key, value in lhs.items():
        if key not in rhs or value > rhs[key]:
            return False
    return True 

def validWord(words, chars):
    sum = 0 
    temp_chars = Counter(chars)
    for word in words:
        freq_dict = Counter(word)
        if doesFit(freq_dict, temp_chars.copy()):
            sum += len(word)
    return sum
                

words = ["cat","bt","hat","tree"]
chars = "atach"
print(validWord(words, chars))