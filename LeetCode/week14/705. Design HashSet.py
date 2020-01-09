class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class MyHashSet:
    def __init__(self,capacity = 500):
        self.capacity = capacity
        self.data = [None]*capacity

    def add(self, key: int) -> None:
        rem = key % self.capacity
        
        if self.data[rem] == None:
            self.data[rem] = Node(key)
        elif self.data[rem].val == key:
            pass
        else:
            curp = self.data[rem]
            cur = self.data[rem].next
            while cur != None and cur.val != key:
                curp = cur
                cur = cur.next
            if cur == None:
                curp.next = Node(key)

    def remove(self, key: int) -> None:
        rem = key % self.capacity
        
        if self.data[rem] == None:
            pass
        elif self.data[rem].val == key:
            self.data[rem] = self.data[rem].next
        else:
            curp = self.data[rem]
            cur = self.data[rem].next
            while cur != None and cur.val != key:
                curp = cur
                cur = cur.next
            if cur == None:
                pass
            else:
                curp.next = cur.next
                cur = None

    def contains(self, key: int) -> bool:
        rem = key % self.capacity
        
        if self.data[rem] == None:
            return False
        elif self.data[rem].val == key:
            return True
        else:
            
            cur = self.data[rem].next
            while cur != None and cur.val != key:
                cur = cur.next
            if cur == None:
                return False
            else:
                return True
    


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
