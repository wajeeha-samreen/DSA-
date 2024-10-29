class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        stack, ans = deque(), -inf
        for x, y in points:
            while stack and abs(stack[0][0] - x) > k:
                stack.popleft()
            if stack:
                ans = max(ans, x + y + stack[0][1])
            while stack and stack[-1][1] <= y - x:
                stack.pop()
            stack.append((x, y - x))
        return ans
