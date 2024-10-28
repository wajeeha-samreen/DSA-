class Solution(object):
    def exist(self, board, word):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, word, i, j): return True
        return False
                
    def dfs(self, board, word, i, j):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] == -1 or board[i][j] != word[0]:
            return False
        if len(word) == 1:
            return True
        
        temp, board[i][j] = board[i][j], -1
        if (self.dfs(board, word[1:], i-1, j) or 
            self.dfs(board, word[1:], i+1, j) or 
            self.dfs(board, word[1:], i, j-1) or 
            self.dfs(board, word[1:], i, j+1)):
            return True
        
        board[i][j] = temp
        return False

