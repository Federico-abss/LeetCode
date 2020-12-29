# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:        
        
        def dfs(node, nums, offEven):
                           
            nums[node.val] += 1
            if nums[node.val] % 2:
                offEven += 1
            else:
                offEven -= 1            
            
            if not node.left and not node.right: 
                nums[node.val] -= 1 
                if offEven <= 1:
                        return 1
                    
                return 0
            
            left = right = 0
            if node.left:
                left = dfs(node.left, nums, offEven)
            if node.right:
                right = dfs(node.right, nums, offEven) 
            
            nums[node.val] -= 1                 
            return left + right
            
            
        return dfs(root, defaultdict(int), 0)
            
        
        
        
        
