class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        result = []
        newStart, newEnd = newInterval
        
        for interval in intervals:
            start, end = interval
            if (newStart <= end <= newEnd) or (newStart <= start <= newEnd) or (start <= newStart <= end):
                if result and [newStart, newEnd] == result[-1]:
                    result.pop()
                merged = [min(start, newStart), max(end, newEnd)]
                result.append(merged)
                newStart, newEnd = result[-1]
                
            elif [newStart, newEnd] == newInterval and start > newEnd and (not result or result[-1][1] < newStart):
                result.append(newInterval)
                result.append(interval)
                newStart, newEnd = -1, -1
            else:
                result.append(interval)
        else:
            if result and result[-1][1] < newStart:
                result.append(newInterval)
                
        return result or [newInterval]