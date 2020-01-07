QuickSort
=============

目錄:
--------
* [簡介](#簡介)
* [比較(InsertionSort vs QuickSort)](#比較)
* [實例講解](#實例講解)
* [完整程式範例](#完整程式範例)
* [課程影片連結](#課程影片連結)
* [參考資料](#參考資料)


簡介
-----

* **QuickSort(快速排序法)**

   * 是一種「把大問題分成小問題處理」方法
   * **具體演算法**:
      1. 數列中選擇任一元素作為基準點(pivot)。
      2. 將數列一分為二，小於此元素的移至基準的左邊，大於此元素的移至右邊，相等的任意放。
      3. 基準點左邊和右邊視為兩個數列，並重複做以上動作直到完成排序。

   * **示意圖**
<br></br>
![QuickSort](https://i2.wp.com/www.techiedelight.com/wp-content/uploads/Quicksort.png?w=1100http://)

[回目錄](https://github.com/imucici/my-learning-note/blob/master/%E4%B8%8A%E8%AA%B2%E5%85%A7%E5%AE%B9%E7%AD%86%E8%A8%98/%E7%AC%AC%E5%9B%9B%E9%80%B1%E4%B8%8A%E8%AA%B2%E9%80%B2%E5%BA%A6.md#%E7%9B%AE%E9%8C%84)


比較:
-----


|         |     InsertionSort     | QuickSort  |
| :-------------: |:-------------:| :------------:|
| 最佳時間複雜度        | O(n)      | O(nlog n) |
| 平均時間複雜度        | O(n^2)      |   O(nlog n) |
| 最差時間複雜度         | O(n^2)     |  O(n2)   |


> 參考資料 [[Sort] 淺談 insertion sort](https://blog.kuoe0.tw/posts/2013/03/05/sort-about-insertion-sort/)

> 參考資料 [[Sort] 淺談 quick sort](https://blog.kuoe0.tw/posts/2013/03/15/sort-about-quick-sort/)

[回目錄](https://github.com/imucici/my-learning-note/blob/master/%E4%B8%8A%E8%AA%B2%E5%85%A7%E5%AE%B9%E7%AD%86%E8%A8%98/%E7%AC%AC%E5%9B%9B%E9%80%B1%E4%B8%8A%E8%AA%B2%E9%80%B2%E5%BA%A6.md#%E7%9B%AE%E9%8C%84)


實例講解:
-----

* QuickSort

```python
舉例有一組序列: 8 2 45 17 4 3 
```      

`灰底`:已排序的值 ; **粗體**: 基準點(假定每次都拿最左邊的數當基準點)

Step1:
**2** 4 3 `8` **45** 17

Step2:
`2` **4** 3 `8` 17 `45`

Step3:
`2` `3` `4` `8` `17` `45`


[回目錄](https://github.com/imucici/my-learning-note/blob/master/%E4%B8%8A%E8%AA%B2%E5%85%A7%E5%AE%B9%E7%AD%86%E8%A8%98/%E7%AC%AC%E5%9B%9B%E9%80%B1%E4%B8%8A%E8%AA%B2%E9%80%B2%E5%BA%A6.md#%E7%9B%AE%E9%8C%84)


完整程式範例:
----

* **QuickSort(佔外部空間法)**

     * 將數列`最左邊`的數當基準點(pivot)，小於此數放入smaller的空list ; 大於此數放入bigger的空list，相等放入equal的空list，重複這些步驟，直到完成排序，最後將這三部分的list合併。
      
```python
   # 佔外部空間法


def quicksort(list):
    if len(list) <= 1: # 若為空list或只含單個元素的list，默認已排序，所以直接回傳
        return list
    else:
        pivot = list[0] #把最左邊的數當基準點
        smaller = [] #建空list給<pivot的值放
        bigger = [] #建空list給>pivot的值放
        equal = [] #建空list給=pivot的值放
        for i in list:
            if i < pivot:
                smaller.append(i) #將<pivot的值放入
            elif i > pivot:
                bigger.append(i) #將>pivot的值放入
            else:
                equal.append(i) #將=pivot的值放入
        return quicksort(smaller) + equal + quicksort(bigger)#3個list合併
   ```
        
```python
list1 = [7,79,45,6,3,65]
quicksort(list1)
```
output

```python
[3, 6, 7, 45, 65, 79]
```
> [完整程式碼](https://github.com/imucici/my-learning-note/blob/master/%E4%B8%8A%E8%AA%B2%E5%85%A7%E5%AE%B9%E7%AD%86%E8%A8%98/quick%20sort/quick%20sort_%E4%BD%94%E5%A4%96%E9%83%A8%E7%A9%BA%E9%96%93%E6%B3%95.ipynb)   

<br></br>
* 流程圖

![quick sort 流程圖](https://github.com/imucici/my-learning-note/blob/master/%E4%B8%8A%E8%AA%B2%E5%85%A7%E5%AE%B9%E7%AD%86%E8%A8%98/quick%20sort/quick%20sort_%E6%B5%81%E7%A8%8B%E5%9C%96.png)


> [流程圖連結](https://github.com/imucici/my-learning-note/blob/master/%E4%B8%8A%E8%AA%B2%E5%85%A7%E5%AE%B9%E7%AD%86%E8%A8%98/quick%20sort/quick%20sort_%E6%B5%81%E7%A8%8B%E5%9C%96.png)

* 佔外部空間法(重寫版)

```python
# 佔外部空間法(重寫版)

#改寫1:
#遍歷list1時，用意思等同於for i in list的index的方法來遍歷(for i in range(len(list)):)

#改寫2:
#一開始想說新增元素到list有3種寫法(append、extend、insert)那就不要寫append，全部改用extend呈現，
#但在起初分3區處extend會報錯('int' object is not iterable)，因此就想說最後一步回傳結果的地方
#用extend新增元素的概念來替代＋連結3個list

#改寫3:
#把需要不斷比大小的smaller、bigger兩個list分別定義函式呼叫

def qs(list):
    
    while len(list) <= 1: # 若為空list或只含單個元素的list，默認已排序，所以直接回傳
        return list
    
    while len(list) > 1:
        
        
        def smaller(list):
            small = []
            for i in range(len(list)):
                if list[i] < list[0]:
                    small.append(list[i]) #將<list[0]的值放入
            return small
        
        equal=[]
        for i in range(len(list)):
            if list[i] == list[0]:
                equal.append(list[i]) #將=list[0]的值放入
            
        def bigger(list):
            big = []
            for i in range(len(list)):
                if list[i] > list[0]:
                    big.append(list[i]) #將>list[0]的值放入
            return big
        
        final = [] #最後用final這個空list存放最終的排序結果
        final.extend(qs(smaller(list)))
        final.extend(equal)
        final.extend(qs(bigger(list)))
        return final
```

```python
list1 = [4,6,13,4,8,7,7,4,5,6]
qs(list1)
```

output
```python
[4, 4, 4, 5, 6, 6, 7, 7, 8, 13]
```

<br></br>     
* **QuickSort(in_place 不佔外部空間法)**

```python
def partition(arr, beg, end):
    # 若為空list或只含單個元素的list，默認已排序，所以直接回傳
    if len(arr) <= 1:
        return arr
    
    else:
        
        pivot_index = beg #為了保留beg (pivot_index:第0位)
        pivot = arr[beg] #把第0位的值叫piviot
        
        
        left = pivot_index + 1
        right = end - 1 #(range的end值不包含)
        
        
        while True: #while True為確保程式出錯時能繼續運行
            
            #只要左邊的值小於基準點，就繼續向下走
            while left <= right and arr[left] < pivot:
                left += 1
            
            #只要右邊的值大於基準點，就繼續往上一個走
            while right >= left and arr[right] > pivot:
                right -= 1
            
            #當left<right時為了避免一直交換下去，因此讓強迫結束迴圈
            if left > right:
                break
            
            #將lef和right的值互換
            else:
                arr[left], arr[right] = arr[right], arr[left]
    
    
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index] #第一次排序後將right的值和基準點互換，如此基準點就能在正確位置
    
    return right, pivot

def quicksort(arr, beg, end):
    
    #將arr切分成左右兩半部各自操作
    if beg < end:
        right, pivot = partition(arr, beg, end)
        
        #運行左側arr
        quicksort(arr, beg, right) #上面互換是互換指針的值 因此指針位置其實不變
        
        #運行右側arr
        quicksort(arr, right + 1,end)
    return arr
```

```python
examplelist = [3,34,53,1,90,25,7]
quicksort(examplelist, 0, len(examplelist))
```

output

```python
[1, 3, 7, 25, 34, 53, 90]
```


> [完整程式碼](https://github.com/imucici/my-learning-note/blob/master/%E4%B8%8A%E8%AA%B2%E5%85%A7%E5%AE%B9%E7%AD%86%E8%A8%98/quick%20sort/quick%20sort_in_place%20%E4%B8%8D%E4%BD%94%E5%A4%96%E9%83%A8%E7%A9%BA%E9%96%93%E6%B3%95.ipynb)

[回目錄](https://github.com/imucici/my-learning-note/blob/master/%E4%B8%8A%E8%AA%B2%E5%85%A7%E5%AE%B9%E7%AD%86%E8%A8%98/%E7%AC%AC%E5%9B%9B%E9%80%B1%E4%B8%8A%E8%AA%B2%E9%80%B2%E5%BA%A6.md#%E7%9B%AE%E9%8C%84)



課程影片連結:
----
<a href="http://www.youtube.com/watch?feature=player_embedded&v=G4dwRF_Rzd0
" target="_blank"><img src="http://img.youtube.com/vi/G4dwRF_Rzd0/0.jpg" 
alt="圖片 ALT 文字放在這裡" width="720" height="540" border="20" /></a>

[回目錄](https://github.com/imucici/my-learning-note/blob/master/%E4%B8%8A%E8%AA%B2%E5%85%A7%E5%AE%B9%E7%AD%86%E8%A8%98/%E7%AC%AC%E5%9B%9B%E9%80%B1%E4%B8%8A%E8%AA%B2%E9%80%B2%E5%BA%A6.md#%E7%9B%AE%E9%8C%84)

參考資料:
----

* [Quick Sort_in place網頁版](https://www.cnblogs.com/zuoyuan/p/3766296.html)

* [Quick Sort影片版](https://www.youtube.com/watch?v=CB_NCoxzQnk)

[回目錄](https://github.com/imucici/my-learning-note/blob/master/%E4%B8%8A%E8%AA%B2%E5%85%A7%E5%AE%B9%E7%AD%86%E8%A8%98/%E7%AC%AC%E5%9B%9B%E9%80%B1%E4%B8%8A%E8%AA%B2%E9%80%B2%E5%BA%A6.md#%E7%9B%AE%E9%8C%84)

