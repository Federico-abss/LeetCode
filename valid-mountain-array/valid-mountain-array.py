class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        if len(arr) < 3 or arr[0] > arr[1] or arr[-1] > arr[-2]:
            return False
        
        desc = False
        
        for i in range(1, len(arr)):
            
            if arr[i] == arr[i-1] or (arr[i] > arr[i-1] and desc):
                return False
            
            if arr[i] < arr[i-1]:
                desc = True
                
        return True
                
        
​
