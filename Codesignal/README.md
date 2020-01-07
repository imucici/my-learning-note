lambda、map()函數
====

目錄:
----
* [lambda簡介](#lambda簡介)
* [lambda語法](#lambda語法)
* [map函數簡介](#map函數簡介)
* [map函數語法](#map函數語法)
* [實例操作](#實例操作)


lambda簡介:
-----

又被稱為**無名函數**，是種將運算式重複運用的方式，類似函數 (function) ，卻又不像函數需要額外命名函數的識別字。

lambda語法:
----

* lambda `變數名稱`:`運算式`



map函數簡介:
-----

map() 會根據提供的函數(function)對指定序列做映射。
第一個参數 function 以参數序列中的每一個元素調用 function 函數，返回包含每次 function 函數返回值的新列表。




map函數語法:
------

map(function, 序列1, 序列2,...)

```diff
!因為返回的為迭代器，因此要再轉成list
```



實例操作:
----

* 兩個list對應元素相乘

```python

X = [-3,-1,0,1,4]
Y = [6,4,2,0,-8]

func = lambda x,y:x*y

final = list(map(func,X,Y))
```
output

```python
[-18,-4,0,0,-32]
```




while True、break、continue、pass
====

目錄:
----
* [while True 核心思想](#核心思想)
* [break_continue_pass區別](#break_continue_pass區別)
* [應用場景](#應用場景)
* [參考資料](#參考資料)


核心思想
------
* while True 是一個無限循環語句(死循環)，核心思想是`如果出現錯誤，可以繼續循環`，因為條件是`True` ，所以永遠不會跳出循環。
* while True 語句中一定要有結束該循環的 **`break`** 語句，否則會一直循環下去。



break_continue_pass區別
-----

* **break** : 強制結束 **`整個`** 迴圈。

```diff
當偵測到字母 t 時，就會強制結束 <整個> 迴圈：
```


```python
count=0
for i in 'content':
    count+=1
    if i == 't':
        break
    print(i)
    
print('\n迴圈結束')
print('迴圈執行了 %d 次' %count)
```
```python
c
o
n

迴圈結束
迴圈執行了4次

```
<br></br>

* **continue** :　強制跳出 **`本次`** 迴圈，繼續進入下一圈。

```python
當偵測到字母 t 時，會跳過 <本次迴圈剩下的程式碼> print(i)，但不會結束迴圈，仍然會進入下一圈繼續執行
```

```python
count=0
for i in 'content':
    count+=1
    if i == 't':
        continue
    print(i)
    
print('\n迴圈結束')
print('迴圈執行了 %d 次' %count)
```

```python
c
o
n
e
n

迴圈結束
迴圈執行了7次
```
<br></br>

* **pass** : 不做任何事情，所有程式都將繼續。

```diff
! 應用時機：當程式碼空著沒寫時，會產生錯誤，此時寫pass不僅不會報錯，也可以提醒自己之後要來完成
```

```python
當偵測到字母 t 時，會忽略該條件，繼續像正常迴圈一樣運行程序
```

```python
count=0
for i in 'content':
    count+=1
    if i == 't':
        pass
    print(i)
    
print('\n迴圈結束')
print('迴圈執行了 %d 次' %count)
```

```python
c
o
n
t
e
n
t

迴圈結束
迴圈執行了7次
```


<br></br>

應用場景:
----

* 過濾:利用 **`continue`** 告訴迴圈當 element 的 type 為非整數時，要跳出`本次`迴圈，繼續進入下一圈執行。

![continue](https://miro.medium.com/max/1798/1*fFZVAYdPRyiPjRWRIVDi3Q.png)

<br></br>
* 限制鍊表長度:利用 **`break`** 告訴迴圈當 result 列表 (List) 中的元素數量超過 5 個時，必須停止繼續加總剩下的值，強制結束迴圈。利用 **`continue`** 告訴迴圈當元素的 type 為字符串時，要跳出本次迴圈，繼續進入下一圈執行。

![break&continue](https://miro.medium.com/max/1812/1*pIjwaFT0wAki6DqFQ94VBw.png)


<br></br>

參考資料:
------
* [while True的用法](https://blog.csdn.net/geerniya/article/details/77524173)
* [1 分鐘搞懂 Python 迴圈控制：break、continue、pass](https://medium.com/@chiayinchen/1-%E5%88%86%E9%90%98%E6%90%9E%E6%87%82-python-%E8%BF%B4%E5%9C%88%E6%8E%A7%E5%88%B6-break-continue-pass-be290cd1f9d8)




strip() vs. split()
====


strip()
----
* **刪除** 的意思，可以刪除字串的某些字元
```python
宣告：s為字串，rm為要刪除的字元序列
```

```diff
!當rm為空時，預設刪除空白符（包括’\n’, ‘\r’, ‘\t’,  ‘ ‘)
```

*  s.strip(rm) 刪除s字串中`開頭`、`結尾`處，位於 rm刪除序列的字元
*  s.lstrip(rm) 刪除s字串中`開頭`處，位於 rm刪除序列的字元
*  s.rstrip(rm) 刪除s字串中`結尾`處，位於 rm刪除序列的字元

```python
a = " 123 "
a.strip()
a.lstrip()
a.rstrip()
print(a.strip())
print(a.lstrip())
print(a.rstrip())
```

output
```python
'123'
'123 '
' 123'
```


split()
----
* **分割** 的意思，是根據規定的字元將字串進行分割。

```python
str = 'www.google.com'
str_split = str.split('.') 
print(str_split)
```

output:
```python
['www', 'google', 'com'] 
```

Numpy套件
====

目錄:
----

* [簡介](#簡介)
* [Numpy vs List](#比較陣列和清單)
* [重要屬性](#重要屬性)
* [操作](#操作)
* [基本運算](#基本運算)
* [參考資料](#參考資料)

簡介:
----
* 一套強調高效率`陣列`處理的Python數學套件，可以幫助我們進行**向量**和**矩陣**運算。
* 處理陣列(array)的套件，協助進行`向量(一維陣列)`、`矩陣(二維陣列)`運算。
* Numpy套件的核心是ndarray物件，這是相同資料型態元素組成的陣列。

比較陣列和清單:
----

| |Numpy陣列|Python 清單|
|:-----:|:----:|:---:|
|尺寸|更改物件尺寸就是建立**新陣列**|似**容器**，不用指定尺寸|
|元素資料型態|需相同|可以不同|
|效率|較高|較低|



重要屬性:
---

* **ndarray.ndim**：NumPy ndarray物件的維度
* **ndarry.shape**：ndarry物件的每一個維度的大小(size)，回傳資料類別為`Tuple`
* **ndarry.size**：ndarry物件所組成之array的總元素數量，回應之數值會等於ndarray.shape的每個元素相乘
* **ndarry.dtype**：ndarray物件內組成元素的型態
* **ndarray.itemsize**：陣列中每一個**元素**的`大小(Bytes)` (ex: int16=>16/8=2 Bytes)
* **ndarry.data**：這是一個存有實際陣列元素的緩衝，通常我們不需要使用這個屬性，因為我們可以使用index存取這些元素。



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


參考資料:
----
[NumPy 1.14 教學 – #01 基礎, 建立陣列的方法](https://www.brilliantcode.net/1022/numpy-tutorial-basics-array-creations/)
