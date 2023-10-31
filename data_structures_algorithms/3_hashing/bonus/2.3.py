from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # build a dictionarry and check that no duplicates exists among the values (of the dictionary)
    
        temp_dict = dict(Counter(arr))

        temp_list = list(temp_dict.values())
        
        if len(temp_list) != len(set(temp_list)):
            return False

        return True