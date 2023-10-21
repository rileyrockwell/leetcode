class Solution:
	def can_construct(self, ransom_note: str, magazine: str) -> bool:
		# build the hashmap for ransom_note
		ransom_note_dic = {}
		magazine_dic = {}

		for letter in ransom_note:
			ransom_note_dic[letter] = len(list(i for i in ransom_note if i == letter))

		for letter in magazine:
			magazine_dic[letter] = len(list(i for i in magazine if i == letter))

		return ransom_note_dic, magazine_dic


ransom_note = "aa"
magazine = "aab"
print(Solution().can_construct(ransom_note, magazine))