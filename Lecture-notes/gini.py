def gini(p):
    total = 0
    for i in p:
        total = total + pow(i,2)
    print(1-total)

gini([1/2,1/2])
