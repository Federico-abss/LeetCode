class Solution:
    def minCostClimbingStairs(self, costs: List[int]) -> int:
        
        minCosts = [0,0] + [float('inf')]
        
        for idx, cost in enumerate(costs):
            minCosts[1] = min(minCosts[1], minCosts[0] + cost)
            minCosts[2] = min(minCosts[2], minCosts[0] + cost)
            if idx + 1 < len(costs):
                minCosts = minCosts[1:] + [float('inf')]
        
        return min(minCosts[-2:])

                
            