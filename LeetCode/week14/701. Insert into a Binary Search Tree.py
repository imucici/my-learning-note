# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        Solution().help(root,val)
        return root
    def help(self, root: TreeNode, val: int) -> TreeNode:
        if val < root.val:
            if root.left == None:
                root.left = TreeNode(val)
                
            else:
                Solution().help(root.left,val)
        elif val > root.val:
            if root.right == None:
                root.right = TreeNode(val)
                
            else:
                Solution().help(root.right,val)
