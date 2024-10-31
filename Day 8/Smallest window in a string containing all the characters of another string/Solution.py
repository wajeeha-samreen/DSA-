#User function Template for python3
class Solution:
    
    #Function to find the smallest window in the string s1 consisting
    #of all the characters of string s2.
    def smallestWindow(self, s1, s2):
        #code here
        d={}
        for i in s2:
            if i not in d:
                d[i] =1
            else:
                d[i]+=1
        total=len(s2)
        st=0
        en=0
        ind=-1
        ans=99999999999
        while en<len(s1):
            
            if s1[en] in d :
                d[s1[en]]-=1
            if s1[en] in d and d[s1[en]]>=0:
                total-=1
                
            while total<=0 and st<=en:
                if en-st+1<ans:
                    ans=en-st+1
                    ind=st
                if s1[st] in d :
                    d[s1[st]]+=1
                if s1[st] in d and d[s1[st]]>0:
                    total+=1
                st+=1
                    
            en+=1
        if ind==-1:
            return -1
        return s1[ind:ind+ans]
            
