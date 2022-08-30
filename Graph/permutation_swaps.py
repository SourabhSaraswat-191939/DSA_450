from operator import ne


def permutation_swaps(p,q,good_pairs,n):
    adj= {}
    for pair in good_pairs:
        if p[pair[0]-1] not in adj:
            adj[p[pair[0]-1]] = []
        adj[p[pair[0]-1]].append(p[pair[1]-1])
        if p[pair[1]-1] not in adj:
            adj[p[pair[1]-1]] = []
        adj[p[pair[1]-1]].append(p[pair[0]-1])

    def dfs(src,visited,target):
        visited[src] = True
        if src not in adj:
            return False
        for neighbour in adj[src]:
            if neighbour==target:
                visited[src] = False
                return True
            if neighbour not in visited:
                result = dfs(neighbour,visited,target)
                if result:
                    return True
        visited[src] = False
        return False

    for i in range(n):
        if p[i]==q[i]:
            continue
        visited={}
        if dfs(p[i],visited,q[i]):
            continue
        
        return 0
    return 1


n,m = map(int,input().split())
p = list(map(int,input().split()))
q = list(map(int,input().split()))
good_pairs = []
for _ in range(m):
    good_pairs.append(tuple(map(int,input().split())))

print(permutation_swaps(p,q,good_pairs,n))