class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        numDict = defaultdict(list)
        for idx, num in enumerate(nums):
            numDict[num].append(idx)
            
        if len(numDict.keys()) == 1:
            if len(numDict[0]) > 2:
                return [[0,0,0]]
            else:
                return []
            
        results = set()
        nums = sorted(numDict.keys())
        
        for idx, num in enumerate(nums):
            for endIdx in range(len(nums)-1, idx-1, -1):
                candidate = -(num + nums[endIdx])
                if candidate in numDict:
                    if (candidate == num and candidate == nums[endIdx] and len(numDict[num]) > 2) or \
                        (candidate == num and nums[endIdx] != candidate and len(numDict[candidate]) > 1) or \
                        (nums[endIdx] == num and candidate != num and len(numDict[num]) > 1) or \
                        (candidate == nums[endIdx] and nums[endIdx] != num and len(numDict[candidate]) > 1) or \
                        (candidate != num and candidate != nums[endIdx] and num != nums[endIdx]):
                        results.add(tuple(sorted([num, nums[endIdx], candidate])))
                
                
        return results
                    
                    
        