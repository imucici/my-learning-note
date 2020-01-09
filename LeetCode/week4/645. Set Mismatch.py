class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        a = []
        sort = [] 
        double = sum(nums) - sum(set(nums)) #重複值
        
        for i in range(1,len(nums)+1):
            sort.append(i)
        non = list(set(sort)-set(nums)) #缺失值
        a.append(double)
        a.extend(non)        
        return a
