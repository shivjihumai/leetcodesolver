/**
 * Problem: Multiply Strings (Medium)
 * Language: Java
 *
 * Description:
 * Given two non-negative integers `num1` and `num2` represented as strings, return the product of `num1` and `num2`, also represented as a string.
 * 
 * **Note:** You must not use any built-in BigInteger library or convert the inputs to integer directly.
 * 
 *  
 * 
 * **Example 1:**
 * 
 * **Input:** num1 = "2", num2 = "3"
 * **Output:** "6"
 * 
 * **Example 2:**
 * 
 * **Input:** num1 = "123", num2 = "456"
 * **Output:** "56088"
 * 
 *  
 * 
 * **Constraints:**
 * 
 * 	• `1 <= num1.length, num2.length <= 200`
 * 
 * 	• `num1` and `num2` consist of digits only.
 * 
 * 	• Both `num1` and `num2` do not contain any leading zero, except the number `0` itself.
 */

class Solution {
    public String multiply(String num1, String num2) {
        int m = num1.length();
        int n = num2.length();
        
        // The result of multiplying two numbers with m and n digits 
        // will have at most m + n digits.
        int[] res = new int[m + n];
        
        // Iterate from the last digit of num1
        for (int i = m - 1; i >= 0; i--) {
            int d1 = num1.charAt(i) - '0';
            
            // Iterate from the last digit of num2
            for (int j = n - 1; j >= 0; j--) {
                int d2 = num2.charAt(j) - '0';
                
                // The product of digits at i and j contributes to 
                // positions i + j and i + j + 1 in the result array.
                int product = d1 * d2 + res[i + j + 1];
                
                // Update the current position with the unit digit
                res[i + j + 1] = product % 10;
                
                // Add the carry to the next position
                res[i + j] += product / 10;
            }
        }
        
        // Build the result string, skipping leading zeros
        StringBuilder sb = new StringBuilder();
        int i = 0;
        // Skip leading zeros
        while (i < res.length && res[i] == 0) {
            i++;
        }
        
        // If we reached the end, the result is 0
        if (i == res.length) {
            return "0";
        }
        
        // Append the remaining digits
        for (; i < res.length; i++) {
            sb.append(res[i]);
        }
        
        return sb.toString();
    }
}
