class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        x = list(zip(*A))
        return x
