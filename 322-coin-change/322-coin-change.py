class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        global reached
        reached = False
        
        @cache
        def change(amount: int) -> int:
            if not amount:
                global reached 
                reached = True
                return 0
            
            minChange = float('inf')
            for coin in coins:
                if coin <= amount:
                    minChange = min(minChange, 1 + change(amount - coin))
                    
            return minChange
        
        minChange = change(amount)
        return minChange if reached else -1
                    