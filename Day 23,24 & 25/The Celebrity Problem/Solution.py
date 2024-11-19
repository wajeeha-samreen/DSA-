class Solution:
    def celebrity(self, mat):
        # code here
        n=len(mat)
        
        top=0
        bottom=n-1
        
        while top<bottom:
            if mat[top][bottom]==1:
                top+=1
            else:
                bottom-=1
        
        for i in range(n):
            if top!=i:
                if mat[top][i]!=0 or mat[i][top]!=1:
                    return -1
        return top
