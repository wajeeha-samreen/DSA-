class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        a=[]
        for i in s:
            if a and a[-1][0]==i:
                a[-1][1]+=1
                if a[-1][1]==k: a.pop()
            else: a.append([i,1])
        return ''.join(key*value for key, value in a)        
