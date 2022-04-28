class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        idx2 = cur = 0
        temp = []
        
        for num in nums1[:m]:
            while idx2 < n and nums2[idx2] <= num:
                temp.append(nums2[idx2])
                idx2 += 1
                
            temp.append(num)
            
        temp += nums2[idx2:]
        for idx, num in enumerate(temp):
            nums1[idx] = num
                
        
                