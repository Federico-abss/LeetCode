class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda x: x[0])
        curIdx = 0
        
        for idx, interval in enumerate(intervals[1:], 1):
            cur = intervals[curIdx]
            if cur[-1] >= interval[0]:
                cur[-1] = max(cur[-1], interval[-1])
                print(cur)
            else:
                curIdx += 1
                intervals[curIdx] = interval
                
        return intervals[:curIdx+1]