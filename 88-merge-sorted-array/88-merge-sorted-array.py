class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        idx2 = 0
        for idx in range(m, len(nums1)):
            nums1[idx] = nums2[idx2]
            idx2 += 1
                
        nums1.sort()
                