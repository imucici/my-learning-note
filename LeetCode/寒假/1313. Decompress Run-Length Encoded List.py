class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        final = []
        for i in range(len(nums)):
            if i % 2 == 0:
                c = 0
                while c < nums[i]:
                    final.append(nums[i+1])
                    c+=1
        return final
