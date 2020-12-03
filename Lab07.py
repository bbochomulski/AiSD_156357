from enum import Enum
from typing import Any, Optional, Dict, List
from Lab02 import Queue
import networkx as nx
import matplotlib.pyplot as plt


class EdgeType(Enum):
    directed = 1
    undirected = 2

class Vertex:
    data: Any
    index: int

    def __init__(self,data,index):
        self.data = data
        self.index = index

    def __repr__(self):
        return self.data

class Edge:
    source: Vertex
    destination: Vertex
    weight: Optional[float]

    def __init__(self,source,destination,weight):
        self.source = source
        self.destination = destination
        self.weight = weight

    def __repr__(self):
        return f'{self.source} -> {self.destination}'

class Graph:
    adjacencies: Dict[Vertex, List[Edge]]

    def __init__(self):
        self.adjacencies = dict()
    
    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(list(self.adjacencies.keys())):
            result = list(self.adjacencies.keys())[self.n]
            self.n += 1
            return result
        else:
            raise StopIteration

    def get(self,data):
        vertex = None
        for vertex in self.adjacencies.keys():
            if vertex.data == data:
                return vertex
        if vertex == None:
            return False

    def create_vertex(self,data):
        maxindex = 0
        if self.adjacencies:
            for key in self.adjacencies.keys():
                if key.index > maxindex:
                    maxindex = key.index
        else:
            maxindex = -1

        self.adjacencies.update({Vertex(data,maxindex+1):list()})

    def add_directed_edge(self, source: Vertex, destination: Vertex, weight:Optional[float] = None):
        self.adjacencies[source].append(Edge(source,destination,weight))

    def add_undirected_edge(self, source: Vertex, destination: Vertex, weight:Optional[float] = None):
        self.add_directed_edge(source,destination,weight)
        self.add_directed_edge(destination, source, weight)

    def add(self, edge: EdgeType, source: Vertex, destination: Vertex, weight: Optional[float] = None):
        if edge == EdgeType.directed:
            self.add_directed_edge(source, destination,weight)
        elif edge == EdgeType.undirected:
            self.add_undirected_edge(source,destination,weight)

    def traverse_breadth_first(self, visit):
        kolejka = Queue()
        odwiedzone = list()
        first = list(self.adjacencies.keys())[0]
        kolejka.enqueue(first)

        while len(kolejka) != 0:
            v = kolejka.dequeue()
            visit(v)
            if len(self.adjacencies[v]) != 0:
                krawedzie = self.adjacencies[v]
                for edge in krawedzie:
                    if edge.destination not in odwiedzone:
                        kolejka.enqueue(edge.destination)
                        odwiedzone.append(edge.destination)

    def traverse_depth_first(self, visit):
        first = list(self.adjacencies.keys())[0]
        visited = list()
        v = first
        self.dfs(v, visited, visit)

    def dfs(self,v: Vertex, visited: List[Vertex], visit):
        visit(v)
        visited.append(v)
        for edge in self.adjacencies[v]:
            if edge.destination not in visited:
                self.dfs(edge.destination, visited, visit)

    def __repr__(self):
        output = ""
        listVertex = list(self.adjacencies.keys())
        for vertex in listVertex:
            output += f'{vertex.data} ----> '
            edges = self.adjacencies[vertex]
            neighbours = list()
            for edge in edges:
                neighbours.append(edge.destination)
            output += f'{neighbours}\n'
        return output

    def show(self, path = list()):
        first = list(self.adjacencies.keys())[0]
        edges = list()
        wazony = False
        for vertex in self:
            edges.extend(self.adjacencies[vertex])
        G = nx.DiGraph()
        nodes = list()
        for e in path:
            for ed in e:
                if nodes.count(ed) == 0:
                    nodes.append(ed)
        for edge in edges:
            if edge.weight != None:
                wazony = True
                if (edge.source, edge.destination) in path:
                    G.add_edge(edge.source,edge.destination,weight=edge.weight, color='r',width=4)
                else:
                    G.add_edge(edge.source,edge.destination,weight=edge.weight,color='black',width=1)
            else:
                if (edge.source, edge.destination) in path:
                    G.add_edge(edge.source,edge.destination, color='r',width=4)
                else:
                    G.add_edge(edge.source,edge.destination,color='black',width=1)

        colors = nx.get_edge_attributes(G,'color').values()
        widths = [x for x in nx.get_edge_attributes(G,'width').values()]
        if wazony:
            pos = nx.planar_layout(G)
        else:
            pos = nx.circular_layout(G)
        if len(path) != 0:
            nx.draw(G,pos, edge_color = colors,width=widths,with_labels=True, node_size=1000, alpha=0.8, arrows=True)
        else:
            nx.draw(G,pos,width=widths,with_labels=True, node_size=1000, alpha=0.8, arrows=True)
        labels = nx.get_edge_attributes(G,'weight')
        nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
        plt.show()

listaOdwiedzonych = list()
def _visit(vertex):
    listaOdwiedzonych.append(vertex.data)

# graf = Graph()
# graf.create_vertex("A")
# graf.create_vertex("B")
# graf.create_vertex("C")
# graf.create_vertex("D")

# graf.add(EdgeType(1),graf.get("B"),graf.get("D"))
# graf.add(EdgeType(1),graf.get("C"),graf.get("B"))
# graf.add(EdgeType(1),graf.get("C"),graf.get("D"))
# graf.add(EdgeType(1),graf.get("A"),graf.get("B"))
# graf.add(EdgeType(1),graf.get("A"),graf.get("C"))

# graf.show()

# graf.traverse_breadth_first(_visit)


# graf.traverse_depth_first(_visit)
# print(listaOdwiedzonych)