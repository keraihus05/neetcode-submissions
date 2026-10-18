class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            col_seen = set()
            row_seen = set()
            for row in board:
                if row[i] == ".":
                    continue
                elif row[i] in col_seen:
                    return False
                else:
                    col_seen.add(row[i])
            for j in range(len(board[i])):
                    if board[i][j] == '.':
                        continue
                    elif board[i][j] in row_seen:
                        return False
                    else:
                        row_seen.add(board[i][j])
        for i in [0,3,6]:
            for j in [0,3,6]:
                mat_seen = set()
                for k in range(i,i+3):
                    for l in range(j,j+3):
                        if board[k][l] == '.':
                            continue
                        elif board[k][l] in mat_seen:
                            return False
                        else:
                            mat_seen.add(board[k][l])


        return True
