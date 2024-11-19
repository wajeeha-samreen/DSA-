class Solution:
    
    #Function to find maximum of minimums of every window size.
    def maxOfMin(self,arr,n):
        
        nse=[n]
        st=[(arr[n-1],n-1)]
        for i in range(n-2,-1,-1):
            while st and st[-1][0]>arr[i]:
                st.pop()
            if st:
                nse.append(st[-1][1])    
            else:
                nse.append(n)
            st.append((arr[i],i))
            
        # print(nse[::-1])
        
        nse=nse[::-1]
        
        pse=[-1]
        st=[(arr[0],0)]
        for i in range(1,n):
            while st and st[-1][0]>=arr[i]:
                st.pop()
            if st:
                pse.append(st[-1][1])    
            else:
                pse.append(-1)
            st.append((arr[i],i))
            
        # print(nse)
        # print(pse)
        ans=[0]*n
        for i in range(n):
            ind=nse[i]-pse[i]-1
            # print(ind)
            ans[ind-1]=max(ans[ind-1],arr[i])
            
        for i in range(n-2,-1,-1):
            ans[i]=max(ans[i],ans[i+1])
                
                
        # print(ans)
        
        return ans
            
        
                
