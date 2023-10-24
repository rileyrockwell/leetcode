class Solution:
	def can_construct(self, ransom_note: str, magazine: str) -> bool:
		# build the hashmap for ransom_note
		ransom_note_dic = {}
		magazine_dic = {}

		for letter in ransom_note:
			ransom_note_dic[letter] = len(list(i for i in ransom_note if i == letter))

		for letter in magazine:
			magazine_dic[letter] = len(list(i for i in magazine if i == letter))

		subset = ransom_note_dic
		orig_set = magazine_dic

		for key, value in subset.items():
			if key not in orig_set.keys():
				# key not in parent set
				return False
			elif subset[key] > orig_set[key]:
				# not enough letters in parent set to satisfy subset
				return False

		
		# if for every key in subset there is a key in orig_set with a value greater than or equal
		# to the value in subset
		return True

ransom_note = "a"
magazine = "b"
print(Solution().can_construct(ransom_note, magazine))

ransom_note = "aa"
magazine = "ab"
print(Solution().can_construct(ransom_note, magazine))

ransom_note = "aa"
magazine = "aab"
print(Solution().can_construct(ransom_note, magazine))

ransom_note = "fihjjjjei"
magazine = "hjibagacbhadfaefdjaeaebgi"
print(Solution().can_construct(ransom_note, magazine))