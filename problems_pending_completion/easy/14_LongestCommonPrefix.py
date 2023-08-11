def longestCommonPrefix(strs):
	for word in strs:
		# assume each element of 'strs' is the same string
		first_letter = word[0]
		second_letter = word[1]
		third_letter = word[2]

		if word[0] != first_letter:
			break
		elif word[1] != second_letter:
			break
		elif word[2] != third_letter:
			break

		# ensure the first letter of the first element ("f") of all words is the same.
		

			




# base case
strs = ["a", "a", "a"]
print(longestCommonPrefix(strs))	

strs = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs))

strs = ["dog", "racecar", "car"]
print(longestCommonPrefix(strs))