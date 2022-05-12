class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        
        def houseRobberI(nums: List[int]) -> int:
            money = nums[0:2] + [0]
            
            cur = nums[0] + nums[2]
            money[2] = cur
            for num in nums[3:]:
                cur = num + max(money[-2], money[-3])
                money[0], money[1], money[2] = money[1], money[2], cur
            
            return max(money)
        
        
        return max(houseRobberI(nums[1:]), houseRobberI(nums[:-1]))