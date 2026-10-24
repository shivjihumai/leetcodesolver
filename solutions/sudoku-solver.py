/**
 * Problem: Sudoku Solver (Hard)
 * Language: Python
 *
 * Description:
 * Write a program to solve a Sudoku puzzle by filling the empty cells.
 * 
 * A sudoku solution must satisfy **all of the following rules**:
 * 
 * 	1. $1
 * 
 * 	2. $1
 * 
 * 	3. $1
 * 
 * The `'.'` character indicates empty cells.
 * 
 *  
 * 
 * **Example 1:**
 * 
 * **Input:** board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
 * **Output:** [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
 * **Explanation:** The input board is shown above and the only valid solution is shown below:
 * 
 *  
 * 
 * **Constraints:**
 * 
 * 	• `board.length == 9`
 * 
 * 	• `board[i].length == 9`
 * 
 * 	• `board[i][j]` is a digit or `'.'`.
 * 
 * 	• It is **guaranteed** that the input board has only one solution.
 */

class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Initialize bitmasks for rows, columns, and boxes
        # Bit i is set if digit (i+1) is present
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        
        # Pre-fill the bitmasks with existing numbers
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    bit = 1 << num
                    box_idx = (i // 3) * 3 + (j // 3)
                    rows[i] |= bit
                    cols[j] |= bit
                    boxes[box_idx] |= bit
        
        # Backtracking function
        def backtrack(i, j):
            # If we've processed all rows, we've solved the sudoku
            if i == 9:
                return True
            
            # Move to the next row if we've finished the current row
            if j == 9:
                return backtrack(i + 1, 0)
            
            # If the cell is already filled, move to the next cell
            if board[i][j] != '.':
                return backtrack(i, j + 1)
            
            # Try digits 1-9
            for num in range(1, 10):
                bit = 1 << num
                box_idx = (i // 3) * 3 + (j // 3)
                
                # Check if the number is valid (not present in row, col, or box)
                if not (rows[i] & bit) and not (cols[j] & bit) and not (boxes[box_idx] & bit):
                    # Place the number
                    board[i][j] = str(num)
                    rows[i] |= bit
                    cols[j] |= bit
                    boxes[box_idx] |= bit
                    
                    # Recurse to the next cell
                    if backtrack(i, j + 1):
                        return True
                    
                    # Backtrack: remove the number
                    board[i][j] = '.'
                    rows[i] &= ~bit
                    cols[j] &= ~bit
                    boxes[box_idx] &= ~bit
            
            return False
        
        backtrack(0, 0)
