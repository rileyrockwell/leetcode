class Solution:
    def check_if_pangram(self, sentence: str) -> bool:
        # use a hashmap: i.e. a set of dictionary?
        # justify why that data structure is the correct one
        # create a set to remove all duplicates (from the string in the parameter)
        temp_list = " ".join(sentence).split(" ")
        temp_list = set(temp_list)

        if len(temp_list) == 26:
            return True

        return False


sent = "thequickbrownfoxjumpsoverthelazydog"
print(Solution().check_if_pangram(sent))

sent = "thissentenceshouldreturnfalse"
print(Solution().check_if_pangram(sent))

sent = "abcdefghijklmnopqrstuvwxyz"
print(Solution().check_if_pangram(sent))