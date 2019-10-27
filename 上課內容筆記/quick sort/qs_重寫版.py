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
    
list1 = [4,6,13,4,8,7,7,4,5,6]
qs(list1)
