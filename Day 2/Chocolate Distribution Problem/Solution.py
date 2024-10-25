class Solution:

    def findMinDiff(self, arr,M):

        # code here
        arr.sort()
        
        i = 0
        j = M -1
        res = float('inf')
        while(j<len(arr)):
            
            curr = arr[j] - arr[i]
            res = min(curr,res)
            
            i+=1
            j+=1
        return res   
