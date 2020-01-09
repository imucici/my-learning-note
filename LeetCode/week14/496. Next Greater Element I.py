class Solution:
    def nextGreaterElement(self, a: List[int], b: List[int]) -> List[int]:
        lst = []
        for i in range(len(a)):
            for j in range(len(b)):
                if a[i] == b[j]:
                    if b[j] == b[-1]:
                        lst.append(-1)
                    else:
                        det = True
                        for k in range(j+1,len(b)):
                            if b[k] > a[i] :
                                det = False
                                lst.append(b[k])
                                break
                        if det:
                            lst.append(-1)
        return lst
