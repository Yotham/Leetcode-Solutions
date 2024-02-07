class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = defaultdict(list)
        columns = defaultdict(list)
        box = defaultdict(list)
        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] == '.':
                    continue
                else:
                    if (board[r][c] in rows[r]) or (board[r][c] in columns[c]) or (board[r][c] in box[r//3,c//3]):
                        return False
                columns[c].append(board[r][c])
                rows[r].append(board[r][c])
                box[r//3,c//3].append(board[r][c])
                

        
        return True

        