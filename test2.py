# cook your dish here
t = int(input())
for _ in range(t):
    a,b,x,y = map(int,input().split())
    board = []
    for i in range(8):
        row = []
        for j in range(8):
            row.append(0)
            
        board.append(row)
    moves = [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[-1,2],[1,-2],[-1,-2]]
    dp = {}
    visited = set()
    def dfs(src,visited,count):
        # print(count,visited)
        print(src)
        if src[0]<1 or src[1]<1 or src[0]>8 or src[1]>8:
            return False
        if src==(x,y):
            print(count)
            if (count%2==0) and count<100:
                return True
            else:
                return False
        if src in visited:
            return False
        visited.add(src)
        if src in dp:
            return False
        
        for mx,my in moves:
            print((src[0],src[1]),"-->",end="")
            result = dfs((src[0]+mx,src[1]+my),visited,count+1)
            if result:
                return True
        # visited.add(src)    
        return False
            
    
    if dfs((a,b),visited,0):
        print("YES")
    else:
        print(visited)
        print("NO")
        