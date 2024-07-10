# creating a linked list from scratch using python
# what is a linked list?
# A linked list is a linear data structure, in which the elements are not stored at contiguous memory locations.
# The elements in a linked list are linked using pointers
# A linked list is represented by a pointer to the first node of the linked list.
# A linked list is a collection of nodes where each node contains a value and a reference to the next node in the list.
# The first node is called the head and the last node is called the tail.
# The tail points to None, which indicates the end of the list.

# Node class
#this node is unidirectional
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def getValue(self):
        return self.data

    def setValue(self, data):
        self.data = data
    
    def getNext(self):
        return self.next
    
    def setNext(self, next):
        self.next = next


a = Node(1)
b = Node(2)
c = Node(3)

print(a)
print(b)
print(c)

print(a.getValue())
a.setNext(b)
print(a.getNext().getValue())
b.setNext(c)
print(a.getNext().getNext().getValue())

# how to access pointer in python?
# using the __dict__ attribute  