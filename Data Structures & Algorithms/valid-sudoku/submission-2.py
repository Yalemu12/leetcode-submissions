"""
We need to check if a number has already appeared in a specific row,column, or box
so a Set is the best data structure we can use for O(1) lookupa you will need
a way to store 9 sets for the rows 9 for the columns and the boxes

Rows and columns are easy to index but the 3x3 sqaures are trickier
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                # if the cell contains a . ignore it
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r]
                    or board[r][c]in columns[c]
                    or board[r][c] in squares[(r // 3, c // 3)]):
                    return False 
                columns[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        return True        


        