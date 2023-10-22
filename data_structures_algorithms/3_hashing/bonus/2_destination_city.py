class Solution:
	def dest_city(self, paths: [[str]]) -> str:
		


paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
print(Solution().dest_city(paths))

paths = [["B","C"],["D","B"],["C","A"]]
print(Solution().dest_city(paths))

paths = [["A", "Z"]]
print(Solution().dest_city(paths))