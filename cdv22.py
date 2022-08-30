from itertools import combinations as c
def area(X,Y,n):
    area = 0.0
    j = n - 1
    for i in range(0,n):
        area += (X[j] + X[i]) * (Y[j] - Y[i])
        j = i 
    return int(abs(area / 2.0))

n = int(input())
if n>=3:
    points = []
    for _ in range(n):
        a,b = map(int,input().split())
        points.append((a,b))
    
    NoOfSides = 0
    l = list(c(points,3))
    print(l)
    # for i in l:
    # if(colinear(i)):NoOfSides+=1
