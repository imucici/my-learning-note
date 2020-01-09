class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        lst = []
        final = []

        a = A.split(" ")
        b = B.split(" ")

        lst.extend(a)
        lst.extend(b)

        s = set(lst)

        for i in s:
            if lst.count(i) == 1:
                final.append(i)
        return final
