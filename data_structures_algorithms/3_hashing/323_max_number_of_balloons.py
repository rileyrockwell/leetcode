class Solution:
    def max_number_of_balloons(self, text: str) -> int:
        # build a dictionary to store frequency of letters in balloon; evaluate
        letters_count = {}

        result = []

        for letter in text:
            letters_count[letter] = len(list(i for i in text if i == letter))

        balloon = {}
        word = "balloon"

        for letter in word:
            balloon[letter] = len(list(i for i in word if i == letter))

        result = len(text)

        for char in balloon:
            print(char)
            result = min(result, letters_count[char] // balloon[char])

        return result


print(Solution().max_number_of_balloons("balloonballoon"))
print(Solution().max_number_of_balloons("leetcode"))