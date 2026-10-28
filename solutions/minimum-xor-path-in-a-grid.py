/**
 * Problem: Minimum XOR Path in a Grid (Medium)
 * Language: Python
 *
 * Description:
 * You are given a 2D integer array `grid` of size `m * n`.
 * 
 * You start at the **top-left** cell `(0, 0)` and want to reach the **bottom-right** cell `(m - 1, n - 1)`.
 * 
 * At each step, you **may** move either **right or down**.
 * 
 * The **cost** of a path is defined as the **bitwise XOR** of all the values in the cells along that path, **including** the start and end cells.
 * 
 * Return the **minimum** possible XOR value among all valid paths from `(0, 0)` to `(m - 1, n - 1)`.
 * 
 *  
 * 
 * **Example 1:**
 * 
 * **Input:** grid = [[1,2],[3,4]]
 * 
 * **Output:** 6
 * 
 * **Explanation:**
 * 
 * There are two valid paths:
 * 
 * 	• `(0, 0) &rarr; (0, 1) &rarr; (1, 1)` with XOR: `1 XOR 2 XOR 4 = 7`
 * 
 * 	• `(0, 0) &rarr; (1, 0) &rarr; (1, 1)` with XOR: `1 XOR 3 XOR 4 = 6`
 * 
 * The minimum XOR value among all valid paths is 6.
 * 
 * **Example 2:**
 * 
 * **Input:** grid = [[6,7],[5,8]]
 * 
 * **Output:** 9
 * 
 * **Explanation:**
 * 
 * There are two valid paths:
 * 
 * 	• `(0, 0) &rarr; (0, 1) &rarr; (1, 1)` with XOR: `6 XOR 7 XOR 8 = 9`
 * 
 * 	• `(0, 0) &rarr; (1, 0) &rarr; (1, 1)` with XOR: `6 XOR 5 XOR 8 = 11`
 * 
 * The minimum XOR value among all valid paths is 9.
 * 
 * **Example 3:**
 * 
 * **Input:** grid = [[2,7,5]]
 * 
 * **Output:** 0
 * 
 * **Explanation:**
 * 
 * There is only one valid path:
 * 
 * 	• `(0, 0) &rarr; (0, 1) &rarr; (0, 2)` with XOR: `2 XOR 7 XOR 5 = 0`
 * 
 * The XOR value of this path is 0, which is the minimum possible.
 * 
 *  
 * 
 * **Constraints:**
 * 
 * 	• `1 <= m == grid.length <= 1000`
 * 
 * 	• `1 <= n == grid[i].length <= 1000`
 * 
 * 	• `m * n <= 1000`
 * 
 * 	• `0 <= grid[i][j] <= 1023​`
 */

from typing import List, Set

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        """
        Returns the minimum possible XOR value of a path from (0,0) to
        (m-1,n-1) moving only right or down.
        """
        m, n = len(grid), len(grid[0])

        # dp[j] holds the set of reachable XOR values for the current row,
        # column j.
        dp: List[Set[int]] = [set() for _ in range(n)]

        # first cell
        dp[0].add(grid[0][0])

        # first row (only moves from the left)
        for j in range(1, n):
            dp[j] = {v ^ grid[0][j] for v in dp[j - 1]}

        # remaining rows
        for i in range(1, m):
            # first column (only moves from above)
            dp[0] = {v ^ grid[i][0] for v in dp[0]}

            for j in range(1, n):
                new_set: Set[int] = set()
                # from top
                for v in dp[j]:
                    new_set.add(v ^ grid[i][j])
                # from left
                for v in dp[j - 1]:
                    new_set.add(v ^ grid[i][j])
                dp[j] = new_set

        # answer is the smallest reachable XOR at the bottom‑right cell
        return min(dp[n - 1])
