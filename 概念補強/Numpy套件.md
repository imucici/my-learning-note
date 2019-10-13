Numpy套件
====

目錄:
* [簡介](#簡介)
* [操作](#操作)
* [基本運算](#基本運算)

簡介:
----
* 一套強調高效率`陣列`處理的Python數學套件，可以幫助我們進行**向量**和**矩陣**運算。
* 處理陣列(array)的套件，協助進行`向量(一維陣列)`、`矩陣(二維陣列)`運算。
陣列(array)類似清單(list)，但`array`裡面的元素資料型態必須**相同**，list可以不同。

操作:
---

* 建立array : 

```python
import numpy as np
```


* 建立一維陣列:

```python
a = np.array([1,2,3,4]) # [] : 參數是清單(list) 資料可更改
b = np.array((1,2,3,4)) # () : 參數是元組(tuple) 資料不可更改
a[0] #取值
b[0] = 6 #更改值
```


```python
a = np.arange(5) #類似 Python 的 range, 但是回傳 array
print(a)
>>[0,1,2,3,4]
```


基本運算:
----


* 建立二維陣列:

```python
c = np.array([[1,2,3],[4,5,6]])
c[0,0] # 取值
c[0,0] = 2 #更改值
```



* 一維轉二維 reshape() :

```python
x = np.arange(10)
y = x.reshape(5,2) # 轉換為5*2的二維陣列
```

* 遍歷:

```python
a = np.array([[1,2],[3,4],[5,6]])
for i in a :
     for j in i :
           print(j)
```           

```python
output : 
1
2
3
4
5
6
```
