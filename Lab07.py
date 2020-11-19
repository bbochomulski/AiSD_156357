from enum import Enum
from typing import Any, Optional, Dict, List
from Lab02 import Queue
import pandas as pd
import numpy as np
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

    def get(self,data):
        for vertex in self.adjacencies.keys():
            if vertex.data == data:
                return vertex

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
        first = list(graf.adjacencies.keys())[0]
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
        first = list(graf.adjacencies.keys())[0]
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
        listVertex = list(graf.adjacencies.keys())
        for vertex in listVertex:
            output += f'{vertex.data} ----> '
            edges = self.adjacencies[vertex]
            neighbours = list()
            for edge in edges:
                neighbours.append(edge.destination)
            output += f'{neighbours}\n'
        return output

    def show(self):
        first = list(graf.adjacencies.keys())[0]
        edges = list()
        kolejka = Queue()
        kolejka.enqueue(first)
        while len(kolejka) != 0:
            v = kolejka.dequeue()
            for edge in self.adjacencies[v]:
                if edge not in edges:
                    edges.append(edge)
                    kolejka.enqueue(edge.destination)
        od = list()
        do = list()
        for edge in edges:
            od.append(edge.source)
            do.append(edge.destination)

        df = pd.DataFrame({ 'from':od, 'to':do})
        G=nx.from_pandas_edgelist(df, 'from', 'to', create_using=nx.DiGraph())
        nx.draw_kamada_kawai(G, with_labels=True, node_size=1000, alpha=0.8, arrows=True)
        # nx.draw_circular(G, with_labels=True, node_size=1000, alpha=0.8, arrows=True)
        plt.show()

listaOdwiedzonych = list()
def _visit(vertex):
    listaOdwiedzonych.append(vertex.data)

graf = Graph()
graf.create_vertex("v0")
graf.create_vertex("v1")
graf.create_vertex("v2")
graf.create_vertex("v3")
graf.create_vertex("v4")
graf.create_vertex("v5")

graf.add(EdgeType(1),graf.get("v0"),graf.get("v1"))
graf.add(EdgeType(2),graf.get("v0"),graf.get("v5"))
graf.add(EdgeType(1),graf.get("v5"),graf.get("v2"))
graf.add(EdgeType(1),graf.get("v5"),graf.get("v1"))
graf.add(EdgeType(2),graf.get("v2"),graf.get("v3"))
graf.add(EdgeType(1),graf.get("v2"),graf.get("v1"))
graf.add(EdgeType(1),graf.get("v3"),graf.get("v4"))
graf.add(EdgeType(2),graf.get("v4"),graf.get("v1"))
graf.add(EdgeType(1),graf.get("v4"),graf.get("v5"))

print(graf)

graf.show()

# graf.traverse_breadth_first(_visit)


# graf.traverse_depth_first(_visit)
# print(listaOdwiedzonych)