from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def addEdge(self,u,v):
        self.graph[u].append(v)
        
    def BFS(self,s):
        temp = []
        q = []
        q.append(s)
        for k in self.graph[s]:
            temp.append(k)
        while len(temp) != 0:
            q.append(temp[0])
            for i in self.graph[temp[0]]:
                if i not in temp and i not in q:
                    temp.append(i)
            temp.pop(0)
        return q
    
    def DFS(self,s):
        temp = []
        stack = []
        stack.append(s)
        for k in self.graph[s]:
            temp.append(k)
        while len(temp) != 0:
            stack.append(temp[-1])
            cur = temp[-1]
            for i in self.graph[temp[-1]]:
                if i not in temp and i not in stack:
                    temp.append(i)
            temp.remove(cur)
        return stack
    
    
# 參考資料:   
# https://github.com/imucici/my-learning-note/blob/master/LeetCode/week4/155.%20Min%20Stack.ipynb
# https://github.com/imucici/my-learning-note/blob/master/LeetCode/week4/232.%20Implement%20Queue%20using%20Stacks.ipynb 
# https://github.com/imucici/my-learning-note/blob/master/LeetCode/week13/225.%20Implement%20Stack%20using%20Queues.ipynb
