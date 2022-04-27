
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        
        for num in nums:
            temp = []
            for sset in result:
                temp.append(sset + [num])
            result += temp
    
            
        return result
            