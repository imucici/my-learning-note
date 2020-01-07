#題目:-1不要動，將其他非-1的由小到大排

Input:
a: [-1, 150, 190, 170, -1, -1, 160, 180]
Expected Output:
[-1, 150, 160, 170, -1, -1, 180, 190]

Input:
a: [-1, -1, -1, -1, -1]
Expected Output:
[-1, -1, -1, -1, -1]

# 解一:
a = [-1, 150, 190, 170, -1, -1, 160, 180]
    
temp = []
for i in a:
    if i != -1:
        temp.append(i) #把非-1的抓出來
        s = sorted(temp)
# print(s)
for j in range(len(a)):
    if a[j] != -1:
        a[j] = s[0]
        s.pop(0)
print(a)

#解二:

def sortByHeight(a):
    b = []
    c = []
    for i in a:
        if i != -1:
            b.append(i) #把非-1的抓出來
    b = sorted(b)
    for i in range(len(a)):
        if a[i] != -1:
            c.append(i) #把非-1的index抓出來
    for i in range(len(b)):
        a[c[i]] = b[i]
    return a
