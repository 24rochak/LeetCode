# Python implementation of Kosaraju's algorithm to print all SCCs

from collections import defaultdict


class Graph:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A function used by DFS
    def DFSUtil(self, v, visited, temp):
        visited[v] = True
        print("visited:", v)
        temp.append(v)
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited, temp)

    def fillOrder(self, v, visited, stack):
        print("Fillorder:", v)
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                self.fillOrder(i, visited, stack)
        print("appending:", v)
        stack.append(v)

    def getTranspose(self):
        g = Graph(self.V)

        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j, i)
        return g

    def printSCCs(self):

        stack = []
        visited = [False] * (self.V)
        for i in range(self.V):
            if visited[i] == False:
                print("Processing:", i)
                self.fillOrder(i, visited, stack)
        print(stack)
        gr = self.getTranspose()
        visited = [False] * (self.V)
        components = []
        while stack:
            i = stack.pop()
            print("popped:", i)
            temp = []
            if visited[i] == False:
                gr.DFSUtil(i, visited, temp)
                print("")
            if temp:
                components.append(temp)
        print(components)


g = Graph(5)
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 1)
g.addEdge(0, 3)
g.addEdge(3, 4)

print("Following are strongly connected components in given graph")
g.printSCCs()
