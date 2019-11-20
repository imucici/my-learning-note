class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    
    def insert(self,root,val):
        if val == root.val:
            new = TreeNode(val)
            new.left = root.left
            root.left = new
            #print("下面有節點的情況下，將相同的節點加到左邊")
            return root.left
        elif val < root.val: #跑到左邊
            if root.left == None:
                root.left = TreeNode(val)
                #print("新節點加到左邊")
                return root.left
            else:
                return Solution().insert(root.left,val)  
        elif val > root.val: #跑到右邊
            if root.right == None:
                root.right = TreeNode(val)
                #print("新節點加到右邊")
                return root.right
            else:
                return Solution().insert(root.right,val)    
   
    def pre(self,root,arr): # root-->left-->right
        
        if root == None:
            return arr
        arr.append(root.val)
        if root.left != None:
            Solution().pre(root.left,arr)
        if root.right != None:
            Solution().pre(root.right,arr)
        return arr
            
    def delete(self,root,target):  
        
        # case5: delete_node(不重複)為root，找左邊最大或右邊最小來補
        # case5-1: root只有right child
        if target == root.val and root.left == None and root.right != None:
            new = root.right
            root = None
            return new  

## case5-1測值:["10",12,11,10.5]
        
        elif target == root.val and root.left.val != target:
            # case5-2: root只有left child，直接將root.left指定為新root
            if root.right == None and root.left != None:
                new = root.left
                root = None
                return new
             
            # case5-3: root有左右小孩，找左或右小孩來補
            elif root.left.right == None and root.right.left == None:
                new = root.left
                new.right = root.right
                root = None
                return new
            # case5-4: d的左小孩只要有右小孩，找右小孩中最大的
            elif root.left.right != None:
                curp = root.left
                cur = root.left.right
                while cur.right != None:
                    curp = cur
                    cur = cur.right
                    
                curp.right = cur.left
                cur.right = root.right
                cur.left = root.left
                root = None
                return cur
        
            # case5-5: d的右小孩只要有左小孩，找左小孩中最小的
            elif root.right.left != None:
                curp = root.right
                cur = root.right.left
                while cur.left != None:
                    curp = cur
                    cur = cur.left
                    
                cur.left = root.left
                curp.left = cur.right    
                cur.right = root.right
                root = None
                return cur
        
        # case7: 刪除值(重複)在root  
        elif target == root.val and root.left.val == target:
            if root.left != None and root.right != None:
                end = root.left
                r = root.right
                while end.val == target:
                    root = end
                    end = end.left
                root.right = r
                
                if root.left.right != None:
                    curp = root.left
                    cur = root.left.right
                    while cur.right != None:
                        curp = cur
                        cur = cur.right
                    cur.right = root.right
                    cur.left = root.left
                    curp.right = None
                    return cur
## case7-1測值:["10","10","10",6,5,6.5,6.7,6.6,12,11,14]

                elif root.right.left != None:
                    curp = root.right
                    cur = root.right.left
                    while cur.left != None:
                        curp = cur 
                        cur = cur.left
                    cur.right = root.right
                    cur = left = root.left
                    curp.left = None
                    root = None
                    return cur
## case7-2測值:[""10","10","10",6,5,12,11,10.5,10.6,14"]

            # case7-3:root只有右小孩，直接將root.right指定為新root
            elif root.left == None and root.right != None:
                root = root.right
                return root
## case7-3測值:["10",20,19,21]

            # case7-4:root只有左小孩，直接將root.left指定為新root
            elif root.right == None and root.left != None :
                while root.left != None and root.left.val == target :
                    root = root.left
                if root.left == None:
                    return None
                else:
                    root = root.left
                    return root

        p = None
        d = root 
    
        #先找到要刪除的那個node
        while target != d.val:
            if target <= d.val:
                if d.left == None:
                    return root
                else:
                    p = d
                    d = d.left
            elif target > d.val:
                if d.right == None:
                    return root
                else:
                    p = d
                    d = d.right

        # case1:delete_node沒有任何小孩，直接將delete_node刪除
        if d.left == None and d.right == None:
            # case1-1:delete_node比parent小，將parent左小孩指向空
            if d.val < p.val:
                p.left = None
                return root
            #case1-2:delete_node比parent大，將parent右小孩指向空
            elif d.val > p.val:
                p.right = None
                return root
        
        # case3:delete_node 只有右邊的小孩(找右邊小孩中最小的來補)
        elif d.left == None and d.right != None:
            # case3-1: p.left = d，且d.left只有left child
            if p.left == d and d.right.left == None and d.right.right != None:
                p.left = d.right
                return root
## case3-1測值:[9,8,"7",7.1,7.2,7.3]

            # case3-2: p.left = d，且d.right只有left child
            elif p.left == d and d.right.right == None and d.right.left != None:
                cur = d.right.left
                curp = d.right
                while cur.left != None:
                    curp = cur
                    cur = cur.left
                p.left = cur
                cur.right = d.right
                d = None
                curp.left = None
                return root
## case3-2測值:[9,8,"7",7.1,7.05,7.03,7.06,7.07]  

            # case3-3: p.left = d，且d.right有right child & left child
            elif p.left == d and d.right.left != None and d.right.right != None:
                cur = d.right.left
                curp = d.right
                while cur.left != None:
                    curp = cur
                    cur = cur.left
                p.left = cur
                curp.left = cur.right
                cur.right = d.right
                d = None
                return root
## case3-3測值:[9,8,"7",7.1,7.05,7.03,7.06,7.07,7.2,7.3]

            # case3-4: p.right = d，且d.right只有right child
            elif p.right == d and d.right.left == None and d.right.right != None:
                p.right = d.right
                return root
## case3-4測值:[9,10,"20",22,24]

            # case3-5: p.right = d，且d.right只有left child
            elif p.right == d and d.right.right == None and d.right.left != None:
                cur = d.right.left
                curp = d.right
                while cur.left != None:
                    curp = cur
                    cur = cur.left
                p.right = cur
                cur.right = d.right
                d = None
                curp.left = None
                return root
## case3-5測值:[9,10,"20",22,21.5,21,21.6,21.7] 

            # case3-6: p.right = d，且d.right有right child & left child
            elif p.right == d and d.right.left != None and d.right.right != None:
                cur = d.right.left
                curp = d.right
                while cur.left != None:
                    curp = cur
                    cur = cur.left
                p.right = cur
                curp.left = cur.right
                cur.right = d.right
                d = None
                return root
## case3-6測值:[9,10,"20",22,21.5,21,21.6,21.7,24] 

        #第一大類:BST中沒有重複值
        elif root.val != target:
            
            # case2:delete_node 只有左邊的小孩(找左邊小孩中最大的來補)
            if d.left != None and d.right == None:
                # case2-1: p.left = d，且d.left只有left child
                if p.left == d and d.left.right == None and d.left.left != None:
                    p.left = d.left
                    return root
## case2-1測值:[9,8,"7",6,5]
                    
                # case2-2: p.left = d，且d.left只有right child
                elif p.left == d and d.left.left == None and d.left.right != None:
                    cur = d.left.right
                    curp = d.left
                    while cur.right != None:
                        curp = cur
                        cur = cur.right
                    p.left = cur
                    cur.left = d.left
                    d = None
                    curp.right = None
                    return root
## case2-2測值:[9,8,"7",6,6.5,6.4,6.3,6.45,6.8]
                    
                # case2-3: p.left = d，且d.left有right child & left child
                elif p.left == d and d.left.left != None and d.left.right != None:
                    cur = d.left.right
                    curp = d.left
                    while cur.right != None:
                        curp = cur
                        cur = cur.right
                    p.left = cur
                    curp.right = cur.left
                    cur.left = d.left
                    d = None
                    return root
## case2-3測值:[9,8,"7",6,5,6.5,6.4,6.3,6.45,6.8]
                
                # case2-4: p.right = d，且d.left只有left child
                elif p.right == d and d.left.right == None and d.left.left != None:
                    p.right = d.left
                    return root
## case2-4測值:[9,10,"11",10.5,10.4]

                # case2-5: p.right = d，且d.left只有right child
                elif p.right == d and d.left.left == None and d.left.right != None:
                    cur = d.left.right
                    curp = d.left
                    while cur.right != None:
                        curp = cur
                        cur = cur.right
                    p.right = cur
                    cur.left = d.left
                    d = None
                    curp.right = None
                    return root
## case2-5測值:[9,10,"11",10.5,10.55,10.54,10.53,10.56,10.65]

                # case2-6: p.right = d，且d.left有right child & left child
                elif p.right == d and d.left.left != None and d.left.right != None:
                    cur = d.left.right
                    curp = d.left
                    while cur.right != None:
                        curp = cur
                        cur = cur.right
                    p.right = cur
                    curp.right = cur.left
                    cur.left = d.left
                    d = None
                    return root
## case2-6測值:[9,10,"11",10.5,10.4,10.55,10.54,10.53,10.56,10.65]

            # case4:delete_node 有左右兩邊的小孩(找左邊小孩中最大或右邊最小的來補) 
            elif d.left != None and d.right != None:
                # case4-1:找左邊最大
                if p.right == d and d.left.right != None:
                    cur = d.left.right
                    curp = d.left
                    while cur.right != None:
                        curp = cur
                        cur = cur.right
                    
                    p.right = cur
                    curp.right = cur.left
                    cur.left = d.left
                    cur.right = d.right
                    d = None
                    return root
                # case4-1:找右邊最小
                elif p.right == d and d.right.left != None:
                    cur = d.right.left
                    curp = d.right
                    while cur.left != None:
                        curp = cur
                        cur = cur.left
                    
                    p.right = cur
                    curp.left = cur.right
                    cur.right = d.right
                    cur.left = d.left
                    d = None
                    return root
## case4-1測值:[9,10,"11",10.5,10.4,10.55,10.65,22,21,5,21,24]
                # case4-2:找左邊最大
                elif p.left == d and d.left.right != None:
                    cur = d.left.right
                    curp = d.left
                    while cur.right != None:
                        curp = cur
                        cur = cur.right
                    
                    p.left = cur
                    curp.right = cur.left
                    cur.left = d.left
                    cur.right = d.right
                    d = None
                    return root
                # case4-2:找右邊最小
                elif p.left == d and d.right.left != None:
                    cur = d.right.left
                    curp = d.right
                    while cur.left != None:
                        curp = cur
                        cur = cur.left
                    
                    p.left = cur
                    curp.left = cur.right
                    cur.right = d.right
                    cur.left = d.left
                    d = None
                    return root
## case4-2測值:[9,8,"7",6,5,5.5,6.5,6.4,6.7,6.75,7.1,7.05,7.03,7.2]
                # case4-3:d.left.right為空且d.right.left為空
                elif d.left.right == None and d.right.left == None:
                    if p.left != None and p.left == d:
                        p.left = d.left
                    else:
                        p.right = d.left
                    d.left.right = d.right
                    d = None
                    return root
        #第二大類:BST中有重複值
        
        elif d.left.val == target:
            # case6-1: 刪除值不在root且p.left = d
            if p.left == d:
                end = d.left
                while end.val == target:
                    d = end
                    end = end.left
                end.right = p.left.right
                p.left = end
                return root
## case6-1測值:[10,"6",6.5,"6","6",5,12]

            # case6-2: 刪除值不在root且p.righ = d
            elif p.right == d:
                end = d.left
                while end.val == target:
                    d = end
                    end = end.left
                end.right = p.right.right
                p.right = end
                return root
##case6-2測值:[10,"12",13,"12","12",11]
  
    def search(self,root,target): #因為助教要的是離root最近的target，因此只要找到第一個target就可以return 
        if target  == root.val:
            return root
        elif target < root.val :
            if root.left == None:
                return False
            else:
                return Solution().search(root.left,target)
        elif target > root.val:
            if root.right == None:
                return False
            else:
                return Solution().search(root.right,target)
            
    def modify(self,root,target,new_val):
        if target != new_val: #先新增再刪除相較之下是較適當且較快速的方式
            Solution().insert(root,new_val)
            return Solution().delete(root,target)
        else: #當修改前後的值相同，直接用修改前的tree做preorder
            return root
