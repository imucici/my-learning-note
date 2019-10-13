Numpy套件
====

目錄:
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
