class Solution:
    def intersection(self, a: List[int], b: List[int]) -> List[int]:
        a = set(a)
        b = set(b)
        lst = []
        for i in a:
            if i in b:
                lst.append(i)
        return lst
