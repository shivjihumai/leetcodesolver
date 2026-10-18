/**
 * Problem: Find the Index of the First Occurrence in a String (Easy)
 * Language: Python
 *
 * Description:
 * Given two strings `needle` and `haystack`, return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.
 * 
 *  
 * 
 * **Example 1:**
 * 
 * **Input:** haystack = "sadbutsad", needle = "sad"
 * **Output:** 0
 * **Explanation:** "sad" occurs at index 0 and 6.
 * The first occurrence is at index 0, so we return 0.
 * 
 * **Example 2:**
 * 
 * **Input:** haystack = "leetcode", needle = "leeto"
 * **Output:** -1
 * **Explanation:** "leeto" did not occur in "leetcode", so we return -1.
 * 
 *  
 * 
 * **Constraints:**
 * 
 * 	• `1 4`
 * 
 * 	• `haystack` and `needle` consist of only lowercase English characters.
 */

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        
        # Edge case: if needle is empty, return 0
        if m == 0:
            return 0
            
        # Step 1: Build the LPS (Longest Proper Prefix which is also Suffix) array
        lps = [0] * m
        length = 0  # length of the previous longest prefix suffix
        i = 1
        
        while i < m:
            if needle[i] == needle[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                # Do not increment i here
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        
        # Step 2: Search for the needle in the haystack
        i = 0  # index for haystack
        j = 0  # index for needle
        
        while i < n:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                
            if j == m:
                # Match found
                return i - j
            elif i < n and haystack[i] != needle[j]:
                # Mismatch
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        
        return -1
