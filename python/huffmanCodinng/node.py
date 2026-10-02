# Node have same consept with linked list
# every objeck in memory keep data and pointer (refeerention) to another node

"""
Node huffman Tree (Binary Tree):

-> Have 2 way to left - hade and right hand

"""


class node:
    """
    This node linear, Singly Linked List

    Node A -> Node B -> Node C
    """
    def __init__(self, value, next):
        """
        This contructor to hold on new objeck
            - self.value : keep the main data
            - self.next : keep the pointer to next node (pointer)
        """
        self.value = value
        self.next = next

    def getValue(self):
        return self.value

    def getNext(self):
        return self.next

    def setValue(self,value):
        self.value = value

    def setNext(self, next):
        self.next = next

class NodeMath:
    def __init__(self, coeff, exp, next_node=None):
        self.coeff = coeff
        self.exp = exp
        self.next = next_node

    def __str__(self):
        pass

    def __init__(self, name, bases, dict, /, **kwds):
        pass

    def __add__(self, other):
        pass



first = node(3, None)
second = node(4, first)
# the mean get the new next value
print(second.getNext().getValue())
