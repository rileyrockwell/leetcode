# 6315. Count the Number of Vowel Strings in Range

words = ["are", "amy", "u"]

left = 0
right = 1

vowels = ['a', 'e', 'i', 'o', 'u']

# vowel string: starts w/ a vowel character; ends w/ a vowel character

# objective: return the number of vowels strings words[i] where i belongs in the inclusive range [left, right]

class Solution:
    def vowelStrings(self, words: str, left: int, right: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        counter = 0
        # words = 
        for i in words[left: right + 1]:
            # isolate the first and last element from each of the words to verify if such characters are vowels:
            if i[0] in vowels and i[-1] in vowels:
                counter += 1
        return counter
    
if __name__ == "__main__":
    words = ["are", "amy", "u"]
    left = 0
    right = 2
    print(Solution().vowelStrings(words, left, right))