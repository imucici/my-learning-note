class Solution:
    def customSortString(self, s: str, t: str) -> str:
        a = []

        s = list(s)
        t = list(t)
        for i in s:
            if i in t:
                c = t.count(i)
                a.extend([i]*c)
                n = 0
                while n < c:
                    t.remove(i)
                    n+=1
        return "".join((a+t))
