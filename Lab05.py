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
        self.root = BinaryNode(root)

    def traverse_in_order(self,visit):
        self.root.traverse_in_order(visit)

    def traverse_post_order(self,visit):
        self.root.traverse_post_order(visit)

    def traverse_pre_order(self,visit):
        self.root.traverse_pre_order(visit)

    def show(self):
        nodes = [] # lista która będzie zawierać wyjściową liste obiektów
        current_level = [self.root] # lista zawierająca węzly z aktualnego poziomu - wstępnie korzeń
        while current_level: # dopóki w aktualnym poziomie są jakieś elementy
            for node in current_level: # przepisuje elementy aktualnego poziomu do 
                nodes.append(node)     # listy wynikowej
            next_level = list() # tworzy pustą liste która będzie zawierać elementy z następnego poziomu
            for n in current_level: # przechodzi po wszystkich węzłach aktualnego poziomu
                if n != None: # jeśli węzeł nie jest obiektem None
                    if n.left_child: # jeśli węzeł posiada lewe dziecko
                        next_level.append(n.left_child) # dodaje lewe dziecko do listy następnego poziomu
                    else: # albo
                        next_level.append(None) # albo jeśli nie posiada dziecka to podaje do listy następnego poziomu obiekt None
                    if n.right_child: # jeśli węzeł posiada prawe dziecko 
                        next_level.append(n.right_child) # dodaje prawe dziecko do listy następnego poziomu
                    else: # albo
                        next_level.append(None) # jeśli nie posiada to dodaje do listy następnego poziomu obiekt None
            current_level = next_level # zmiana aktualnego poziomu na następny

        ### konwersja listy wartosci do wydruku poprzez biblioteke binarytree
        values = list() # utworzenie pustej listy wartości
        for node in nodes: # przejście po liście z poprzedniego fragmentu zawierającej liste obiektów w odpowiedniej kolejności
            if node != None: # jeśli węzeł nie jest obiektem None
                values.append(node.value) # dodaje wartość węzła do listy wartości
            else: # albo
                values.append(None) # dodaje wartość None do listy wartości żeby biblioteka binarytree narysowała drzewo tak jak trzeba
        tree = build(values) # zbudowanie drzewa metodą build z biblioteki binarytree
        print(tree) # wydrukowanie drzewa na ekran
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

###### przestrzen testowa #######

tree = BinaryTree(10)
tree.root.add_left_child(9)
tree.root.add_right_child(11)

tree.root.left_child.add_left_child(15)
tree.root.left_child.add_right_child(18)

tree.show()