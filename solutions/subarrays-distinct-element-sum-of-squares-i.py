/**
 * Problem: Subarrays Distinct Element Sum of Squares I (Easy)
 * Language: Python
 *
 * Description:
 * You are given a **0-indexed **integer array `nums`.
 * 
 * The **distinct count** of a subarray of `nums` is defined as:
 * 
 * 	• Let `nums[i..j]` be a subarray of `nums` consisting of all the indices from `i` to `j` such that `0 
 * **Input:** nums = [1,2,1]
 * **Output:** 15
 * **Explanation:** Six possible subarrays are:
 * [1]: 1 distinct value
 * [2]: 1 distinct value
 * [1]: 1 distinct value
 * [1,2]: 2 distinct values
 * [2,1]: 2 distinct values
 * [1,2,1]: 2 distinct values
 * The sum of the squares of the distinct counts in all subarrays is equal to 12 + 12 + 12 + 22 + 22 + 22 = 15.
 * 
 * **Example 2:**
 * 
 * **Input:** nums = [1,1]
 * **Output:** 3
 * **Explanation:** Three possible subarrays are:
 * [1]: 1 distinct value
 * [1]: 1 distinct value
 * [1,1]: 1 distinct value
 * The sum of the squares of the distinct counts in all subarrays is equal to 12 + 12 + 12 = 3.
 * 
 *  
 * 
 * **Constraints:**
 * 
 * 	• `1 <= nums.length <= 100`
 * 
 * 	• `1 <= nums[i] <= 100`
 */

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = 0
        
        for i in range(n):
            seen = set()
            for j in range(i, n):
                seen.add(nums[j])
                distinct_count = len(seen)
                total_sum += distinct_count * distinct_count
                
        return total_sum
