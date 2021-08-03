#Day 1 - https://leetcode.com/submissions/detail/501341938/
# Solution : think of solving it using dfs without using extra space , use the same 2D array and when every we get 1 from there using dfs start checking for max area and update it.


def dfs(grid, i, j,area):
    area[0] += 1
    grid[i][j] = 0
    if j - 1 >= 0 and grid[i][j-1] == 1:
        dfs(grid, i, j-1,area)
    if j + 1 < len(grid[0]) and grid[i][j+1] == 1:
        dfs(grid, i, j+1,area)
    if i - 1 >= 0 and grid[i-1][j] == 1:
        dfs(grid, i-1, j,area)
    if i + 1 < len(grid) and grid[i+1][j] == 1:
        dfs(grid, i+1, j,area)
    return 
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_area = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    cur_area = [0]
                    dfs(grid, i, j,cur_area)
                    
                    max_area = max(max_area, cur_area[0])
                    
        return max_area
        
