# copied from solution

class Solution:
    def destCity(self, paths: [[str]]) -> str:
        # using a hashmap...
        has_outgoing = set()
        for i in range(len(paths)):
            has_outgoing.add(paths[i][0])
        print(has_outgoing)

        for i in range(len(paths)):
            candidate = paths[i][1]
            if candidate not in has_outgoing:
                return candidate
        
        return ""





paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
print(Solution().destCity(paths))

paths = [["B","C"],["D","B"],["C","A"], ["E", "D"]]
print(Solution().destCity(paths))

paths = [["A","Z"]]
print(Solution().destCity(paths))