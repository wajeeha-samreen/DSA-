from itertools import permutations
class Solution:
    def uniquePerms(self, arr, n):
        # code here 
        if arr.count(0)==n:
            return [arr]
        arr.sort()
        prem_set=set(permutations(arr))
        results=sorted(prem_set)
        return [list(prem) for prem in results]
