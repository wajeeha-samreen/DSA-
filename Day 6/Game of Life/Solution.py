class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        rowLen, colLen = len(board[0]), len(board)

        def inBound(i, j):
            return 0 <= i < colLen and 0 <= j < rowLen

        for i in range(colLen):
            for j in range(rowLen):
                live_neighbors = 0
                # Check all 8 possible neighbors
                for ii, jj in [(i, j+1), (i, j-1), (i-1, j), (i+1, j), 
                               (i-1, j+1), (i+1, j-1), (i+1, j+1), (i-1, j-1)]:
                    if inBound(ii, jj) and abs(board[ii][jj]) == 1:
                        live_neighbors += 1

                # Apply the rules with temporary states
                if board[i][j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[i][j] = -1  # Live cell dies
                if board[i][j] == 0 and live_neighbors == 3:
                    board[i][j] = 2  # Dead cell becomes live

        # Final pass to convert markers back to final state
        for i in range(colLen):
            for j in range(rowLen):
                if board[i][j] == -1:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1
