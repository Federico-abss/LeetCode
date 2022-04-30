class Solution:
    def numSquares(self, n: int) -> int:
        
        cache = dict()
        
        def perfectSquares(num: int):
            root = sqrt(num)
            roundedRoot = int(root)
            if root == roundedRoot:
                cache[num] = 1
                return 1
            
            minSteps = float("inf")
            for n in range(roundedRoot, 0, -1):
                if n ** 2 in cache:
                    minSteps = min(minSteps, 1 + perfectSquares(num - n ** 2))
                    break
                minSteps = min(minSteps, 1 + perfectSquares(num - n ** 2))
            
            cache[num] = minSteps
            return minSteps
        
        return perfectSquares(n)
            
            