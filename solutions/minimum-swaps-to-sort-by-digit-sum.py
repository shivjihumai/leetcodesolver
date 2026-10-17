/**
 * Problem: Minimum Swaps to Sort by Digit Sum (Medium)
 * Language: Python
 *
 * Description:
 * You are given an array `nums` of **distinct** positive integers. You need to sort the array in **increasing** order based on the sum of the digits of each number. If two numbers have the same digit sum, the **smaller** number appears first in the sorted order.
 * 
 * Return the **minimum** number of swaps required to rearrange `nums` into this sorted order.
 * 
 * A **swap** is defined as exchanging the values at two distinct positions in the array.
 * 
 *  
 * 
 * **Example 1:**
 * 
 * **Input:** nums = [37,100]
 * 
 * **Output:** 1
 * 
 * **Explanation:**
 * 
 * 	• Compute the digit sum for each integer: `[3 + 7 = 10, 1 + 0 + 0 = 1] &rarr; [10, 1]`
 * 
 * 	• Sort the integers based on digit sum: `[100, 37]`. Swap `37` with `100` to obtain the sorted order.
 * 
 * 	• Thus, the minimum number of swaps required to rearrange `nums` is 1.
 * 
 * **Example 2:**
 * 
 * **Input:** nums = [22,14,33,7]
 * 
 * **Output:** 0
 * 
 * **Explanation:**
 * 
 * 	• Compute the digit sum for each integer: `[2 + 2 = 4, 1 + 4 = 5, 3 + 3 = 6, 7 = 7] &rarr; [4, 5, 6, 7]`
 * 
 * 	• Sort the integers based on digit sum: `[22, 14, 33, 7]`. The array is already sorted.
 * 
 * 	• Thus, the minimum number of swaps required to rearrange `nums` is 0.
 * 
 * **Example 3:**
 * 
 * **Input:** nums = [18,43,34,16]
 * 
 * **Output:** 2
 * 
 * **Explanation:**
 * 
 * 	• Compute the digit sum for each integer: `[1 + 8 = 9, 4 + 3 = 7, 3 + 4 = 7, 1 + 6 = 7] &rarr; [9, 7, 7, 7]`
 * 
 * 	• Sort the integers based on digit sum: `[16, 34, 43, 18]`. Swap `18` with `16`, and swap `43` with `34` to obtain the sorted order.
 * 
 * 	• Thus, the minimum number of swaps required to rearrange `nums` is 2.
 * 
 *  
 * 
 * **Constraints:**
 * 
 * 	• `1 5`
 * 
 * 	• `1 9`
 * 
 * 	• `nums` consists of **distinct** positive integers.
 */

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(n):
            s = 0
            while n:
                s += n % 10
                n //= 10
            return s
        
        # Create the target sorted array
        # Sort by (digit_sum, value)
        target = sorted(nums, key=lambda x: (digit_sum(x), x))
        
        # Map each value in target to its index in target
        # Since nums are distinct, this is a valid bijection
        val_to_idx = {val: idx for idx, val in enumerate(target)}
        
        n = len(nums)
        visited = [False] * n
        swaps = 0
        
        for i in range(n):
            # If already in correct position or already visited, skip
            if visited[i] or nums[i] == target[i]:
                continue
            
            # Start a new cycle
            cycle_len = 0
            j = i
            
            while not visited[j]:
                visited[j] = True
                cycle_len += 1
                # The element nums[j] should go to index val_to_idx[nums[j]] in the target array.
                # This index is the next node in the cycle.
                j = val_to_idx[nums[j]]
            
            # A cycle of length k requires k-1 swaps
            swaps += cycle_len - 1
            
        return swaps
