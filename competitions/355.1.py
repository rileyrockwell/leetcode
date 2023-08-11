# Split Strings by Separator

import string

def splitWordsBySeperator(words, separator):
	return_list = []
	for i in words:
		i.split(separator)
		for j in i:
			if j not in string.punctuation:
				return_list.append(j)

	return return_list

print(splitWordsBySeperator(["#easy#", "#problem#"], "#"))