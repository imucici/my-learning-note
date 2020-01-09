class Solution:
    def search(self, n: List[int], t: int) -> bool:
        for i in n:
            if i == t:
                return True
        return False
