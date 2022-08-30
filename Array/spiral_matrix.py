def spiralOrder(a):
    ans = [] 
    m = len(a)
    n = len(a[0])
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    visited = set()
    r=c=0
    j=0
    for i in range(m*n):
        visited.add((r,c))
        ans.append(a[r][c])
        if r+dr[j]>=m or c+dc[j]>=n or r+dr[j]<0 or c+dc[j]<0:
            j = (j+1)%4
        if (r+dr[j],c+dc[j]) in visited:
            j = (j+1)%4
        r = r+dr[j]
        c = c+dc[j]
    
    return ans

a = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]
  
for x in spiralOrder(a):
    print(x, end=" ")