from typing import Any, List
import queue

class TreeNode:
    value: Any
    children: List['TreeNode']

    def __init__(self, value = Any):
        self.value = value
        self.children = list()

    def is_leaf(self):
        if len(self.children) == 0:
            return True
        return False
    
    def add(self,child):
        self.children.append(child)
    
    def for_each_deep_first(self, visit):
        visit(self)
        for child in self.children:
            child.for_each_deep_first(visit)
        

    def for_each_level_order(self,visit):
        visit(self)
        kolejka = queue.Queue()
        for child in self.children:
            kolejka.put(child)
        
        while(kolejka.empty() != True):
            element = kolejka.get()
            visit(element)
            for child in element.children:
                kolejka.put(child)

    def search(self, value: Any):
        if self.value == value:
            return True
        for node in self.children:
            if node.search(value):
                return True
        return False

    def __repr__(self):
        return f'{self.value}'

class Tree:
    root: TreeNode

    def __init__(self, root):
        self.root = root

    def for_each_deep_first(self,visit):
        self.root.for_each_deep_first(visit)

    def for_each_level_order(self,visit):
        self.root.for_each_level_order(visit)

    def add(self, value: Any, parent_value: Any):
        kolejka = queue.Queue()
        node = self.root
        if self.root.value == parent_value:
            self.root.add(TreeNode(value))
        else:
            for child in node.children:
                kolejka.put(child)
        
        while(kolejka.empty() != True):
            element = kolejka.get()
            if element.value == parent_value:
                element.add(TreeNode(value))
                break
            else:
                for child in element.children:
                    kolejka.put(child)

                
#### klasa zajmujaca sie trzymaniem elementow funkcji _visit ####
class visited:
    visited: list

    def __init__(self):
        self.visited = list()

    def append(self, value):
        self.visited.append(value)

    def print(self):
        print(self.visited)
        self.visited.clear()

v = visited()
def _visit(node: TreeNode):
    v.append(node.value)

#### tworzenie drzewa "na piechote" ####
NodeA = TreeNode('A')
NodeB = TreeNode('B')
NodeC = TreeNode('C')
NodeD = TreeNode('D')
NodeE = TreeNode('E')
NodeF = TreeNode('F')
NodeG = TreeNode('G')
NodeH = TreeNode('H')
NodeI = TreeNode('I')

NodeF.add(NodeB)
NodeF.add(NodeG)
NodeB.add(NodeA)
NodeB.add(NodeD)
NodeD.add(NodeC)
NodeD.add(NodeE)
NodeG.add(NodeI)
NodeI.add(NodeH)

drzewo = Tree(NodeF)
#### tworzenie drzewa2 używając metod klasy ####

drzewo2 = Tree(TreeNode('F'))
drzewo2.add('B','F')
drzewo2.add('G','F')
drzewo2.add('A','B')
drzewo2.add('D','B')
drzewo2.add('C','D')
drzewo2.add('E','D')
drzewo2.add('I','G')
drzewo2.add('H','I')

#### wydruk obu drzew ####

drzewo.for_each_deep_first(_visit)
v.print()
drzewo2.for_each_level_order(_visit)
v.print()

#### test metody search ####
assert drzewo2.root.search('E') == True

drzewo.show()