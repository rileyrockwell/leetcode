class Solution:
    def checkValidGrid(self, grid: [[int]]) -> bool:
        x, y = 0, 0
        position = 0
        while True:
            # (1). uncertain...
            grid[x + 2][y + 1]

            # (2). "calculate all possible moves" given constraints from (1), and return false if no valid moves are
            # the next move

            # (3). Q: if not at 0,0 (top-left), how is the program updating the matrix indentification elements so
            # that 

            # (4). relevance of dimensions of the grid



grid = [[0,11,16,5,20],[17,4,19,10,15],[12,1,8,21,6],[3,18,23,14,9],[24,13,2,7,22]]
print(Solution().checkValidGrid(grid))