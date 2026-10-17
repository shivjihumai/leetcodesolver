/**
 * Problem: Valid Parentheses (Easy)
 * Language: Python
 *
 * Description:
 * Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.
 * 
 * An input string is valid if:
 * 
 * 	1. $1
 * 
 * 	2. $1
 * 
 * 	3. $1
 * 
 *  
 * 
 * **Example 1:**
 * 
 * **Input:** s = "()"
 * 
 * **Output:** true
 * 
 * **Example 2:**
 * 
 * **Input:** s = "()[]{}"
 * 
 * **Output:** true
 * 
 * **Example 3:**
 * 
 * **Input:** s = "(]"
 * 
 * **Output:** false
 * 
 * **Example 4:**
 * 
 * **Input:** s = "([])"
 * 
 * **Output:** true
 * 
 * **Example 5:**
 * 
 * **Input:** s = "([)]"
 * 
 * **Output:** false
 * 
 *  
 * 
 * **Constraints:**
 * 
 * 	• `1 4`
 * 
 * 	• `s` consists of parentheses only `'()[]{}'`.
 */

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching_brackets = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in matching_brackets:
                # If it's a closing bracket
                if not stack or stack[-1] != matching_brackets[char]:
                    return False
                stack.pop()
            else:
                # If it's an opening bracket
                stack.append(char)
                
        return len(stack) == 0
