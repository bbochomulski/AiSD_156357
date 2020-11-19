from typing import Any, List
from binarytree import build
import types
import queue

class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value = None,left_child = None, right_child = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child
    
    def add_left_child(self, value: Any):
        self.left_child = (BinaryNode(value))

    def add_right_child(self, value: Any):
        self.right_child = (BinaryNode(value))

    def min(self):
        nodes = BinarySearchTree.node_list(self,self)
        min = nodes[0]
        print(nodes)
        for node in nodes:
            try:
                if node.value < min.value:
                    min = node
            except:
                pass
        return min

    def is_leaf(self):
        if self.left_child == None and self.right_child == None:
            return True
        return False

    def __repr__(self):
        return f'{self.value}'

class BinarySearchTree:
    root: BinaryNode

    def __init__(self, root):
        self.root = BinaryNode(root)

    def node_list(self, _from: BinaryNode):
        nodes = []
        current_level = [_from]
        while current_level:
            for node in current_level:
                nodes.append(node)
            next_level = list()
            for n in current_level:
                if n != None:
                    if n.left_child:
                        next_level.append(n.left_child)
                    else:
                        next_level.append(None)
                    if n.right_child:
                        next_level.append(n.right_child)
                    else:
                        next_level.append(None)
            current_level = next_level
        return nodes

    def show(self):
        values = list()
        kolejka = queue.Queue()
        kolejka.put(self.root)

        while kolejka.empty() != True:
            element = kolejka.get()
            if element != None:
                values.append(element.value)
            else:
                values.append(None)
                kolejka.put(None)
                kolejka.put(None)
                continue

            if element.left_child != None:
                kolejka.put(element.left_child)
            else:
                kolejka.put(None)
            if element.right_child != None:
                kolejka.put(element.right_child)
            else:
                kolejka.put(None)

            checklist = list()
            while kolejka.empty() != True:
                checklist.append(kolejka.get())
            check = False
            for element in checklist:
                if element != None:
                    check = True
                kolejka.put(element)
            if not check:
                break
        tree = build(values)
        print(tree)

    def contains(self, value):
        nodes = self.node_list(self.root)
        for node in nodes:
            if node != None:
                if node.value == value:
                    return True
        return False

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, _from: BinaryNode, value: Any):
        current = _from

        try:
            # print(f'current = {current.value}\nvalue = {value}')
            if value < current.value:
                current.left_child = self._insert(current.left_child, value)
            elif value >= current.value:
                current.right_child = self._insert(current.right_child, value)
        except:
            return BinaryNode(value)
        return current
    
    def insertlist(self,list):
        for value in list:
            self.insert(value)

    def remove(self,value):
        if(self.contains(value)):
            self.root = self._remove(self.root,value)

    def _remove(self,node,value):
        if value == node.value:
            if node.is_leaf():
                return None
            if node.left_child == None:
                return node.right_child
            if node.right_child == None:
                return node.left_child
            node.value = node.right_child.min().value
            node.right_child = self._remove(node.right_child,node.value)
        elif value < node.value:
            node.left_child = self._remove(node.left_child,value)
        else:
            node.right_child = self._remove(node.right_child,value)
        return node

tree = BinarySearchTree(8)

tree.insertlist([5,7,9,3,4,5,7,12,15,16,17,13,14,14,18,19,13])

# print("przed remove(13)")
tree.show()

# tree.remove(13)

# print("po remove(13)")
# tree.show()