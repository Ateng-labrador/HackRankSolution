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

class NodePolynomial:
    def __init__(self, coeff, exp, next_node=None):
        self.coeff = coeff
        self.exp = exp
        self.next = next_node

# Child Class
class PrintPolynomial(NodePolynomial):
    def __init__(self, coeff, exp, next_node=None):
        super().__init__(coeff, exp, next_node)

    def traverse_chain(self):
        current = self
        persamaan = []

        while current:
            if current.exp == 0:
                persamaan.append(f"{current.coeff}")
            else:
                persamaan.append(f"{current.coeff}x^{current.exp}")
            current = current.next
        print(" + ".join(persamaan))



# make equation: 3x^3 + 5x^2 + 2
term3 = PrintPolynomial(coeff=2, exp=0)
term2 = PrintPolynomial(coeff=5, exp=1, next_node=term3)
term1 = PrintPolynomial(coeff=3, exp=3, next_node=term2)

term1.traverse_chain()




# first = node(3, None)
# second = node(4, first)
# # the mean get the new next value
# print(second.getNext().getValue())
