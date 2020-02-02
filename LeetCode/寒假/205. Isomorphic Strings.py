class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) == 0 and len(t) == 0:
            return True
        
        if len(set(s)) != len(set(t)):
            return False
        
        z = list(zip(s,t))
        s = sorted(z)
    
        for i in range(len(s)-1):
            if s[i][0] != s[i+1][0]:
                pass
            else:
                if s[i][1] != s[i+1][1]:
                    return False
        return True
