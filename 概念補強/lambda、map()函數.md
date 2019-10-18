lambda、map()函數
====

目錄:
----
* [lambda簡介](#lambda簡介)
* [lambda語法](#lambda語法)
* [map()簡介](#map()簡介)
* [map()語法](#map()語法)
* [實例操作](#實例操作)


lambda簡介:
-----

又被稱為**無名函數**，是種將運算式重複運用的方式，類似函數 (function) ，卻又不像函數需要額外命名函數的識別字。

[回目錄](https://github.com/imucici/my-learning-note/blob/master/%E6%A6%82%E5%BF%B5%E8%A3%9C%E5%BC%B7/lambda%E3%80%81map()%E5%87%BD%E6%95%B8.md#%E7%9B%AE%E9%8C%84)

lambda語法:
----

* lambda `變數名稱`:`運算式`

[回目錄](https://github.com/imucici/my-learning-note/blob/master/%E6%A6%82%E5%BF%B5%E8%A3%9C%E5%BC%B7/lambda%E3%80%81map()%E5%87%BD%E6%95%B8.md#%E7%9B%AE%E9%8C%84)

map()簡介:
-----

map() 會根據提供的函數(function)對指定序列做映射。
第一個参數 function 以参數序列中的每一個元素調用 function 函數，返回包含每次 function 函數返回值的新列表。


[回目錄](https://github.com/imucici/my-learning-note/blob/master/%E6%A6%82%E5%BF%B5%E8%A3%9C%E5%BC%B7/lambda%E3%80%81map()%E5%87%BD%E6%95%B8.md#%E7%9B%AE%E9%8C%84)

map()語法:
------

map(function, 序列1, 序列2,...)

```diff
!因為返回的為迭代器，因此要再轉成list
```


[回目錄](https://github.com/imucici/my-learning-note/blob/master/%E6%A6%82%E5%BF%B5%E8%A3%9C%E5%BC%B7/lambda%E3%80%81map()%E5%87%BD%E6%95%B8.md#%E7%9B%AE%E9%8C%84)

實例操作:
----

* 兩個list對應元素相乘

```python

X = [-3,-1,0,1,4]
Y = [6,4,2,0,-8]

func = lambda x,y:x*y

final = list(map(func,X,Y))
```


