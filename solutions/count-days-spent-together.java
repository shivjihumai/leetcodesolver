/**
 * Problem: Count Days Spent Together (Easy)
 * Language: Java
 *
 * Description:
 * Alice and Bob are traveling to Rome for separate business meetings.
 * 
 * You are given 4 strings `arriveAlice`, `leaveAlice`, `arriveBob`, and `leaveBob`. Alice will be in the city from the dates `arriveAlice` to `leaveAlice` (**inclusive**), while Bob will be in the city from the dates `arriveBob` to `leaveBob` (**inclusive**). Each will be a 5-character string in the format `"MM-DD"`, corresponding to the month and day of the date.
 * 
 * Return* the total number of days that Alice and Bob are in Rome together.*
 * 
 * You can assume that all dates occur in the **same** calendar year, which is **not** a leap year. Note that the number of days per month can be represented as: `[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]`.
 * 
 *  
 * 
 * **Example 1:**
 * 
 * **Input:** arriveAlice = "08-15", leaveAlice = "08-18", arriveBob = "08-16", leaveBob = "08-19"
 * **Output:** 3
 * **Explanation:** Alice will be in Rome from August 15 to August 18. Bob will be in Rome from August 16 to August 19. They are both in Rome together on August 16th, 17th, and 18th, so the answer is 3.
 * 
 * **Example 2:**
 * 
 * **Input:** arriveAlice = "10-01", leaveAlice = "10-31", arriveBob = "11-01", leaveBob = "12-31"
 * **Output:** 0
 * **Explanation:** There is no day when Alice and Bob are in Rome together, so we return 0.
 * 
 *  
 * 
 * **Constraints:**
 * 
 * 	• All dates are provided in the format `"MM-DD"`.
 * 
 * 	• Alice and Bob's arrival dates are **earlier than or equal to** their leaving dates.
 * 
 * 	• The given dates are valid dates of a **non-leap** year.
 */

class Solution {
    private static final int[] DAYS_IN_MONTH = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    private static final int[] CUMULATIVE_DAYS = new int[12];
    
    static {
        int sum = 0;
        for (int i = 0; i < 12; i++) {
            CUMULATIVE_DAYS[i] = sum;
            sum += DAYS_IN_MONTH[i];
        }
    }

    private int toDayOfYear(String date) {
        int month = Integer.parseInt(date.substring(0, 2));
        int day = Integer.parseInt(date.substring(3, 5));
        return CUMULATIVE_DAYS[month - 1] + day;
    }

    public int countDaysTogether(String arriveAlice, String leaveAlice, String arriveBob, String leaveBob) {
        int aStart = toDayOfYear(arriveAlice);
        int aEnd = toDayOfYear(leaveAlice);
        int bStart = toDayOfYear(arriveBob);
        int bEnd = toDayOfYear(leaveBob);
        
        int overlapStart = Math.max(aStart, bStart);
        int overlapEnd = Math.min(aEnd, bEnd);
        
        if (overlapStart > overlapEnd) {
            return 0;
        }
        
        return overlapEnd - overlapStart + 1;
    }
}
