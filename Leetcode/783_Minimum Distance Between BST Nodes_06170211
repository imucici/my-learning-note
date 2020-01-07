# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        if root == None:
            return root.val
        else:
            a = self.pre(root,[])
            d = []
            d.append(abs(a[0]-a[1]))
            
            for i in range(1,len(a)-1):
                if d[0] > abs(a[i]-a[i+1]):
                    d[0] = abs(a[i]-a[i+1])
            return d[0]
        
    def pre(self,root,arr):
        if root.left != None:
            self.pre(root.left,arr)
        arr.append(root.val)
        if root.right != None:
            self.pre(root.right,arr)
        return arr
