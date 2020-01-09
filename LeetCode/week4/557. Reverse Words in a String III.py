class Solution:
    def reverseWords(self, s: str) -> str: #遇到空格拆掉再反轉
        a = s.split(" ")
        list1 = []
        for i in range(len(a)):
            t = a[i][::-1]
            list1.append(t)
        return " ".join(list1) 
