# This algo is use to find the shortest path between src vertex and all other vertex in
# a weighted graph and directed graph.
# A very imp. use of this algo. is to check if there is a negative cycle in a graph.
# This algo works to find shortest path in a graph having negative edges but not in which
# have negative cycle.

import sys
maxVal = sys.maxsize
class Graph:
    def __init__(self,n) -> None:
        self.v = n
        self.adj = []
    def add_edge(self,u,v,w):
        self.adj.append([u,v,w])
        
    def print(self,dist):
        print("Vertex Distance from Source") 
        for i in range(self.v): 
            print("{0}\t\t{1}".format(i, dist[i])) 

    def bellmonFords(self,src):
        shortest_path_dist = [maxVal]*self.v
        shortest_path_dist[src] = 0

        for i in range(self.v-1):
            for u,v,w in self.adj:
                if shortest_path_dist[v]>shortest_path_dist[u]+w:
                    shortest_path_dist[v] = shortest_path_dist[u]+w
        flag = False
        for u,v,w in self.adj:
            if shortest_path_dist[v]>shortest_path_dist[u]+w:
                print("Negative Cycle Detected")
                flag = True
                break
        if not flag:
            print("Your Shortest Path Distance")
            print(shortest_path_dist)
            

g = Graph(3)
g.add_edge(0,1,3)
g.add_edge(1,2,-4)
g.add_edge(2,0,-2)
# g.dfs(2)
# print("Connected Components count ->",g.connectedComp())

print("########## Bellmon Ford's Algorithm ###########")
g.bellmonFords(0)
