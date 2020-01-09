# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def __init__(self):
        self.sum = 0
        self.det = True
        
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root == None or (root.left == None and root.right == None):
            return 0
        else:
            
            ans = Solution().helper(root)
            return ans
        
    def helper(self,root):
        if root.left:
            self.det = True
            self.helper(root.left)
        if root.right != None:
            self.det = False
            self.helper(root.right)
        if root.left == None and root.right == None and self.det == True:
            self.sum+=root.val
        return self.sum
