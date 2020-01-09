class MinStack:

    def __init__(self):
    
        self.item = [] #初始化給個空間

    def push(self, x: int) -> None:
        self.item.append(x) #新增一個元素在最List最末端(Stack的頂端)

    def pop(self) -> None:
        self.item.pop() #移除List最後一個值(Stack的頂端)
        

    def top(self) -> int:
        return self.item[-1] #回傳List最後一個值(Stack的頂端)

    def getMin(self) -> int:
        return min(self.item) #回傳最小值
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
