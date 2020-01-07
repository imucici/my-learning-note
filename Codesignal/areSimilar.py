def areSimilar(a, b):
    x = []
    y = []

    for i in range(len(a)):
        if a[i] != b[i]:
            x.append(a[i])
            y.append(b[i])
    
    if len(x) == 0:
        return True
    if len(x) == 2 and x[0] == y[1] and x[1] == y[0]:
        return True
    else:
        return False
