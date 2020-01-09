class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        lst = []
        for i in range(len(coordinates)-1):
            a = coordinates[i+1][1] - coordinates[i][1]
            b = coordinates[i+1][0] - coordinates[i][0]
            if b != 0:
                m  = a / b
            else :
                return False
            lst.append(m)
        s = set(lst)
        if len(s) == 1:
            return True
        else:
            return False
