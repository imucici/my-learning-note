class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = s.split( )
        if len(a) == 0: #當字串只由空格組成時，切割後為空list
            return 0
        else:
            return len(a[-1])
