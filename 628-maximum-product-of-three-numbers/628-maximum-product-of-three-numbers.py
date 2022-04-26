class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        
        maxNums = []
        minNums = []
        closestNegToZero = []
        
        for num in nums:
            if num < 0:
                if len(minNums) < 2:
                    minNums.append(num)
                    minNums.sort()
                else:
                    if num < minNums[-1]:
                        minNums.pop()
                        minNums.append(num)
                        minNums.sort()
                        
                if len(closestNegToZero) < 3:
                    closestNegToZero.append(num)
                    closestNegToZero.sort(reverse = True)
                else:
                    if num > minNums[-1]:
                        closestNegToZero.pop()
                        closestNegToZero.append(num)
                        closestNegToZero.sort(reverse = True)
                            
            if num >= 0:
                if len(maxNums) < 3:
                    maxNums.append(num)
                    maxNums.sort(reverse = True)
                else:
                    if num > maxNums[-1]:
                        maxNums.pop()
                        maxNums.append(num)
                        maxNums.sort(reverse = True)
                        
        
        if not maxNums:
            print(closestNegToZero)
            return prod(closestNegToZero)
        
        if len(nums) == 3:
            return prod(nums)
        
        if minNums and (prod(minNums) > prod(maxNums[1:])):
            return prod(minNums) * maxNums[0]
        else:
            return prod(maxNums)
        
        return 0
        
                    
                    