import sys
from heapq import heapify, heappush, heappop
maxVal = sys.maxsize
class Graph:
    def __init__(self,n) -> None:
        self.v = n
        self.adj = [None]*(n+1)
    def add_edge(self,n1,n2,weight,biDir = True):
        if self.adj[n1] is None:
            self.adj[n1] = []
        self.adj[n1].append([n2,weight])
        if biDir:
            if self.adj[n2] is None:
                self.adj[n2] = []
            self.adj[n2].append([n1,weight])    
    def print(self):
        print(self.adj)
    def shortestDistance(self,src,dest):
        heap = []
        heapify(heap)
        heappush(heap, (src,0))
        previousNode = {}
        shortest_path_distances = [maxVal]*self.v
        shortest_path_distances[src] = 0

        while len(heap)!=0:
            out, weight = heappop(heap)
            for neighbour, n_weight in self.adj[out]:
                if shortest_path_distances[neighbour]>weight+n_weight:
                    shortest_path_distances[neighbour] = weight+n_weight
                    previousNode[neighbour] = out
                    heappush(heap,(neighbour, shortest_path_distances[neighbour]))
        print("Shortes Path Distances")
        print(shortest_path_distances)
        print("Path from dest to src")
        while dest!=src:
            print(dest, end=" <- ")
            dest = previousNode[dest]
        print(dest)



g = Graph(7)
g.add_edge(0,1,2)
g.add_edge(1,3,5)
g.add_edge(0,2,1)
g.add_edge(2,3,8)
g.add_edge(3,5,15)
g.add_edge(3,4,10)
g.add_edge(4,5,6)
g.add_edge(4,6,2)
g.add_edge(6,5,6)
# g.dfs(2)
# print("Connected Components count ->",g.connectedComp())
g.print()

print("########## Dijkistra's Algorithm ###########")
g.shortestDistance(0,4)
