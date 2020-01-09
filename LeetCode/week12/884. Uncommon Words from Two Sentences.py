#題目:找出只出現一次的單詞

A = "s z z z s"
B = "s z ejt"

lst = []
final = []

a = A.split(" ")
b = B.split(" ")

lst.extend(a)
lst.extend(b)
print("lst:",lst)

s = set(lst)

for i in s:
    if lst.count(i) == 1:
        final.append(i)
print("final",final)
