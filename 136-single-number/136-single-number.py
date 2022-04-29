class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        hashMap = defaultdict(int)
        for num in nums:
            hashMap[num] += 1
            
        for key, value in hashMap.items():
            if value == 1:
                return key