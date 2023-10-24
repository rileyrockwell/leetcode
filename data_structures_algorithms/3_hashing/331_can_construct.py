class Solution:
	def can_construct(self, ransom_note: str, magazine: str) -> bool:
		hashmap_set = {}
		hashmap_subset = {}

		for letter in magazine:
			hashmap_set[letter] = len(list(i for i in magazine if i == letter))

		for letter in ransom_note:
			hashmap_subset[letter] = len(list(i for i in ransom_note if i == letter))

		return hashmap_set, hashmap_subset


ransom_note = "testing this string"
magazine = "magazone string"
print(Solution().can_construct(ransom_note, magazine))

print("testing")