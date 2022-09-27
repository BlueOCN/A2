"""
    GRAPH DECLARATION FOR ADJACENCY LIST

    In this representation all the vertices connected to a vertex v are listed on an adjacency list for that vertex v. 
    This can be easily implemented with linked lists. That means, for each vertex v we use a linked list and list 
    nodes represents the connections between v and other vertices to which v has an edge. 
    The IOtnl number of linked lists is equol to the number of vertices in the graph. 
"""
import sys


class Vertex:
    def __init__(self, node) -> None:
        self.id = node
        self.adjacent = {}
        self.distance = sys.maxsize
        self.visited = False
        self.previous = None
        self.color = 'white'
    
    def addNeighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight
    
    def getConnections(self):
        return self.adjacent.keys()
    
    def getVertexID(self):
        return self.id
    
    def getWeight(self, neighbor):
        return self.adjacent[neighbor]

    def setDistance(self, dist):
        self.distance = dist
    
    def getDistance(self):
        return self.distance

    def setPrevious(self, prev):
        self.previous = prev

    def setVisisted(self):
        self.visited = True
    
    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color
    
    def __str__(self) -> str:
        return str(self.id) + 'adjacent: ' + str([x.id for x in self.adjacent])


class Graph:
    def __init__(self) -> None:
        self.vertDictionary = {}
        self.numVertices = 0
    
    def __iter__(self):
        return iter(self.vertDictionary.values())
    
    def addVertex(self, node):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(node)
        self.vertDictionary[node] = newVertex
        return newVertex
    
    def getVertex(self, n):
        if n in self.vertDictionary:
            return self.vertDictionary[n]
        else:
            return None
    
    def addEdge(self, frm, to, cost = 0):
        if frm not in self.vertDictionary:
            self.addVertex(frm)
        if to not in self.vertDictionary:
            self.addVertex(to)
        self.vertDictionary[frm].addNeighbor(self.vertDictionary[to], cost)
        self.vertDictionary[to].addNeighbor(self.vertDictionary[frm], cost)

    def getVertices(self):
        return self.vertDictionary.keys()
    
    def setPrevious(self, current):
        self.previous = current

    def getPrevious(self, current):
        return self.previous

    def getEdges(self):
        edges = []
        for v in G:
            for w in v.getConnections():
                vid = v.getVertexID()
                wid = w.getVertexID()
                edges.append((vid, wid, v.getWeight(w)))
        return edges

def dfs(G, currentVert, visited):
    visited[currentVert] = True
    print(currentVert.getVertexID(), end=' ')
    for nbr in currentVert.getConnections():
        if nbr not in visited:
            dfs(G, nbr, visited)

def DFSTraversal(G):
    visited = {}
    for currentVert in G:
        if currentVert not in visited:
            dfs(G, currentVert, visited)


def BFSTraversal(G, s):
    start = G.getVertex(s)
    start.setDistance(0)
    start.setPrevious(None)
    vertQueue = list()
    vertQueue.append(start)
    while (len(vertQueue) > 0):
        currentVert = vertQueue.pop()
        print(currentVert.getVertexID(), end=' ')
        for nbr in currentVert.getConnections():
            if(nbr.getColor() == 'white'):
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPrevious(currentVert)
                vertQueue.append(nbr)
            currentVert.setColor('black')

def BFS(G):
    for v in G:
        if (v.getColor() == 'white'):
            BFSTraversal(G, v.getVertexID())


if __name__ == '__main__':
    # Creates a graph
    G = Graph()

    # Adds nodes
    G.addVertex('1')
    G.addVertex('2')
    G.addVertex('3')
    G.addVertex('4')
    G.addVertex('5')
    G.addVertex('6')
    G.addVertex('7')
    G.addVertex('8')
    G.addVertex('9')

    # Adds connections
    G.addEdge('1','2', 1)
    G.addEdge('1','3', 1)
    G.addEdge('1','4', 1)
    G.addEdge('2','5', 1)
    G.addEdge('2','6', 1)
    G.addEdge('2','3', 1)
    G.addEdge('3','7', 1)
    G.addEdge('3','8', 1)
    G.addEdge('4','8', 1)
    G.addEdge('7','9', 1)

    print('Graph data:')
    print(G.getEdges())
    print('\nDepth First Traversal:',end=' ')
    DFSTraversal(G)
    print('\nBreadth First Traversal:',end=' ')
    BFS(G)
