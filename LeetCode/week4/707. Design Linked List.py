class Node:
    
    def __init__ (self,val):
        self.val = val # 節點包含一個val和next字段
        self.next = None 

class MyLinkedList:

    def __init__(self):
       
        self.head = None # 先給一個空間(初始化Linked List為空)
        self.size = 0 

        
#當頭節點為空時，無法取值
#當index為負、超過鍊表長度時，無法獲取該位置的值
#當index、size皆=0 ，無法取值
    
    def get(self, index):
        
        if self.head == None or index <0 or index >= self.size :
            return -1
        else:
            count = 0
            current = self.head # 從頭開始遍歷
            while (index != count) : #當count還沒跑到指定index，繼續往下一個節點前進
                current = current.next
                count +=1
            return current.val #回傳指定index位置的值
        

    def addAtHead(self, val):
        new_head = Node(val)
        
        if self.head == None: #若為空鏈表，則新節點成為頭節點
            self.head = new_head
        else:
            new_head.next = self.head #更換掉舊的頭節點
            self.head = new_head # 指定新節點為頭節點
        self.size+=1

    def addAtTail(self, val):
        new_tail = Node(val)
        
        if self.head == None: #若為空鏈表，則新節點為頭節點
            self.head = new_tail
        else:
            current = self.head
            while current.next != None: #當頭節點下一個節點不為空，則將原始最後一個節點的字段指向新插入的節點
                current = current.next 
            current.next = new_tail 
        self.size+=1
    

#當index超過鍊表長度時，無法獲取該位置的值

    def addAtIndex(self, index, val):
        newindex =  Node(val)
        if index > self.size : # = size>>加尾巴
            return -1
        elif index <= 0:
            new=Node(val) # 給他一個空間，設新加入的節點為new
            new.next=self.head #更改原始頭節點
            self.head=new #插入的節點為新頭節點
            self.size+=1
        else:
            count = 0
            current = self.head #從頭開始遍歷
            while (count != index) :
                prev = current #新插入的節點需要用prev來找到上一個節點才能連接
                current = current.next
                count+=1
            new = Node(val) # 給他一個空間，設新加入的節點為new
            prev.next = new #將上一個節點的next字段連接到新插入的節點
            new.next = current #將新插入的節點的next字段連接到原始index位置的節點
            self.size+=1
        
#當頭節點為空時，無法取值
#當index為負、超過鍊表長度時，無法獲取該位置的值
#當index、size皆=0 ，無法取值        
        
    def deleteAtIndex(self, index): #刪除第index位置的節點
        if index < 0 or index >= self.size or self.head == None :
            return -1
        elif index == 0:
            self.head.val=None #刪除頭節點
            self.head=self.head.next #原始頭節點的下一個節點成為新頭節點
            self.size-=1
        else:
            count = 0
            current = self.head #從頭開始遍歷
            while( count != index ):
                prev = current
                current = current.next
                count+=1
            prev.next = current.next #將上一個節點prev的next字段連結到下一個節點
            current = None #移除欲刪除的節點
            self.size-=1
