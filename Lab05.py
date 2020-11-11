from typing import Any, List
from binarytree import build

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

    def traverse_in_order(self, visit):
        if self.left_child != None:
            self.left_child.traverse_in_order(visit)
        visit(self)
        if self.right_child != None:
            self.right_child.traverse_in_order(visit)
    
    def traverse_post_order(self,visit):
        if self.left_child != None:
            self.left_child.traverse_post_order(visit)
        if self.right_child != None:
            self.right_child.traverse_post_order(visit)
        visit(self)

    def traverse_pre_order(self,visit):
        visit(self)
        if self.left_child != None:
            self.left_child.traverse_pre_order(visit)
        if self.right_child != None:
            self.right_child.traverse_pre_order(visit)
        

    def is_leaf(self):
        if self.right_child == None and self.left_child == None:
            return True
        return False

    def __repr__(self):
        return f'{self.value}'

class BinaryTree:
    root: BinaryNode

    def __init__(self, root):
        self.root = root

    def traverse_in_order(self,visit):
        self.root.traverse_in_order(visit)

    def traverse_post_order(self,visit):
        self.root.traverse_post_order(visit)

    def traverse_pre_order(self,visit):
        self.root.traverse_pre_order(visit)

    def show(self):
        nodes = []
        current_level = [self.root]
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

        ### konwersja listy wartosci do wydruku poprzez biblioteke binarytree
        values = list()
        for node in nodes:
            if node != None:
                values.append(node.value)
            else:
                values.append(None)
        tree = build(values)
        print(tree)     
        ###       


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
def _visit(node: BinaryNode):
    v.append(node.value)

Node6 = BinaryNode(6)
Node6.add_left_child(20)
Node4 = BinaryNode(4)
Node2 = BinaryNode(2,Node4,Node6)
Node3 = BinaryNode(3)
Node3.add_right_child(21)
Node1 = BinaryNode(1)
Node9 = BinaryNode(9,Node1,Node3)
tree = BinaryTree(BinaryNode(10, Node9, Node2))

tree.traverse_in_order(_visit)
print("In order: ")
v.print()
tree.traverse_post_order(_visit)
print("Post order: ")
v.print()
tree.traverse_pre_order(_visit)
print("Pre order: ")
v.print()

assert tree.root.value == 10
assert tree.root.right_child.value == 2
assert tree.root.right_child.is_leaf() is False
assert tree.root.left_child.left_child.value == 1
assert tree.root.left_child.left_child.is_leaf() is True
print('')
tree.show()