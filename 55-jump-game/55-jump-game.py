class Solution:
    def canJump(self, nums: List[int]) -> bool:

        if len(nums) == 1:
            return True
        
        @lru_cache(maxsize=None)
        def jumps(idx: int) -> bool:
            jump = nums[idx]
            if not jump:
                return False

            if idx + jump >= len(nums) - 1:
                return True

            for num in range(jump, 0, -1):
                if jumps(idx + num):
                    return True

            return False
        
        return jumps(0)
        

        