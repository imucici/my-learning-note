class Solution:
    def validPalindrome(self, s):
        while s[0] == s[-1]:
            s  = s[1:-1]
            if len(s) < 3 :
                return True
        #刪尾
        temp = s
        s = s[:-1]
        while s[0] == s[-1]:
            s = s[1:-1]
            if len(s) < 2:
                return True
        #刪頭    
        s = temp[1:]
        while s[0] == s[-1]:
            s = s[1:-1]
            if len(s) < 2 :
                return True 
        return False
