class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        else:
            temp = []
            for i in range(len(strs)):
                temp.append(len(strs[i]))
            temp = sorted(temp)
            
            if temp[0] == 0:
                return ""
            
            for j in range(temp[0]):
                for k in range(len(strs)-1):
                    if strs[k][j] != strs[k+1][j]:
                        if j == 0:
                            return ""
                        else:
                            return strs[0][:j]
            return strs[0][:temp[0]]
                    
            
