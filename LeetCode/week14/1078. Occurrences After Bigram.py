class Solution:
    def findOcurrences(self, text: str, a: str, b: str) -> List[str]:
        l = []
        t = text.split(" ")

        for i in range(len(t)-2):
            if t[i] == a and t[i+1] == b:
                l.append(t[i+2])
        return l
