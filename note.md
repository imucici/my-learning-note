Linked List
===========
概念:
----------
* Linked List 由節點(Node)及"next"字段組成。通常用第一個節點(稱為頭節點)來表示整個list。
* 和array不同，若想要獲取第n個元素，必須從頭節點的"next"字段逐個走訪。

操作:
-----
* 新增:
  * `addAtHead(val)` : 在開頭插入一個新節點。
    * 先初始化新節點"cur"，再鏈接到原始頭節點，最後指定新節點為新的頭節點。
  * `addAtTail(val)` : 在尾巴插入一個新節點。 
    * 將原始最後一個節點的"next"字段指向新插入的節點。
  * `addAtIndex(val)` : 加入節點至指定位置。
    * 先初始化新節點"cur"，再將"cur"的"next"字段鏈接到下個節點，最後將上一個的"next"字段鏈接到"cur"節點。
* 刪除:
 * `deleteAtIndex(index)` :
