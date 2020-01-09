class Solution:
    def canPlaceFlowers(self, a, n) -> bool:
        c = 0
        
        if len(a)==1:
            if a[0] == 0:
                c+=1
               
        elif len(a) == 2:
            if a[0] == 0 and a[1] == 0:
                c+=1
                
        else:
            if a[0] == 0 and a[1] == 0 :
                a[0] = 1
                c+=1
                
            if a[-1] == 0 and a[-2] == 0 :
                a[-1] = 1
                c+=1
                
            for i in range(1,len(a)-1):
                if a[i] != 1 and a[i-1] == 0 and a[i+1] ==0 :
                    a[i] = 1
                    c += 1
            
        print(a)
        print(c)
        if n <= c:
            return True
        else:
            return False
