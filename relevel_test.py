n,m=map(int,input().split())
p = list(map(int,input().split()))

pSet = set(p)

i=1
while True:
    if m-i not in pSet:
        print(m-i)
        break
    if m+i not in pSet:
        print(m+i)
        break

    i+=1

