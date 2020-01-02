from collections import defaultdict 

class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
        self.edge = []
        self.wet = []
        self.root = {} #紀錄每條邊的root
        self.final = {} #最後要return的
        self.n = 0 #等到執行 self.V-1次即停止
        
    def addEdge(self,u,v,w): 
        self.edge.append([u,v])
        self.wet.append(w)

    def Dijkstra(self, s): #最短路徑
        lst2 = self.helper_d()
        
        path,pq = [s],[] # path用來記錄已走訪過的節點 ; pq用來找出最短路徑的vertex
        shortest , previous = {} , {}
        for i in range(self.V):
            shortest[i] , previous[i] = None , None
        shortest[s],previous[s] = 0 , None
        
        for i in range(self.V-1):
            a = lst2[path[-1]]
            for j in range(len(a)):
                vertex = a[j][0]
                if vertex not in path:
                    total = a[j][-1]+shortest[path[-1]]
                    if shortest[vertex] == None:
                        shortest[vertex] = total
                        previous[vertex] = path[-1]
                        pq.append([vertex,total])
                    else:
                        if total < shortest[vertex]:
                            shortest[vertex] = total
                            previous[vertex] = path[-1]
                            pq.append([vertex,total])
            
            temp = 1
            for k in range(len(pq)): #從pq中找出最短路徑的vertex
                if pq[k][0] not in path:
                    if temp == 1:
                        temp = pq[k]   
                    else:
                        if temp[-1] > pq[k][-1]:
                            temp = pq[k]
            
            path.append(temp[0])
            pq.remove(temp)

        final = {}
        for i in range(self.V):
            final[str(i)] = shortest[i]

        return final
    
    def helper_d(self): #每個點到與他相鄰的點的路徑長
        lst1 = []
        lst2 = [None]*self.V
        for i in range(self.V):
            for j in range(len(self.graph[i])):
                if self.graph[i][j] != 0:
                    lst1.append([j,self.graph[i][j]])
            lst2[i] = lst1
            lst1 = []
        return lst2
    
    
    
    def Kruskal(self):
        arr = sorted(list(zip(self.wet,self.edge))) #權重由小到大排
        
        for i in range(self.V):
            self.root[i] = None
            
        
        while self.n < self.V -1:
            self.helper(arr)
        
        return self.final
            
    def helper(self,arr):
        
        a = arr[0]
        
        s , b = min(a[1][0],a[1][1]) , max(a[1][0],a[1][1])
        
        det = True
        
        # 兩個input的root皆為空，統一指定成大的那個的root
        if self.root[s] == None and self.root[b] == None:
            self.root[s],self.root[b] = b,b
            self.n+=1
        
        # 小的那個root為空，且大的那個的root存在，把小的那個root指定成大的input的root
        elif self.root[s] == None and self.root[b] != None: 
            self.root[s] = self.root[b]
            self.n+=1
        
        # 大的那個root為空，且小的那個的root存在，把大的那個root指定成小的input的root
        elif self.root[b] == None and self.root[s] != None: 
            self.root[b] = self.root[s]
            self.n+=1
            
        # root皆存在且不相等，把所有root=小的那個改成大的root
        # (先處理非小的那個以外的，等出了迴圈再處理小的那個)
        elif self.root[s] != None and self.root[b] != None and self.root[s] != self.root[b]:
            for j in range(len(self.root)):
                if j != s and self.root[j] == self.root[s]:
                    self.root[j] = self.root[b]
            self.root[s] = self.root[b]
            self.n+=1
            
        # root皆存在且相等(會產生loop)，不加入(把那情況刪除)，進行recursive    
        elif self.root[s] != None and self.root[b] != None and self.root[s] == self.root[b]:
            det = False
            arr.pop(0)
            self.helper(arr)
                
        if det == True:
            self.final[str(a[1][0])+"-"+str(a[1][1])] = a[0]
            arr.pop(0)
            
            
# 參考資料:
# 1. https://www.youtube.com/watch?v=9wV1VxlfBlI
# 2. https://wiki.mbalib.com/zh-tw/Dijkstra%E7%AE%97%E6%B3%95
# 3. https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/434938/
# 4. https://www.youtube.com/watch?v=wuU4DDEUu1w
# 5. https://www.youtube.com/watch?v=71UQH7Pr9kU
