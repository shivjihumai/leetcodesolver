/**
 * Problem: Count Islands With Total Value Divisible by K (Medium)
 * Language: Python
 *
 * Description:
 * You are given an `m x n` matrix `grid` and a positive integer `k`. An **island** is a group of **positive** integers (representing land) that are **4-directionally** connected (horizontally or vertically).
 * 
 * The **total value** of an island is the sum of the values of all cells in the island.
 * 
 * Return the number of islands with a total value **divisible by** `k`.
 * 
 *  
 * 
 * **Example 1:**
 * 
 * **Input:** grid = [[0,2,1,0,0],[0,5,0,0,5],[0,0,1,0,0],[0,1,4,7,0],[0,2,0,0,8]], k = 5
 * 
 * **Output:** 2
 * 
 * **Explanation:**
 * 
 * The grid contains four islands. The islands highlighted in blue have a total value that is divisible by 5, while the islands highlighted in red do not.
 * 
 * **Example 2:**
 * 
 * **Input:** grid = [[3,0,3,0], [0,3,0,3], [3,0,3,0]], k = 3
 * 
 * **Output:** 6
 * 
 * **Explanation:**
 * 
 * The grid contains six islands, each with a total value that is divisible by 3.
 * 
 *  
 * 
 * **Constraints:**
 * 
 * 	• `m == grid.length`
 * 
 * 	• `n == grid[i].length`
 * 
 * 	• `1 5`
 * 
 * 	• `0 6`
 * 
 * 	• `1 6`
 */

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        count = 0
        
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return 0
            
            val = grid[i][j]
            grid[i][j] = 0  # Mark as visited
            
            # Explore 4 directions
            total = val
            total += dfs(i + 1, j)
            total += dfs(i - 1, j)
            total += dfs(i, j + 1)
            total += dfs(i, j - 1)
            
            return total
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    island_sum = dfs(i, j)
                    if island_sum % k == 0:
                        count += 1
                        
        return count
