/**
 * Problem: 4Sum (Medium)
 * Language: Python
 *
 * Description:
 * Given an array `nums` of `n` integers, return *an array of all the **unique** quadruplets* `[nums[a], nums[b], nums[c], nums[d]]` such that:
 * 
 * 	• `0 
 * **Input:** nums = [1,0,-1,0,-2,2], target = 0
 * **Output:** [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
 * 
 * **Example 2:**
 * 
 * **Input:** nums = [2,2,2,2,2], target = 8
 * **Output:** [[2,2,2,2]]
 * 
 *  
 * 
 * **Constraints:**
 * 
 * 	• `1 9 9`
 * 
 * 	• `-109 9`
 */

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        res = []
        
        for i in range(n - 3):
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            for j in range(i + 1, n - 2):
                # Skip duplicates for the second element
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                    
                left = j + 1
                right = n - 1
                
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if total == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        # Skip duplicates for the third element
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        # Skip duplicates for the fourth element
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
                        
        return res
