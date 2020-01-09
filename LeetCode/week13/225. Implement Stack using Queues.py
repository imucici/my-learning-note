class MyStack:

    def __init__(self):
        self.s = []
        self.temp = []
    def push(self, x: int) -> None:
        self.s.append(x)
        

    def pop(self) -> int: #移除並回傳
        if len(self.s) >=1:
            s = self.s[:-1]
            for i in s:
                self.temp.append(i)
                self.s.pop(0)
                
            ans = self.s[0]
            self.s = []
            for i in self.temp:
                self.s.append(i)
            self.temp = []
            return ans
        
    def top(self) -> int:
        if len(self.s) >=1:
            s = self.s[:-1]
            for i in s:
                self.temp.append(i)
                self.s.pop(0)
                
            ans = self.s[0]
            self.temp.append(self.s[0])
            self.s.pop(0)
            
            for i in self.temp:
                self.s.append(i)
            self.temp = []
            return ans
        

    def empty(self) -> bool:
        if len(self.s) == 0:
            return True
        else:
            return False
