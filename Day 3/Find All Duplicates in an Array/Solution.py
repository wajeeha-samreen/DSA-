class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n=len(nums)
        p=10**5+3
        ans=[]
        for x in nums:
            next=(x%p)-1
            if nums[next]>p:
                ans.append(next+1)
            nums[next]+=p
        return ans
        
