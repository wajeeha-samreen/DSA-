class Solution:
    def circularTour(self, a1, a2):
        n=len(a1)
        balance=0
        deflict=0
        start=0
        for i in range(n):
            balance+=a1[i]-a2[i]
            
            if balance<0:
                deflict+=balance 
                start=i+1
                balance=0
                
        
        if balance+deflict>=0:
            return start
            
        else:
            return -1 
            
