def populateSubLists(num: int, numlists: List[int]) -> Set[int]:
    result = []
    
    for numlist in numlists:
        result.append(numlist + [num])
    
    return result
    

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        
        for num in nums:
            result += populateSubLists(num, result)
            
        return result
            