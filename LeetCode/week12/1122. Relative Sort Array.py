#題目:
#將arr1的元素按照arr2的順序排列，再將沒出現在arr2的元素按照升冪排列


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        a = []
        b = []
        final = []
        for j in range(len(arr2)):
            for i in arr1:
                if i == arr2[j]:
                    a.append(i)
                    
        for i in arr1:
            if i not in arr2:
                b.append(i)
        final = a + sorted(b)
        return final
        
