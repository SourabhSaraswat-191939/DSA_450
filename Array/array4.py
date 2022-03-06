arr = list(map(int,input().split()))
n = len(arr)
count0 = 0
count1 = 0
count2 = 0
for i in range(n):
    if arr[i]==0:
        count0+=1
    elif arr[i]==1:
        count1+=1
    else:
        count2+=1
result = []
for _ in range(count0):
    result.append(0)    
for _ in range(count1):
    result.append(1)
for _ in range(count2):
    result.append(2)

print(result)