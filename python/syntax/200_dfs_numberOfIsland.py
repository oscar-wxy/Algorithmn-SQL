from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        flag = [[False for j in range(len(grid[0]))] for i in range(len(grid))]

        for i in range(len(grid)):
            for j in range(len(grid[1])):
                if grid[i][j] == '1' and flag[i][j] == False:
                    self.search(grid, flag, i, j)
                    count = count + 1
        return count

    def search(self, grid, flag, i, j):
        if i < 0 or i > len(grid) - 1 or j < 0 or j > len(grid[0]) - 1 or flag[i][j] == True or grid[i][j] == '0':
            return

        flag[i][j] = True

        self.search(grid, flag, i + 1, j)
        self.search(grid, flag, i - 1, j)
        self.search(grid, flag, i, j + 1)
        self.search(grid, flag, i, j - 1)
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
# print(Solution().numIslands(grid))
print(grid[1][0])
print(len(grid))
print(len(grid[0]))

"""
use self to call internal class method, how to create two dimenison array
flag = [[False for j in range(len(grid[0]))] for i in range(len(grid))]
"""