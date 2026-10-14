/**
 * Problem: Longest Common Prefix (Easy)
 * Language: Java
 *
 * Description:
 * Write a function to find the longest common prefix string amongst an array of strings.
 * 
 * If there is no common prefix, return an empty string `""`.
 * 
 *  
 * 
 * **Example 1:**
 * 
 * **Input:** strs = ["flower","flow","flight"]
 * **Output:** "fl"
 * 
 * **Example 2:**
 * 
 * **Input:** strs = ["dog","racecar","car"]
 * **Output:** ""
 * **Explanation:** There is no common prefix among the input strings.
 * 
 *  
 * 
 * **Constraints:**
 * 
 * 	• `1 <= strs.length <= 200`
 * 
 * 	• `0 <= strs[i].length <= 200`
 * 
 * 	• `strs[i]` consists of only lowercase English letters if it is non-empty.
 */

class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0) {
            return "";
        }
        
        // Iterate through each character index of the first string
        for (int i = 0; i < strs[0].length(); i++) {
            char c = strs[0].charAt(i);
            
            // Compare this character with the same index in all other strings
            for (int j = 1; j < strs.length; j++) {
                // If the current string is shorter than i+1 or the character doesn't match
                if (i >= strs[j].length() || strs[j].charAt(i) != c) {
                    // Return the common prefix found so far
                    return strs[0].substring(0, i);
                }
            }
        }
        
        // If we finish the loop without returning, the first string is the prefix
        return strs[0];
    }
}
