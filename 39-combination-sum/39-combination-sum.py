class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []
        
        def dfs(current, currentSum, curIdx):
            
            for idx, candidate in enumerate(candidates[curIdx:]):
                
                if currentSum + candidate < target:
                    dfs(current + [candidate], currentSum + candidate, curIdx + idx)
                elif currentSum + candidate == target:
                    result.append(current + [candidate])
                    
        dfs([], 0, 0)
        return result