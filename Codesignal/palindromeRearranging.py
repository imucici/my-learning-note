a = "abcecba"

s = set(a)

n = 0
for i in s :
    if a.count(i) %2 != 0:
        n+=1
    if n > 1:
        return False

return True
