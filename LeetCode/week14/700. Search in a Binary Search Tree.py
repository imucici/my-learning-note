# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        
        if val == root.val:
            return root
        
        elif val < root.val :
            if root.left == None:
                return None
            else:
                return Solution().searchBST(root.left,val)
        else:
            if root.right == None:
                return None
            else:
                return Solution().searchBST(root.right,val)
