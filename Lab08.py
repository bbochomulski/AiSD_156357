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
            self.path = self.selectMethod()
        else:
            if source not in self.graph:
                print("Wierzcholek startowy nie istnieje")
            if destination not in self.graph:
                print("Wierzcholek docelowy nie istnieje")
    
    def __repr__(self):
        strng = f"Sciezka {self.source} -> {self.destination} wykonana za pomoca"
        lista = ' -> '.join(str(bit) for bit in self.path)
        if self._wazony:
            strng = f"{strng} algorytmu Dijkstry: {lista}\nKoszt: {self.price}"
            return strng
        else:
            strng = f"{strng} przechodzenia wszerz: {lista}"
            return strng

    def selectMethod(self):
        if self.graph.adjacencies[self.source][0].weight != None:
            print("Graf wazony: uzywam algorytmu Dijkstry")
            self._wazony = True
            return self._dijkstra()
        else:
            print("Graf niewazony: uzywam przechodzenia wszerz")
            self._wazony = False
            return self._wszerz()
        

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
        result = list()
        while v in parents.keys():
            result.append(v)
            v = parents[v]
        result.append(self.source)
        result.reverse()
        self.price = price[self.destination]

        # print(f'{self.source} -> {self.destination}:\nKoszt: {price[self.destination]}\nSciezka: ',end='')
        # print(*result, sep=' -> ')
        return result
    
        
    def lowVert(self, price, visited):
        lc = 9999999999
        for vertex in price.keys():
            if price[vertex] < lc and vertex not in visited:
                lc = price[vertex]
                lcv = vertex
        return lcv

    def _wszerz(self):
        queue = Queue()
        visited = [self.source]
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
                        while queue:
                            result = queue.dequeue()
                            if result[0] == self.source and result[-1] == self.destination:
                                break
        # print(f'{self.source} -> {self.destination}:')
        # print('Sciezka: ',end='')
        # print(*result, sep=' -> ')
        return result

    def show(self):
        edges = list()
        path = self.path.copy()
        while len(path) > 1:
            v = path.pop(0)
            edges.append((v,path[0]))
        print(edges)
        self.graph.show(edges)

graf = Graph()
for x in ["0","1","2","3","4","5","6"]:
    graf.create_vertex(x)

#graf.add(EdgeType(1/2),wierzcholek_od,wierzcholek_do,waga)
graf.add(EdgeType(1),graf.get("0"),graf.get("1"))
graf.add(EdgeType(1),graf.get("0"),graf.get("4"))
graf.add(EdgeType(1),graf.get("0"),graf.get("2"))
graf.add(EdgeType(1),graf.get("0"),graf.get("5"))
graf.add(EdgeType(1),graf.get("2"),graf.get("4"))
graf.add(EdgeType(1),graf.get("2"),graf.get("6"))
graf.add(EdgeType(1),graf.get("2"),graf.get("3"))
graf.add(EdgeType(1),graf.get("2"),graf.get("5"))
graf.add(EdgeType(1),graf.get("3"),graf.get("5"))
graf.add(EdgeType(1),graf.get("3"),graf.get("6"))

sciezka = GraphPath(graf,graf.get("0"), graf.get("6"))

# graf.show()
sciezka.show()
