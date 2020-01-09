class MyQueue:

    def __init__(self):
        self.q = [] #初始化給個空間

    def push(self, x: int) -> None:
        self.q.append(x) #新增一個資料在最尾端

    def pop(self) -> int:
        pop_q = self.q[0] #移除最前面的資料，並回傳那個值
        self.q[:] = self.q[1:]
        return pop_q

    def peek(self) -> int:
        return self.q[0] #獲取最前面的元素

    def empty(self) -> bool:
        if len(self.q) == 0: #判斷queue是否為空
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
