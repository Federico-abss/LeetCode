class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda x: (x[0], x[1]))
        result = [intervals[0]]
        
        for interval in intervals[1:]:
            cur = result[-1]
            if cur[-1] >= interval[0]:
                cur[-1] = max(cur[-1], interval[-1])
            else:
                result.append(interval)
                
        return result