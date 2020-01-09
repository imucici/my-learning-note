class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int: #判斷S是否在J裡面，是>寫入空list
        a = []
        j = list(J)
        s = list(S)
        for i in s:
            if i in j:
                a.append(i)
        return len(a)
        
