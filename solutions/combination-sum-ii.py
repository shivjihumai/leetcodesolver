/**
 * Problem: Combination Sum II (Medium)
 * Language: Python
 *
 * Description:
 * Given a collection of candidate numbers (`candidates`) and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sum to `target`.
 * 
 * Each number in `candidates` may only be used **once** in the combination.
 * 
 * **Note:** The solution set must not contain duplicate combinations.
 * 
 *  
 * 
 * **Example 1:**
 * 
 * **Input:** candidates = [10,1,2,7,6,1,5], target = 8
 * **Output:** 
 * [
 * [1,1,6],
 * [1,2,5],
 * [1,7],
 * [2,6]
 * ]
 * 
 * **Example 2:**
 * 
 * **Input:** candidates = [2,5,2,1,2], target = 5
 * **Output:** 
 * [
 * [1,2,2],
 * [5]
 * ]
 * 
 *  
 * 
 * **Constraints:**
 * 
 * 	• `1 <= candidates.length <= 100`
 * 
 * 	• `1 <= candidates[i] <= 50`
 * 
 * 	• `1 <= target <= 30`
 */

class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        result = []
        
        def backtrack(start, current_combination, remaining_target):
            if remaining_target == 0:
                result.append(list(current_combination))
                return
            
            for i in range(start, len(candidates)):
                # Pruning: if the current candidate is greater than remaining target,
                # no need to continue since the array is sorted.
                if candidates[i] > remaining_target:
                    break
                
                # Skip duplicates: 
                # If the current element is the same as the previous one and 
                # it's not the first element in this recursion level (i > start),
                # skip it to avoid duplicate combinations.
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                current_combination.append(candidates[i])
                backtrack(i + 1, current_combination, remaining_target - candidates[i])
                current_combination.pop()
        
        backtrack(0, [], target)
        return result
