def is_safe(M, r, c, visited):
    ROW = len(M)
    COL = len(M[0])
    return (r >= 0) and (r < ROW) and (c >= 0) and (c < COL) and (M[r][c] == '1' and not visited[r][c])

def DFS(M, r, c, visited):
    rNbr = [-1, -1, -1, 0, 0, 1, 1, 1]
    cNbr = [-1, 0, 1, -1, 1, -1, 0, 1]
    visited[r][c] = True
    for k in range(8):
        newR = r + rNbr[k]
        newC = c + cNbr[k]
        if is_safe(M, newR, newC, visited):
            DFS(M, newR, newC, visited)

def count_islands(M):
    ROW = len(M)
    COL = len(M[0])
    visited = [[False for _ in range(COL)] for _ in range(ROW)]
    count = 0
    for r in range(ROW):
        for c in range(COL):
            if M[r][c] == '1' and not visited[r][c]:
                DFS(M, r, c, visited)
                count += 1
    return count

if __name__ == "__main__":
    M = [['1', '1', '0', '0', '0'],
         ['0', '1', '0', '0', '1'],
         ['1', '0', '0', '1', '1'],
         ['0', '0', '0', '0', '0'],
         ['1', '0', '1', '1', '0']]
    
    print(count_islands(M))
