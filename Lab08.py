from Lab07 import Graph, Vertex, EdgeType, Edge
from Lab02 import Queue

class GraphPath:
    graph: Graph
    source: Vertex
    destination: Vertex
    path: list
    
    def __init__(self,graph: Graph,source:Vertex, destination:Vertex):
        self.graph = graph
        if source and destination in self.graph:
            self.source = source
            self.destination = destination
            self.path = list()
            if self.graph.adjacencies[self.source][0].weight != None:
                print("Graf wazony: uzywam algorytmu Dijkstry")
                self._wazony = True
                self._dijkstra()
            else:
                print("Graf niewazony: uzywam przechodzenia wszerz")
                self._wazony = False
                self._wszerz()
        else:
            if source not in self.graph:
                print("Wierzcholek startowy nie istnieje")
            if destination not in self.graph:
                print("Wierzcholek docelowy nie istnieje")
    
    def __repr__(self):
        string = f"Sciezka {self.source} -> {self.destination} wykonana za pomoca"
        lista = ' -> '.join(str(bit) for bit in self.path)
        if self._wazony:
            string = f"{string} algorytmu Dijkstry: {lista}\nKoszt: {self.price}"
            return string
        else:
            string = f"{string} przechodzenia wszerz: {lista}"
            return string
        

    def _dijkstra(self):
        visited = list()
        price = {self.source : 0, self.destination : 999999999}
        parents = {self.destination : None}
        for neighbor in self.graph.adjacencies[self.source]:
            parents[neighbor.destination] = self.source
        v = self.source
        while v:
            c = price[v]
            for edge in self.graph.adjacencies[v]:
                nc = c + edge.weight
                if edge.destination not in price.keys():
                    price[edge.destination] = nc
                    parents[edge.destination] = v
                elif price[edge.destination] > nc:
                    price[edge.destination] = nc
                    parents[edge.destination] = v
            visited.append(v)
            if v != self.destination:
                v = self.lowVert(price,visited)
            else:
                v = None
        v = self.destination
        while v in parents.keys():
            self.path.append(v)
            v = parents[v]
        self.path.append(self.source)
        self.path.reverse()
        self.price = price[self.destination]

        # print(f'{self.source} -> {self.destination}:\nKoszt: {price[self.destination]}\nSciezka: ',end='')
        # print(*self.path, sep=' -> ')
    
        
    def lowVert(self, price, visited):
        lc = 9999999999
        for vertex in price.keys():
            if price[vertex] < lc and vertex not in visited:
                lc = price[vertex]
                lcv = vertex
        return lcv

    def _wszerz(self):
        queue = Queue()
        visited = list()
        queue.enqueue([self.source])
        while queue:
            br = False
            p = queue.dequeue()
            v = p[-1]
            for n in self.graph.adjacencies[v]:
                if n.destination not in visited:
                    np = p.copy()
                    np.append(n.destination)
                    visited.append(n.destination)
                    queue.enqueue(np)
                if n.destination == self.destination:
                    br = True
            if br:
                break
        self.path = queue.dequeue()
        self.path.append(self.destination)
        # print(f'{self.source} -> {self.destination}:')
        # print('Sciezka: ',end='')
        # print(*self.path, sep=' -> ')

    def show(self):
        edges = list()
        path = self.path.copy()
        while len(path) > 1:
            v = path.pop(0)
            edges.append((v,path[0]))
        self.graph.show(edges)


listaOdwiedzonych = list()
def _visit(vertex):
    listaOdwiedzonych.append(vertex.data)

graf = Graph()
for _ in ["A","B","C","D"]:
    graf.create_vertex(_)

testGraf = True  # True: graf wazony    False: graf niewazony
testDirected = 1 # 1: graf skierowany     2: graf nieskierowany

if testGraf:
    graf.add(EdgeType(testDirected),graf.get("B"),graf.get("D"),2)
    graf.add(EdgeType(testDirected),graf.get("C"),graf.get("B"),5)
    graf.add(EdgeType(testDirected),graf.get("C"),graf.get("D"),9)
    graf.add(EdgeType(testDirected),graf.get("A"),graf.get("B"),30)
    graf.add(EdgeType(testDirected),graf.get("A"),graf.get("C"),10)
else:
    graf.add(EdgeType(testDirected),graf.get("B"),graf.get("D"))
    graf.add(EdgeType(testDirected),graf.get("C"),graf.get("B"))
    graf.add(EdgeType(testDirected),graf.get("C"),graf.get("D"))
    graf.add(EdgeType(testDirected),graf.get("A"),graf.get("B"))
    graf.add(EdgeType(testDirected),graf.get("A"),graf.get("C"))

sciezka = GraphPath(graf,graf.get("A"), graf.get("D"))

# graf.show()
sciezka.show()
print(sciezka)