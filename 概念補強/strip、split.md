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
