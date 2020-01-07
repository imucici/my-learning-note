def addBorder(picture):
    top = []
    down = []
    final = []

    n = 0
    while n < len(picture[0])+2:
        top.append("*")
        n+=1
    top = "".join(top) #list轉str
    final.append(top)

    for i in picture:
        i = list(i)
        i.insert(0,"*")
        i.append("*")
        i = "".join(i)
        final.append(i)

    m = 0
    while m < len(picture[0])+2:
        down.append("*")
        m+=1
    down = "".join(down)
    final.append(down)
    return final
