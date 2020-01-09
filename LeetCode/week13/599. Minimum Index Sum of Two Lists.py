class Solution:
    def findRestaurant(self, l1: List[str], l2: List[str]) -> List[str]:
        t = []
        p = []
        for i in range(len(l1)):
            for j in range(len(l2)):
                if l1[i] == l2[j]:
                    s = i+j
                    t.append(s)
                    p.append(i)

        ans = []
        for i in range(len(t)):
            if t[i] == min(t):
                ans.append(l1[p[i]])
        return ans
