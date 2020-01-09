# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        s = []
        a = Solution().pre(root,s)
        if len(set(a)) == 1:
            return True
        else:
            return False
    def pre(self,root,s):
        s.append(root.val)
        if root.left != None:
            Solution().pre(root.left,s)
        if root.right != None:
            Solution().pre(root.right,s)
        return s
