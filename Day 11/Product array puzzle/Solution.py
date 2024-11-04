class Solution:
    def productExceptSelf(self, arr):
        #code here
        res=[1]* len(arr)
        p=1
        for i in range(len(arr)):
            res[i]*=p
            p*=arr[i]
        post=1
        for i in range(len(arr) -1,-1,-1):
            res[i]*=post
            post*=arr[i]
        return res
