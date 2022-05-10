class Solution:
    def minCostClimbingStairs(self, costs: List[int]) -> int:
        
        minCosts = [float('inf')] * (len(costs)-1)
        minCosts = [0,0] + minCosts
        
        for idx, cost in enumerate(costs):
            minCosts[idx+1] = min(minCosts[idx+1], minCosts[idx] + cost)
            if idx + 2 < len(minCosts):
                minCosts[idx+2] = min(minCosts[idx+2], minCosts[idx] + cost)
        
        return minCosts[-1]

                
            