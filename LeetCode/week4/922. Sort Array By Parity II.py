class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        even = []
        odd = []
        final = []
        for i in A:
            if i%2 == 0:
                even.append(i)
            else:
                odd.append(i)
        for x,y in zip(even,odd):
            final.append(x)
            final.append(y)
        return final
