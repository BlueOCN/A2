from platform import node
from signal import valid_signals


"""
    GRAPH DECLARATION FOR ADJACENCY MATRIX

    In this meLhod, we use a matrix with sizt: V x V. The values of matrix arc boolean. Let us assume the matrix is 
    Adj. The value Adj[u, 11] is set to I if there is an edge from vertex u to vertex v and 0 otherwise. 
    In the matrix, each edge is represented by two bits for undirected graphs. That means, an edge from u to v is 
    represented by 1 value in both Adflu, vj and Adflii, v]. To save time, we can process only half of this symmetric 
    matrix. Also, we can assume that there is an ~edge" from each vertex lo itself. So, Adj[u, uJ is set to I for all veniccs. 
    If the graph is a direc ted graph then we need to mark only one entry in the adjacency matrix. 
"""


class Vertex:
    def __init__(self, node) -> None:
        self.id = node
        self.visited = False

    def addNeighbor(self, neighbor, G):
        G.addEdge(self.id, neighbor)
    
    def getConnections(self, G):
        return G.adjMatrix[self.id]
    
    def getVertexID(self):
        return self.id
    
    def setVertexID(self, id):
        self.id = id

    def setVisited(self):
        self.visited = True

    def __str__(self) -> str:
        return str(self.id)


class Graph:
    def __init__(self, numVertices, cost = 0) -> None:
        self.adjMatrix = [[-1]*numVertices for _ in range(numVertices)]
        self.numVertices = numVertices
        self.vertices = []
        for i in range(0, numVertices):
            newVertex = Vertex(i)
            self.vertices.append(newVertex)
    
    def setVertex(self, vtx, id):
        if 0 <= vtx < self.numVertices:
            self.vertices[vtx].setVertexID(id)
    
    def getVertex(self, n):
        for vertxin in range(0, self.numVertices):
            if n == self.vertices[vertxin].getVertexID():
                return vertxin
        else:
            return -1
    
    def addEdge(self, frm, to, cost = 0):
        if self.getVertex(frm) != -1 and self.getVertex(to) != -1:
            self.adjMatrix[self.getVertex(frm)][self.getVertex(to)] = cost
            self.adjMatrix[self.getVertex(to)][self.getVertex(frm)] = cost

    def getVertices(self):
        vertices = []
        for vertxin in range(0, self.numVertices):
            vertices.append(self.vertices[vertxin].getVertexID())
        return vertices
    
    def printMatrix(self):
        for u in range(0 , self.numVertices):
            row = []
            for v in range(0, self.numVertices):
                row.append(self.adjMatrix[u][v])
            print(row)
    
    def getEdges(self):
        edges = []
        for v in range(0, self.numVertices):
            for u in range(0, self.numVertices):
                if self.adjMatrix[u][v] != -1:
                    vid = self.vertices[v].getVertexID()
                    wid = self.vertices[u].getVertexID()
                    edges.append((vid, wid, self.adjMatrix[u][v]))
        return edges
    
def dfs(G, currentVert, visited):
    visited[currentVert] = True
    print("Traversal: " + currentVert.getVertexID())
    for nbr in currentVert.getVertexID():
        if nbr not in visited:
            dfs(G, nbr, visited)

def DFSTraversal(G):
    visited = {}
    for currentVert in G:
        if currentVert not in visited:
            dfs(G, currentVert, visited)

if __name__ == '__main__':
    G = Graph(5)
    G.setVertex(0,'a')
    G.setVertex(1,'b')
    G.setVertex(2,'c')
    G.setVertex(3,'d')
    G.setVertex(4,'e')
    print('Graph data:')
    G.addEdge('a','e', 10)
    G.addEdge('a','c', 20)
    G.addEdge('c','b', 30)
    G.addEdge('b','c', 40)
    G.addEdge('e','d', 50)
    G.addEdge('f','e', 60)
    G.printMatrix()
    print(G.getEdges())
    DFSTraversal(G)