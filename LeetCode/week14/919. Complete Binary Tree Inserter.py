# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        self.size = helper().pre(root,[])
        
    def insert(self, v: int) -> int:
        if self.root == None:
            self.root = TreeNode(v)
            self.size += 1
            return None
        elif self.root.left == None:
            self.root.left = TreeNode(v)
            self.size += 1
            return self.root.val
        elif self.root.right == None:
            self.root.right = TreeNode(v)
            self.size += 1
            return self.root.val
        arr = []
        size = self.size // 2
        while size != 1:
            arr.append(size)
            size = size // 2   
        arr = arr[::-1]
        
        cur = self.root
        for i in arr:
            if i %2 == 1:
                cur = cur.right
            else:
                cur = cur.left
        if self.size % 2 == 0:
            cur.left = TreeNode(v)
        else:
            cur.right = TreeNode(v)
        self.size += 1
        return cur.val
        
    def get_root(self) -> TreeNode:
        return self.root

class helper:  
    def pre(self,root,lst):
        if root == None:
            return len(lst) + 1
        else:   
            lst.append(root.val)
            if root.left != None:
                helper().pre(root.left,lst)
            if root.right != None:
                helper().pre(root.right,lst)
            return len(lst) + 1
# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()
