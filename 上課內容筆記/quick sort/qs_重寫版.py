# 佔外部空間法(重寫版)

#改寫1:
#遍歷list1時，用意思等同於for i in list的index的方法來遍歷(for i in range(len(list)):)

#改寫2:
#一開始想說新增元素到list有3種寫法(append、extend、insert)那就不要寫append，全部改用extend呈現，
#但在起初分3區處extend會報錯('int' object is not iterable)，因此就想說最後一步回傳結果的地方
#用extend新增元素的概念來替代＋連結3個list


def quicksort(list):
    if len(list) <= 1: # 若為空list或只含單個元素的list，默認已排序，所以直接回傳
        return list
    else:
        pivot = list[0] #把最左邊的數當基準點
        smaller = [] #建空list給<pivot的值放
        bigger = [] #建空list給>pivot的值放
        equal = [] #建空list給=pivot的值放
        final = [] #建空list存放最終結果
        for i in range(len(list)):
            if list[i] < pivot:
                smaller.append(list[i]) #將<pivot的值放入
            if list[i] > pivot:
                bigger.append(list[i]) #將>pivot的值放入
            if list[i] == pivot:
                equal.append(list[i]) #將=pivot的值放入
        #最後用final這個空list存放最終的排序結果
        final.extend(quicksort(smaller))
        final.extend(equal)
        final.extend(quicksort(bigger))
        return final

list1 = [77,7,4,96,3,5]
quicksort(list1)
