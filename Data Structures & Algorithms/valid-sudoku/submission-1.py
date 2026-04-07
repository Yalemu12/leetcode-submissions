class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # this is a duplicate detetion problem across three dimensions 
        #rows columns and boxes 
        # and we need to use hash sets 

        # Plan:
        # prepare three arrays of 9 sets each for rows, columns, and boxes
        # for every cell:
        # if it's '.' continue
        # if the digit already exista in rows[r] or cols[c] or boxes[boxes_id] then return False
        #otherwise we will insert it into those sets 
        #if the loop finishes with no conflicta then we return true 

        #these are the sets to record the seen digits in rows columns and the 3x3 box
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                ch = board[r][c]
                if ch == '.':
                    continue


                b = (r // 3) * 3 + (c // 3) # this is to compute the box_id

                #condition if th duplicate is found 
                if (ch in rows[r]) or(ch in columns[c]) or (ch in boxes[b]):
                    return False
                
                #mark as seen 
                rows[r].add(ch)
                columns[c].add(ch)
                boxes[b].add(ch)

        return True            


                


       

        