class Solution:
    def removeDuplicates(self, n):
        for i in n :
            count = n.count(i)
            if count >2:
                d = 0
                while d < count-2:
                    d+=1
                    n.remove(i)
