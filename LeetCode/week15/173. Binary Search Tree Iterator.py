# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.ans = self.pre(root,[])
    
    def next(self) -> int:
        if len(self.ans) != 0:
            a = self.ans.pop(0)
            return a

    def hasNext(self) -> bool:
        if len(self.ans) != 0:
            return True
        else:
            return False
        
    def pre(self,root,arr):
        if root == None:
            return arr
        
        if root.left != None:
            self.pre(root.left,arr)
        arr.append(root.val)
        if root.right != None:
            self.pre(root.right,arr)
        return arr
    
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
