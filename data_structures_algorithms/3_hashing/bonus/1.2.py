class Solution:
	def dest_city(self, paths: [[str]]) -> str:
		beginning_node = set()
        destination_node = set()
        
        for x, y in paths:
            beginning_node.add(x)
            destination_node.add(y)

        # b/c the destination city will always be in "destination"
        complement = destination_node - beginning_node

        return list(complement)[0]	


paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
print(Solution().dest_city(paths))

paths = [["B","C"],["D","B"],["C","A"]]
print(Solution().dest_city(paths))

paths = [["A", "Z"]]
print(Solution().dest_city(paths))