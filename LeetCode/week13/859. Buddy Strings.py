class Solution:
    def buddyStrings(self, a: str, b: str) -> bool:
        A = list(a)
        B = list(b)
        lst = []
        if a == b and len(set(A)) == len(A):
            return False
        else:
        
            if len(A) == len(B):
                for i in set(A):
                    if A.count(i) != B.count(i):
                        return False
                    else:
                        for i in range(len(A)):
                            if A[i] != B[i]:
                                lst.append(A[i])
                        if len(lst) > 2:
                            return False
                        else:
                            return True
            else:
                return False
