class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        
        stk, days = [], [0] * len(temp)
        
        for i, currTemp in enumerate(temp):
            while stk and temp[stk[-1]] < currTemp:
                unsettledDay = stk.pop()
                days[unsettledDay] = i - unsettledDay
                
            stk.append(i)
            
        return days
