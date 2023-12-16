class Solution:
	def max_number_of_balloons(self, text: str) -> int:
		# using a hashmap in the context of counting
		letters_frequency = {}

		result = []

		# build parameter ("text") dictionary
		for letter in text:
			letters_frequency[letter] = len(list(i for i in text if i == letter))

		balloon = {}
		word = "balloon"

		# build balloon dictionary
		for letter in word:
			balloon[letter] = len(list(i for i in word if i == letter))

		print(letters_frequency)
		print(balloon)
		percent_correct = 0

		for char in range(len(text)):
			if word[char] < 1:
				return False
			elif word[char] not in list(word.keys()):
				pass
			else:
				letters_frequency[char] -= 1
				percent_correct += 1

		result = percent_correct // len(word)

		return result




# print(Solution().max_number_of_balloons("nlaebolko"))

print(Solution().max_number_of_balloons("loonbalxballpoon"))