class Solution:
    def wordPattern(self, s: str, a: str) -> bool:
        b = a.split(" ")
        if len(s) == 1 and len(a) == 1:
            return True
        else:
            if len(set(s)) != len(set(b)) or len(s) != len(b):
                return False
            else:
                z = list(zip(s,b))

                for i in range(len(s)-1):
                    if z[i][0] == z[i+1][0]:
                        if z[i][-1] != z[i+1][-1]:
                            return False
                    if z[i][0] != z[i+1][0]:
                        if z[i][-1] == z[i+1][-1]:
                            return False
                return True
