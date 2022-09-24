import sys
from collections import deque
maxVal = sys.maxsize
class Graph:
    def __init__(self,n) -> None:
        self.v = n
        self.adj = [None]*n
    def add_edge(self,u,v):
        if self.adj[u]==None:
            self.adj[u]= []
        self.adj[u].append(v)
        if self.adj[v]==None:
            self.adj[v]= []
        
    def print(self,dist):
        print("Vertex Distance from Source") 
        for i in range(self.v): 
            print("{0}\t\t{1}".format(i, dist[i])) 

    def topo_sort_BFS(self):
        stack = []
        que = deque()        
        visited = set()
        for i in range(self.v):
            if i not in visited:
                que.append(i)
                stack2 = []
                while len(que)!=0:
                    pop = que.popleft()
                    stack2.append(pop)
                    visited.add(pop)
                    for neighbour in self.adj[pop]:
                        if neighbour not in visited:
                            que.append(neighbour)
                            
                stack += stack2[::-1]

        return stack

g = Graph(6)
g.add_edge(5,0)
g.add_edge(4,0)
g.add_edge(5,2)
g.add_edge(2,3)
g.add_edge(3,1)
g.add_edge(4,1)
# g.dfs(2)
print(g.topo_sort_BFS())
# print("Connected Components count ->",g.connectedComp())


