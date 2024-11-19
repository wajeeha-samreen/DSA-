class Solution:

    #Function to find minimum time required to rot all oranges. 
    def orangesRotting(self, mat):
        q = []
        num_rows = len(mat)
        num_cols = len(mat[0])
        fresh_oranges = 0
    
    
        visited = [[False] * num_cols for _ in range(num_rows)]
        level = 0
        for i in range(num_rows):
            for j in range(num_cols):
                if mat[i][j] == 2:
                    q.append((i, j, level))
                elif mat[i][j] == 1:
                    fresh_oranges += 1
        
        offsets = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        while q:
            r, c, level = q.pop(0)
            visited[r][c] = True
            for ro, co in offsets:
                nr = r + ro
                nc = c + co
                inbound = nr >= 0 and nc >=0 and nr < num_rows and nc < num_cols
                if inbound and not visited[nr][nc] and mat[nr][nc] == 1:
                    mat[nr][nc] = 2 # make it rotten
                    fresh_oranges -= 1
                    q.append((nr, nc, level + 1))
        
        
        return -1 if fresh_oranges > 0 else level
                    
            
