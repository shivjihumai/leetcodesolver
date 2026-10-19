/**
 * Problem: Find First and Last Position of Element in Sorted Array (Medium)
 * Language: Java
 *
 * Description:
 * Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.
 * 
 * If `target` is not found in the array, return `[-1, -1]`.
 * 
 * You must write an algorithm with `O(log n)` runtime complexity.
 * 
 *  
 * 
 * **Example 1:**
 * 
 * **Input:** nums = [5,7,7,8,8,10], target = 8
 * **Output:** [3,4]
 * 
 * **Example 2:**
 * 
 * **Input:** nums = [5,7,7,8,8,10], target = 6
 * **Output:** [-1,-1]
 * 
 * **Example 3:**
 * 
 * **Input:** nums = [], target = 0
 * **Output:** [-1,-1]
 * 
 *  
 * 
 * **Constraints:**
 * 
 * 	• `0 5`
 * 
 * 	• `-109 9`
 * 
 * 	• `nums` is a non-decreasing array.
 * 
 * 	• `-109 9`
 */

class Solution {
    public int[] searchRange(int[] nums, int target) {
        int n = nums.length;
        if (n == 0) {
            return new int[]{-1, -1};
        }

        int left = 0;
        int right = n - 1;

        // Find the first occurrence
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] < target) {
                left = mid + 1;
            } else {
                // nums[mid] >= target, so the first occurrence is at mid or to the left
                right = mid - 1;
            }
        }

        // Check if target was found
        if (left >= n || nums[left] != target) {
            return new int[]{-1, -1};
        }

        int first = left;

        // Reset for finding the last occurrence
        left = 0;
        right = n - 1;

        // Find the last occurrence
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] > target) {
                right = mid - 1;
            } else {
                // nums[mid] <= target, so the last occurrence is at mid or to the right
                left = mid + 1;
            }
        }

        // right will be the last index where nums[right] == target
        int last = right;

        return new int[]{first, last};
    }
}
