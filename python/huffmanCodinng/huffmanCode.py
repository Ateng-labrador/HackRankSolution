class Node:
    # Leaf node
    def __init__(self, d, i, left=None, right=None):
        self.data = d
        self.index = i

        self.left = left
        self.right = right


def preOrder(root, ans, curr):
    if root is None:
        return

    if root.left is None and root.right is None:
        if curr == "":
            curr = "0"
        ans.append(curr)
        return

    preOrder(root.left, ans, curr + '0')
    preOrder(root.right, ans, curr + '1')

def huffmanCodes(s, freq):
    n = len(s)
    pq = []
    for i in range(n):
        tmp = Node(freq[i], i)
        heapq.heappush(pq, (tmp.data, tmp.index, tmp))

    if n == 1:
        return ["0"]

    while len(pq) >= 2:
        
