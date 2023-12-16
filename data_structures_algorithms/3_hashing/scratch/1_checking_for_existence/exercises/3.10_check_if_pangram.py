class Solution:
    def check_if_pangram(self, sentence: str) -> bool:
        # use a hashmap: i.e. a set of dictionary?
        # justify why that data structure is the correct one
        # create a set to remove all duplicates (from the string in the parameter)
        return len(set(sentence)) == 26

sent = "thequickbrownfoxjumpsoverthelazydog"
print(Solution().check_if_pangram(sent))

sent = "thissentenceshouldreturnfalse"
print(Solution().check_if_pangram(sent))

sent = "abcdefghijklmnopqrstuvwxyz"
print(Solution().check_if_pangram(sent))