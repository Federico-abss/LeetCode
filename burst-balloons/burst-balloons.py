from functools import lru_cache
​
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
​
        # reframe the problem
        nums = [1] + nums + [1]
​
        # cache this
        @lru_cache(None)
        def dp(left, right):
​
            # no more balloons can be added
            if left + 1 == right: return 0
​
            # add each balloon on the interval and return the maximum score
            return max(nums[left] * nums[i] * nums[right] + dp(left, i) + dp(i, right) for i in range(left+1, right))
​
        # find the maximum number of coins obtained from adding all balloons from (0, len(nums) - 1)
        return dp(0, len(nums)-1)
​
