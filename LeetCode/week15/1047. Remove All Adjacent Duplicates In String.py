class Solution:
    def removeDuplicates(self, S: str) -> str:
        b = list(S)
        l = len(S) - 1
        det = True
        for i in range(l):
            if i < l:
                if b[i] == b[i+1]:
                    b.pop(i)
                    b.pop(i)
                    l = l - 2
                    det = False
        if det:
            return S
        else:
            c = "".join(b)
            if c == "" or len(c) == 1:
                return c
            else:
                return Solution().removeDuplicates(c)
