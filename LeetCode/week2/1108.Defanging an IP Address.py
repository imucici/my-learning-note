# 題目:
#將字串內的"."替換成"[.]"

# 觀念:
#replace('舊字符串','新字符串') 此函數適用於str
#---------------------------------------------------------------------------

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.','[.]') # replace() 將字串內的"."替換成"[.]" 
