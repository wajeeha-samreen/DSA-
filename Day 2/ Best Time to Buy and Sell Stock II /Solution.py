import math

class Solution:
    def maxProfit(self, p):
        n = len(p)
        min_so_far, max_so_far = math.inf, 0
        
        for i in range(n):
            cur = p[i] - min_so_far
            max_so_far = max(cur, max_so_far)
            min_so_far = min(min_so_far, p[i])
        
        return max_so_far
