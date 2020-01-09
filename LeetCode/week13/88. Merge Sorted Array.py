# 由後往前排

class Solution:
    def merge(self, n1, m, n2, n) -> None:
        if n2 == None:
            pass
        if n1 == None:
            n1 = n2
        else:
            i=-1

            while n>0:
                n1[i] = n2[i]
                n-=1
                i-=1
                
            a = sorted(n1)
            for i in range(len(n1)):
                n1[i] = a[i]
