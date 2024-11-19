class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        res = 0
        stack = [float('inf')]

        for i in arr:
            while stack[-1] <= i:
                mid = stack.pop()
                res += mid * min(stack[-1], i)

            stack.append(i)
        
        while len(stack) > 2:
            res += stack.pop() * stack[-1]
        
        return res
