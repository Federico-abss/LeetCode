class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        
        def houseRobberI(nums: List[int]) -> int:
            money = [0] * len(nums)
            money[0:2] = nums[0:2]
            
            for idx, num in enumerate(nums[2:], 2):
                if idx < 3:
                    money[idx] = num + nums[idx-2]
                    continue
                
                money[idx] = num + max(money[idx-3], money[idx-2])
            
            return max(money[-2:])
        
        
        return max(houseRobberI(nums[1:]), houseRobberI(nums[:-1]))