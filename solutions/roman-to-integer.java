/**
 * Problem: Roman to Integer (Easy)
 * Language: Java
 *
 * Description:
 * Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D` and `M`.
 * 
 * ```
 * 2
 * ```
 * 
 * **Example 2:**
 * 
 * **Input:** s = "LVIII"
 * **Output:** 58
 * **Explanation:** L = 50, V= 5, III = 3.
 * 
 * **Example 3:**
 * 
 * **Input:** s = "MCMXCIV"
 * **Output:** 1994
 * **Explanation:** M = 1000, CM = 900, XC = 90 and IV = 4.
 * 
 *  
 * 
 * **Constraints:**
 * 
 * 	• `1 <= s.length <= 15`
 * 
 * 	• `s` contains only the characters `('I', 'V', 'X', 'L', 'C', 'D', 'M')`.
 * 
 * 	• It is **guaranteed** that `s` is a valid roman numeral in the range `[1, 3999]`.
 */

class Solution {
    public int romanToInt(String s) {
        // Mapping of Roman characters to their integer values
        int[] map = new int[128];
        map['I'] = 1;
        map['V'] = 5;
        map['X'] = 10;
        map['L'] = 50;
        map['C'] = 100;
        map['D'] = 500;
        map['M'] = 1000;

        int total = 0;
        int n = s.length();

        for (int i = 0; i < n; i++) {
            int curr = map[s.charAt(i)];
            // Look ahead to the next character if it exists
            if (i + 1 < n && curr < map[s.charAt(i + 1)]) {
                total -= curr;   // subtractive case
            } else {
                total += curr;   // additive case
            }
        }
        return total;
    }
}
