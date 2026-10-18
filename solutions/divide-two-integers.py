/**
 * Problem: Divide Two Integers (Medium)
 * Language: Python
 *
 * Description:
 * Given two integers `dividend` and `divisor`, divide two integers **without** using multiplication, division, and mod operator.
 * 
 * The integer division should truncate toward zero, which means losing its fractional part. For example, `8.345` would be truncated to `8`, and `-2.7335` would be truncated to `-2`.
 * 
 * Return *the **quotient** after dividing *`dividend`* by *`divisor`.
 * 
 * **Note: **Assume we are dealing with an environment that could only store integers within the **32-bit** signed integer range: `[&minus;231, 231 &minus; 1]`. For this problem, if the quotient is **strictly greater than** `231 - 1`, then return `231 - 1`, and if the quotient is **strictly less than** `-231`, then return `-231`.
 * 
 *  
 * 
 * **Example 1:**
 * 
 * **Input:** dividend = 10, divisor = 3
 * **Output:** 3
 * **Explanation:** 10/3 = 3.33333.. which is truncated to 3.
 * 
 * **Example 2:**
 * 
 * **Input:** dividend = 7, divisor = -3
 * **Output:** -2
 * **Explanation:** 7/-3 = -2.33333.. which is truncated to -2.
 * 
 *  
 * 
 * **Constraints:**
 * 
 * 	• `-231 31 - 1`
 * 
 * 	• `divisor != 0`
 */

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # 32‑bit signed integer limits
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Overflow case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine sign of the result
        positive = (dividend >= 0) == (divisor >= 0)

        # Work with positive numbers using 64‑bit to avoid overflow
        a = abs(dividend)
        b = abs(divisor)

        result = 0
        while a >= b:
            temp = b
            multiple = 1
            # Find the largest double of b that fits into a
            while (temp << 1) <= a:
                temp <<= 1
                multiple <<= 1
            a -= temp
            result += multiple

        # Apply sign
        if not positive:
            result = -result

        # Clamp to 32‑bit range (already handled overflow case above)
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
        return result
