/**
 * Problem: Longest Valid Parentheses (Hard)
 * Language: Python
 *
 * Description:
 * Given a string containing just the characters `'('` and `')'`, return *the length of the longest valid (well-formed) parentheses **substring*.
 * 
 *  
 * 
 * **Example 1:**
 * 
 * **Input:** s = "(()"
 * **Output:** 2
 * **Explanation:** The longest valid parentheses substring is "()".
 * 
 * **Example 2:**
 * 
 * **Input:** s = ")()())"
 * **Output:** 4
 * **Explanation:** The longest valid parentheses substring is "()()".
 * 
 * **Example 3:**
 * 
 * **Input:** s = ""
 * **Output:** 0
 * 
 *  
 * 
 * **Constraints:**
 * 
 * 	• `0 4`
 * 
 * 	• `s[i]` is `'('`, or `')'`.
 */

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        
        n = len(s)
        dp = [0] * n
        max_len = 0
        
        for i in range(1, n):
            if s[i] == ')':
                # Find the index of the potential matching '('
                # i - 1 - dp[i-1] is the index just before the valid substring ending at i-1
                prev_index = i - 1 - dp[i-1]
                
                if prev_index >= 0 and s[prev_index] == '(':
                    # We found a matching '('
                    # The length is 2 (for the current pair) 
                    # + dp[i-1] (the valid substring ending at i-1)
                    # + dp[prev_index - 1] (any valid substring before the matching '(')
                    dp[i] = 2 + dp[i-1]
                    if prev_index > 0:
                        dp[i] += dp[prev_index - 1]
                    
                    max_len = max(max_len, dp[i])
        
        return max_len
