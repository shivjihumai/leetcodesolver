/**
 * Problem: Substring with Concatenation of All Words (Hard)
 * Language: Python
 *
 * Description:
 * You are given a string `s` and an array of strings `words`. All the strings of `words` are of **the same length**.
 * 
 * A **concatenated string** is a string that exactly contains all the strings of any permutation of `words` concatenated.
 * 
 * 	• For example, if `words = ["ab","cd","ef"]`, then `"abcdef"`, `"abefcd"`, `"cdabef"`, `"cdefab"`, `"efabcd"`, and `"efcdab"` are all concatenated strings. `"acdbef"` is not a concatenated string because it is not the concatenation of any permutation of `words`.
 * 
 * Return an array of *the starting indices* of all the concatenated substrings in `s`. You can return the answer in **any order**.
 * 
 *  
 * 
 * **Example 1:**
 * 
 * **Input:** s = "barfoothefoobarman", words = ["foo","bar"]
 * 
 * **Output:** [0,9]
 * 
 * **Explanation:**
 * 
 * The substring starting at 0 is `"barfoo"`. It is the concatenation of `["bar","foo"]` which is a permutation of `words`.
 * The substring starting at 9 is `"foobar"`. It is the concatenation of `["foo","bar"]` which is a permutation of `words`.
 * 
 * **Example 2:**
 * 
 * **Input:** s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
 * 
 * **Output:** []
 * 
 * **Explanation:**
 * 
 * There is no concatenated substring.
 * 
 * **Example 3:**
 * 
 * **Input:** s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
 * 
 * **Output:** [6,9,12]
 * 
 * **Explanation:**
 * 
 * The substring starting at 6 is `"foobarthe"`. It is the concatenation of `["foo","bar","the"]`.
 * The substring starting at 9 is `"barthefoo"`. It is the concatenation of `["bar","the","foo"]`.
 * The substring starting at 12 is `"thefoobar"`. It is the concatenation of `["the","foo","bar"]`.
 * 
 *  
 * 
 * **Constraints:**
 * 
 * 	• `1 4`
 * 
 * 	• `1 <= words.length <= 5000`
 * 
 * 	• `1 <= words[i].length <= 30`
 * 
 * 	• `s` and `words[i]` consist of lowercase English letters.
 */

from collections import Counter
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        n_words = len(words)
        w_len = len(words[0])
        s_len = len(s)
        
        # Total length of the concatenated string
        total_len = n_words * w_len
        
        # If s is shorter than the total length, no solution exists
        if s_len < total_len:
            return []
        
        # Target frequency map
        word_counts = Counter(words)
        unique_words = len(word_counts)
        
        result = []
        
        # We need to check starting positions for each offset 0 to w_len - 1
        for i in range(w_len):
            # Initialize the window with the first n_words words starting at offset i
            window_counts = Counter()
            valid = 0
            count = 0  # Number of words currently in the window
            
            # Initialize the window
            for j in range(n_words):
                start_idx = i + j * w_len
                if start_idx + w_len > s_len:
                    break
                word = s[start_idx:start_idx + w_len]
                if word in word_counts:
                    window_counts[word] += 1
                    if window_counts[word] == word_counts[word]:
                        valid += 1
                    elif window_counts[word] > word_counts[word]:
                        # This case shouldn't happen in initialization if we break correctly, 
                        # but good to be safe. Actually, if it exceeds, it's invalid.
                        # We just track valid count.
                        pass
                count += 1
            
            # If we couldn't fit n_words, skip this offset
            if count < n_words:
                continue
                
            # Check if initial window is valid
            if valid == unique_words:
                result.append(i)
            
            # Slide the window
            # The next word to add starts at i + n_words * w_len
            # The word to remove starts at i
            left = i
            right = i + n_words * w_len
            
            while right + w_len <= s_len:
                # Remove word at left
                word_left = s[left:left + w_len]
                if word_left in word_counts:
                    if window_counts[word_left] == word_counts[word_left]:
                        valid -= 1
                    window_counts[word_left] -= 1
                    if window_counts[word_left] == 0:
                        del window_counts[word_left]
                
                # Add word at right
                word_right = s[right:right + w_len]
                if word_right in word_counts:
                    window_counts[word_right] += 1
                    if window_counts[word_right] == word_counts[word_right]:
                        valid += 1
                
                # Check validity
                if valid == unique_words:
                    result.append(left + w_len)
                
                # Move window
                left += w_len
                right += w_len
        
        return result
