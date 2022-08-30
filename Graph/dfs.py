class Graph:
    def __init__(self, n) -> None:
        self.v = n
        self.adj = [None]*(n+1)
    def add_edge(self,n1,n2,biDir = True):
        if self.adj[n1] is None:
            self.adj[n1] = []
        self.adj[n1].append(n2)
        if biDir:
            if self.adj[n2] is None:
                self.adj[n2] = []
            self.adj[n2].append(n1)
    def dfsHelper(self,src,visited):
        visited[src] = True
        print(src)
        for neighbour in self.adj[src]:
            if neighbour not in visited:
                self.dfsHelper(neighbour,visited)

    def dfs(self,src):
        visited = dict()
        self.dfsHelper(src,visited)

    def connectedComponents(self):
        visited = {}
        result = 0
        for i in range(1,self.v+1):
            if i not in visited:
                result+=1
                self.dfsHelper(i,visited)
            print("Visited -> ",visited)
            print("-----------------------")
        return result
        
g = Graph(4)
g.add_edge(1,1)
g.add_edge(2,3)
g.add_edge(3,3)
g.add_edge(4,4)

g.dfs(2)
print("----------------------")
print("Number of connected components in graph are -> ",g.connectedComponents())