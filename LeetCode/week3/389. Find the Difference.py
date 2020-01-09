class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counts = [0 for _ in range(26)]

        for c in s:
            counts[ord(c) - ord("a")] += 1

        for c in t:
            index = ord(c) - ord("a")
            counts[index] -= 1
            if counts[index] < 0:
                return c
