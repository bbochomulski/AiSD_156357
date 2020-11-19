from typing import Any

class Node:
    value: Any
    next: None

    def __init__(self, value=Any, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        if(self.next==None):
            return f'{self.value}'
        return f'{self.value} -> {self.next}'

class LinkedList:
    head: Node
    tail: Node

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def push(self, wartosc):
        nowy = Node(wartosc, self.head)
        self.head = nowy
        if(self.tail==None):
            self.tail = nowy
        
    def append(self,wartosc):
        nowy = Node(wartosc)
        if(self.tail == None and self.head == None):
            self.head = nowy
            self.tail = nowy
        else:
            self.tail.next = nowy
            self.tail = nowy

    def node(self, at):
        licznik = 0
        aktualny = self.head
        while (licznik != at):
            aktualny = aktualny.next
            licznik += 1
            if(aktualny.next == None):
                return aktualny
        return aktualny

    def insert(self,wartosc, after):
        if(after.next != None):
            nowy_obiekt = Node(value = wartosc, next=after.next)
        else:
            nowy_obiekt = Node(value = wartosc, next=None)
        after.next = nowy_obiekt

    def pop(self):
        obiekt = self.head
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return obiekt.value
        else:
            self.head = self.head.next
            obiekt.next = None
            return obiekt.value
    
    def remove_last(self):
        obiekt = self.head
        while(obiekt.next.next != None):
            obiekt = obiekt.next
        ostatni = obiekt.next
        obiekt.next = None
        return ostatni.value
    
    def remove(self,obj):
        if(obj.next != None):
            usuniety = obj.next
        else:
            return None
        obj.next = usuniety.next
        return usuniety.value
        
    def __repr__(self):
        return f'{self.head}'
    
    def __len__(self):
        if (self.head == None):
            return 0
        
        obiekt = self.head
        licznik = 1
        while obiekt.next != None:
            obiekt = obiekt.next
            licznik += 1
        return licznik

class Queue():
    queue : LinkedList
    
    def __init__(self):
        self.queue = LinkedList()

    def peek(self):                    # zwraca wartosc pierwszego elementu w kolejce
        return self.queue.head.value
    
    def enqueue(self, wartosc):        # dodaje element do kolejki                         
        self.queue.append(wartosc)
    
    def dequeue(self):                 # zwraca pierwszy element w kolejce
        return self.queue.pop()

    def __repr__(self):
        return str(self.queue)
    
    def __len__(self):
        return len(self.queue)

        
# ####### Zadanie 1 #######
# list_ = LinkedList()

# assert list_.head == None

# list_.push(1)
# list_.push(0)
# assert str(list_) == '0 -> 1'

# list_.append(9)
# list_.append(10)
# assert str(list_) == '0 -> 1 -> 9 -> 10'

# middle_node = list_.node(1)
# list_.insert(5,middle_node)
# assert str(list_) == '0 -> 1 -> 5 -> 9 -> 10'

# first_element = list_.node(0)
# returned_first_element = list_.pop()
# assert first_element.value == returned_first_element


# last_element = list_.node(at=3)
# returned_last_element = list_.remove_last()

# assert last_element.value == returned_last_element
# assert str(list_) == '1 -> 5 -> 9'

# second_node = list_.node(at=1)
# list_.remove(second_node)
# assert str(list_) == '1 -> 5'

# ####### Zadanie 3 #######

# queue = Queue()

# assert len(queue) == 0

# queue.enqueue('klient1')
# queue.enqueue('klient2')
# queue.enqueue('klient3')

# assert str(queue) == 'klient1 -> klient2 -> klient3'

# client_first = queue.dequeue()

# assert client_first == 'klient1'
# assert str(queue) == 'klient2 -> klient3'
# assert len(queue) == 2