# 題目:反轉後再將0換成1、1換成0

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        lst = []
        for i in A:
            a = i[::-1]    
            lst.append(a)

        for j in range(len(lst)) :
            for k in range(len(lst[0])) :
                if lst[j][k] == 0:
                    lst[j][k] = 1
                else:
                    lst[j][k] = 0
        return lst
