/**
 * Problem: Valid Sudoku (Medium)
 * Language: Python
 *
 * Description:
 * Determine if a `9 x 9` Sudoku board is valid. Only the filled cells need to be validated **according to the following rules**:
 * 
 * 	1. $1
 * 
 * 	2. $1
 * 
 * 	3. $1
 * 
 * **Note:**
 * 
 * 	• A Sudoku board (partially filled) could be valid but is not necessarily solvable.
 * 
 * 	• Only the filled cells need to be validated according to the mentioned rules.
 * 
 *  
 * 
 * **Example 1:**
 * 
 * **Input:** board = 
 * [["5","3",".",".","7",".",".",".","."]
 * ,["6",".",".","1","9","5",".",".","."]
 * ,[".","9","8",".",".",".",".","6","."]
 * ,["8",".",".",".","6",".",".",".","3"]
 * ,["4",".",".","8",".","3",".",".","1"]
 * ,["7",".",".",".","2",".",".",".","6"]
 * ,[".","6",".",".",".",".","2","8","."]
 * ,[".",".",".","4","1","9",".",".","5"]
 * ,[".",".",".",".","8",".",".","7","9"]]
 * **Output:** true
 * 
 * **Example 2:**
 * 
 * **Input:** board = 
 * [["8","3",".",".","7",".",".",".","."]
 * ,["6",".",".","1","9","5",".",".","."]
 * ,[".","9","8",".",".",".",".","6","."]
 * ,["8",".",".",".","6",".",".",".","3"]
 * ,["4",".",".","8",".","3",".",".","1"]
 * ,["7",".",".",".","2",".",".",".","6"]
 * ,[".","6",".",".",".",".","2","8","."]
 * ,[".",".",".","4","1","9",".",".","5"]
 * ,[".",".",".",".","8",".",".","7","9"]]
 * **Output:** false
 * **Explanation:** Same as Example 1, except with the **5** in the top left corner being modified to **8**. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 * 
 *  
 * 
 * **Constraints:**
 * 
 * 	• `board.length == 9`
 * 
 * 	• `board[i].length == 9`
 * 
 * 	• `board[i][j]` is a digit `1-9` or `'.'`.
 */

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Initialize sets for rows, columns, and 3x3 boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue
                
                # Calculate the box index
                # Box index ranges from 0 to 8
                # Top-left box is 0, top-middle is 1, top-right is 2, etc.
                box_index = (i // 3) * 3 + (j // 3)
                
                # Check if the value already exists in the current row, col, or box
                if val in rows[i] or val in cols[j] or val in boxes[box_index]:
                    return False
                
                # Add the value to the respective sets
                rows[i].add(val)
                cols[j].add(val)
                boxes[box_index].add(val)
        
        return True
