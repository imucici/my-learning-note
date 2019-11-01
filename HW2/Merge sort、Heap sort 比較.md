穩定性_時間_空間複雜度比較:
----

|         |     Merge Sort     |  	Heap Sort |
| :-------------: |:-------------:| :------------:|
| 最佳時間複雜度        | Ο(n log n)    |Ο(n log n)|
| 平均時間複雜度        | Ο(n log n)     |   Ο(n log n)|
| 最差時間複雜度         | Ο(n log n)     |  Ο(n log n)|
|空間複雜度| Ο(n) 為避免在合併時覆蓋掉還未比較的元素，因此需暫時開一個空間存放Merge後的結果| Ο(1) (in_place不占外部空間)|
|穩定性|穩定|不穩定|

```diff
! 穩定:如果鍵值相同之資料，在排序後相對位置與排序前相同時，稱穩定排序。
! 不穩定:如果鍵值相同之資料，在排序後相對位置與排序前不相同時，稱不穩定排序。
````

* **Merge Sort_時間複雜度推導**
<br></br>
![Merge Sort_時間複雜度推導](https://github.com/imucici/my-learning-note/blob/master/%E5%9C%96%E7%89%87/Merge%20Sort_%E6%99%82%E9%96%93%E8%A4%87%E9%9B%9C%E5%BA%A6.jpg)


* **Heap Sort_時間複雜度推導**

假設堆有n個節點，則高度為log n。

```python


每回合取出最大值，再重新堆積 : Ο(log n)
總共需進行回合數 : n 次
最大堆建立後接著排序 : Ο( n log n)

故時間複雜度為 : Ο( n log n)

````

:blush: 理論上由於Heap sort是in place sorting，相較Merge sort需要佔外部空間，因此Heap sort較優於Merge sort。
