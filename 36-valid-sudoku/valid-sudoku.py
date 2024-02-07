class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(len(board)):
            column = []
            row = []
            for j in range(len(board)):
                if board[j][i] != '.':
                    row.append(board[j][i])
                if board[i][j] != '.':
                    column.append(board[i][j])
            if len(row) != len(set(row)):
                return False
            if len(column) != len(set(column)):
                return False

        def subBox(values):
            final = []
            for num in values:
                if num != '.':
                    final.append(num)
            if len(final) == len(set(final)):
                return True
            return False
            
        for i in range(len(board)):
            for j in range(len(board)):
                if i == 1:
                    if j == 1 or j == 4 or j == 7:
                        values = [board[i][j],board[i][j-1],board[i][j+1],
                        board[i-1][j],board[i-1][j-1],board[i-1][j+1],
                        board[i+1][j],board[i+1][j-1],board[i+1][j+1]]
                        if not subBox(values):
                            return False
                elif i == 4:
                    if j == 1 or j == 4 or j == 7:
                        values = [board[i][j],board[i][j-1],board[i][j+1],
                        board[i-1][j],board[i-1][j-1],board[i-1][j+1],
                        board[i+1][j],board[i+1][j-1],board[i+1][j+1]]
                        if not subBox(values):
                            return False
                elif i == 7:
                    if j == 1 or j == 4 or j == 7:
                        values = [board[i][j],board[i][j-1],board[i][j+1],
                        board[i-1][j],board[i-1][j-1],board[i-1][j+1],
                        board[i+1][j],board[i+1][j-1],board[i+1][j+1]]
                        if not subBox(values):
                            return False
                else:
                    continue
        
                        

        
        return True

        