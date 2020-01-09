class Solution:
    def judgeCircle(self, moves: str) -> bool:
        base = list(moves)
        U = []
        D = []
        L = []
        R = []
        for i in base :
            if i == 'U':
                U.append(i)
            if i == 'D':
                D.append(i)
            if i == 'L':
                L.append(i)
            if i == 'R':
                R.append(i)
        if len(U) == len(D) and (len(L) == len(R)) !=0:
            return True
        elif len(L) == len(R) and (len(U) == len(D)) !=0:
            return True
        else:
            return False
