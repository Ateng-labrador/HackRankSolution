import heapq
from collections import Counter, defaultdict
import struct


class HuffmanNode:
    def __init__(self, value=None, freq=0, left=None, right=None):
        self.value = value
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(freq_map):
    """Membuat Huffman Tree"""
    heap = [HuffmanNode(value=v, freq=f) for v, f in freq_map.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(freq=left.freq + right.freq, left=left, right=right)
        heapq.heappush(heap, merged)
    return heap[0]

def build_codebook(root, prefix="", codebook=None):
    "Untuk membangun tabel kode"
    if codebook is None:
        codebook = {}
    if root.value is not None:
        codebook[root.value] = prefix if prefix else "0"
    else:
        build_codebook(root.left + "0", codebook)
        build_codebook(root.right + "1", codebook)
    return codebook


# Tanpa Menggunakan node
def huffman_code(text):
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1


    count = 0
    heap = []
    for c, f in freq.items():
        heap.append([f, count, {c: ""}])
        count += 1
    heapq.heapify(heap)

    while len(heap) > 1:
        f1,_ ,c1 = heapq.heappop(heap)
        f2,_ ,c2 = heapq.heappop(heap)

        for char in c1:
            c1[char] = "0" + c1[char]
        for char in c2:
            c2[char] = "1" + c2[char]

        c1.update(c2)
        count += 1
        heapq.heappush(heap, [f1 + f2, count,c1])
    return heap[0][2] if heap else {}


# Menggunakan Array


x = "khansa"
code = huffman_code(x)
print(code)

