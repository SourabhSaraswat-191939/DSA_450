import sys
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

    def topoSortUtils(self,n, stack, visited):
        visited.add(n)
        for neighbour in self.adj[n]:
            if neighbour not in visited:
                self.topoSortUtils(neighbour,stack,visited)

        stack.append(n)

    def topoSort(self):
        stack = []
        visited = set()
        for i in range(self.v):
            if i not in visited:
                self.topoSortUtils(i,stack,visited)

        return stack

g = Graph(6)
g.add_edge(5,0)
g.add_edge(4,0)
g.add_edge(5,2)
g.add_edge(2,3)
g.add_edge(3,1)
g.add_edge(4,1)
# g.dfs(2)
print(g.topoSort())
# print("Connected Components count ->",g.connectedComp())


