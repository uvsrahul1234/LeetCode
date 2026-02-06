class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set) # Key: (r // 3, c // 3)
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                # Check for duplicates
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                
                # Add number to sets
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
                
        return True

        # Brute Force T:(N2) S:O(N)
    #     for i in board:
    #         count = defaultdict(int)
    #         for j in i:
    #             if j != '.':
    #                 count[j] += 1
    #                 if count[j] > 1:
    #                     return False
        
    #     for i in range(9):
    #         count = defaultdict(int)
    #         for j in range(9):
    #             if board[j][i] != '.':
    #                 count[board[j][i]] += 1
    #                 if count[board[j][i]] > 1:
    #                     return False
        
    #     if self.isValidBox(board, 0, 3, 0, 3) and self.isValidBox(board, 0, 3, 3, 6) and self.isValidBox(board, 0, 3, 6, 9) and self.isValidBox(board, 3, 6, 0, 3) and self.isValidBox(board, 3, 6, 3, 6) and self.isValidBox(board, 3, 6, 6, 9) and self.isValidBox(board, 6, 9, 0, 3) and self.isValidBox(board, 6, 9, 3, 6) and self.isValidBox(board, 6, 9, 6, 9):
    #         return True
    #     else:
    #         return False
        
        
    #     return True

    # def isValidBox(self, board, tr, br, lc, rc) -> bool:
    #     count = defaultdict(int)
    #     for i in range(tr, br):
    #         for j in range(lc, rc):
    #             if board[i][j] != '.':
    #                 count[board[i][j]] += 1
    #                 if count[board[i][j]] > 1:
    #                     return False
    #     return True