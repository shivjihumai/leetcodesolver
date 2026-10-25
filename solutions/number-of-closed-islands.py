/**
 * Problem: Number of Closed Islands (Medium)
 * Language: Python
 *
 * Description:
 * Given a 2D `grid` consists of `0s` (land) and `1s` (water).  An *island* is a maximal 4-directionally connected group of `0s` and a *closed island* is an island **totally** (all left, top, right, bottom) surrounded by `1s.`
 * 
 * Return the number of *closed islands*.
 * 
 *  
 * 
 * **Example 1:**
 * 
 * **Input:** grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
 * **Output:** 2
 * **Explanation:** 
 * Islands in gray are closed because they are completely surrounded by water (group of 1s).
 * 
 * **Example 2:**
 * 
 * **Input:** grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
 * **Output:** 1
 * 
 * **Example 3:**
 * 
 * **Input:** grid = [[1,1,1,1,1,1,1],
 *                [1,0,0,0,0,0,1],
 *                [1,0,1,1,1,0,1],
 *                [1,0,1,0,1,0,1],
 *                [1,0,1,1,1,0,1],
 *                [1,0,0,0,0,0,1],
 *                [1,1,1,1,1,1,1]]
 * **Output:** 2
 * 
 *  
 * 
 * **Constraints:**
 * 
 * 	• `1 <= grid.length, grid[0].length <= 100`
 * 
 * 	• `0 <= grid[i][j] <=1`
 */

class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        closed_islands = 0
        
        def dfs(r, c):
            # If out of bounds, this island touches the boundary, so it's not closed
            if r < 0 or r >= m or c < 0 or c >= n:
                return False
            
            # If it's water or already visited, it doesn't affect the closed status
            if grid[r][c] == 1:
                return True
            
            # Mark as visited
            grid[r][c] = 1
            
            # Check all 4 directions
            # If any direction leads to a non-closed island, this island is not closed
            up = dfs(r - 1, c)
            down = dfs(r + 1, c)
            left = dfs(r, c - 1)
            right = dfs(r, c + 1)
            
            return up and down and left and right
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    if dfs(i, j):
                        closed_islands += 1
                        
        return closed_islands
