class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        result = [0] * len(temperatures)
        
        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                tempIdx = stack.pop()[1]
                result[tempIdx] = idx - tempIdx
            stack.append((temp,idx))
            
        return result
                
            