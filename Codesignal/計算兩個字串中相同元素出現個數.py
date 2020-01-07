s1 = "aabcc"
s2 = "adcaacsc"


a = list(s1)
b = list(s2)

n = 0
if len(a) <= len(b):
    for i in b :
        if i in a:
            a.remove(i)
            n+=1
else:
    for i in a :
        if i in b:
            b.remove(i)
            n+=1
        
print(n)
