class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        minCoin = [0] + [float('inf') for _ in range(amount)]
        
        for idx, comb in enumerate(minCoin):
            for coin in coins:
                if idx + coin < len(minCoin):
                    minCoin[idx + coin] = min(minCoin[idx + coin], comb+1)
                        
        return minCoin[-1] if minCoin[-1] != float('inf') else -1
                    