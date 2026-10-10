import heapq

class Node:
    # Node 
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # (Less Than)
    def __lt__(self, other):
        return self.freq < other.freq


# Pembuatan huffman tree
def build_huffman_tree(text):
    # cout freq char
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1

    # input all node into min-heap
    heap = [Node(char, freq) for char, freq in freq.items()]
    heapq.heapify(heap)

    # marge twwo small node until 1 root
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    root = heap[0]

    # generate huffman code from tree
    huffman_codes = {}
    def generate_codes(node, current_code=""):
        if node is None:
            return
        if node.char is not None:  # Mencapai leaf node
            huffman_codes[node.char] = current_code
            return
        generate_codes(node.left, current_code + "0")
        generate_codes(node.right, current_code + "1")

    generate_codes(root)
    return root, huffman_codes

def encode(text, huffman_codes):
    return "".join(huffman_codes[char] for char in text)

def decode(encoded_text, root):
    if not root:
        return ""
    
    decoded_text = []
    current = root
    for bit in encoded_text:
        current = current.left if bit == '0' else current.right

        if current.char is not None:  # Daun ditemukan
            decoded_text.append(current.char)
            current = root

    return "".join(decoded_text)

# --- Contoh Pengujian ---
text = "KHANSA AULIA HADIWIJAYA"
root, codes = build_huffman_tree(text)

print("Tabel Kode Huffman:")
for char, code in sorted(codes.items()):
    print(f"'{char}': {code}")

encoded = encode(text, codes)
decoded = decode(encoded, root)

print(f"\nTeks Asli     : {text}")
print(f"Hasil Enkoding : {encoded}")
print(f"Hasil Dekoding : {decoded}")
