class Solution:
    def strStr(self, a: str, b: str) -> int:
        a = list(a)
        b = list(b)
        if len(b)>len(a):
            return -1
        
        elif len(b)==0:
            return 0
        else:
            for i in range(len(a)-len(b)+1):
                if a[i:i+len(b)] == b:
                    return i
            return -1
