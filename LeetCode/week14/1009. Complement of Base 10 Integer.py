class Solution:
    def bitwiseComplement(self, x: int) -> int:
        a = bin(x)
        a = a[2:]
        a = list(a)

        for i in range(len(a)) :
            if a[i] == '0':
                a[i] = "1"
            elif a[i] == '1':
                a[i] = "0"

        a = "".join(a)
        a = int(a, 2)
        return a
