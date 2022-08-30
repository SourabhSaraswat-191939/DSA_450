import numpy as np

n = int(input("Enter the no. of processes"))#5
m = int(input("Enter the no. of resources"))#3 

# Allocation Matrix
  
print("Enter allocation matrix (entries in single line separated by space): ")
entries = list(map(int, input().split()))
alloc = np.array(entries).reshape(n, m)
print(alloc) #[[0, 1, 0 ],[ 2, 0, 0 ],[3, 0, 2 ],[2, 1, 1] ,[ 0, 0, 2]]

# MAX Matrix
print("Enter Max matrix (entries in single line separated by space): ")
inputs = list(map(int, input().split()))
max = np.array(inputs).reshape(n, m)
print(max)
#[[7, 5, 3 ],[3, 2, 2 ],[ 9, 0, 2 ],[2, 2, 2],[4, 3, 3]]

#Available Resources
avail = list(map(int, input("Enter available resources").split()))#[3, 3, 2] 

f = [0]*n
ans = [0]*n
ind = 0
for k in range(n):
    f[k] = 0
    
need = [[ 0 for i in range(m)]for i in range(n)]
for i in range(n):
    for j in range(m):
        need[i][j] = max[i][j] - alloc[i][j]
y = 0
for k in range(5):
    for i in range(n):
        if (f[i] == 0):
            flag = 0
            for j in range(m):
                if (need[i][j] > avail[j]):
                    flag = 1
                    break
            
            if (flag == 0):
                ans[ind] = i
                ind += 1
                for y in range(m):
                    avail[y] += alloc[i][y]
                f[i] = 1
                
print("Following is the SAFE Sequence")

for i in range(n - 1):
    print(" P", ans[i], " ->", sep="", end="")
print(" P", ans[n - 1], sep="")