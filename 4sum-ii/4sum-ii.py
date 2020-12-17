class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        
        AB = defaultdict(int)
        result = 0
        
        for a in A:
            for b in B:
                AB[a+b] += 1
                
        for c in C:
            for d in D:
                result += AB[-(c+d)]
                
        return result
                
