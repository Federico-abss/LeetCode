class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
       
        hmap = defaultdict(list)
        minVal = float("inf")
        
        for idx, num in enumerate(A):
            if num < 0:
                hmap[num].append(idx)
            minVal = min(minVal, abs(num))
                
        nums = sorted(hmap.keys())
        
        for num in nums:
            
            if not K:
                break
                
            for idx in hmap[num]:
                
                if not K:
                    break
                    
                A[idx] = -num
                K -= 1
                
        if K % 2:
            A.append(-2*minVal)
                
        
        return sum(A)
