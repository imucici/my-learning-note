from Cryptodome.Hash import MD5

class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
        
class MyHashSet:
    def __init__(self,capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
        
    def add(self,key):
        h = MD5.new()
        h.update(key.encode("utf-8"))
        enc = int(h.hexdigest(),16) # 加密過的結果
        rem = enc % self.capacity # 加入第幾條Linked List
#         print(rem)
        
        #整條Linked List為空，將新插入的節點當作新的頭節點
        if self.data[rem] == None:
            self.data[rem] = ListNode(enc)
#             return self.data[rem]
        
        elif self.data[rem].val == enc:
            pass
    
        else:
            #Linked List不為空，將新節點(不重複)插入Linked List尾端
            new = ListNode(enc)
            cur = self.data[rem]
            while cur.next != None and cur.next.val != enc:
                cur = cur.next
            if cur.next == None:
                cur.next = new
#             return cur.next
                   
    def show(self,n): #列出第n條Linked List內容
        count = 0
        cur = self.data[n]
        while cur != None:
            print("第",n,"條Linked List的第",count,"個是:",cur.val)
            cur = cur.next
            count+=1
            
            
    def contains(self,key):
        h = MD5.new()
        h.update(key.encode("utf-8"))
        enc = int(h.hexdigest(),16) #加密過的結果
        rem = enc % self.capacity #位於第幾條Linked List
        
        #整條Linked List為空，代表目標值不存在
        if self.data[rem] == None:
            return False
        else:
            #目標值在第0位
            if self.data[rem].val == enc :
                return True
            else:
                #目標值在中間
                cur = self.data[rem].next
                while cur != None and cur.val != enc :
                    cur = cur.next
                if cur == None:
                    return False
                else:
                    return True
                    
    def remove(self,key):
        h = MD5.new()
        h.update(key.encode("utf-8"))
        enc = int(h.hexdigest(),16) #加密過的結果
        rem = enc % self.capacity #位於第幾條Linked List
        
        #整條Linked List為空，代表目標值不存在
        if self.data[rem] == None:
            pass
        else:
            #目標值在第0位
            if self.data[rem].val == enc:
                self.data[rem] = self.data[rem].next

            else:
                #目標值在中間
                curp = self.data[rem]
                cur = self.data[rem].next
                while cur != None and cur.val != enc:
                    curp = cur
                    cur = cur.next
                if cur == None:
                    pass
                else:
                    curp.next = cur.next
                    cur = None


##參考資料:
# 1. https://github.com/imucici/my-learning-note/blob/master/LeetCode/week4/707.%20Design%20Linked%20List.ipynb
# 2. https://www.youtube.com/watch?v=9HFbhPscPU0
# 3. https://www.youtube.com/watch?v=2BldESGZKB8&feature=youtu.be
