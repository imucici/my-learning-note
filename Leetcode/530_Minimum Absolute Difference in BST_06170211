
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        if root:
            a = self.inorder(root,[])
            
            d = []
            d.append(abs(a[0]-a[1]))
            for i in range(1,len(a)-1):
                if abs(a[i]-a[i+1]) < d[0]:
                    d[0] = abs(a[i]-a[i+1])
            return d[0]
    def inorder(self,root,arr):
        if root.left != None:
            self.inorder(root.left,arr)
        arr.append(root.val)
        if root.right != None:
            self.inorder(root.right,arr)
        return arr
