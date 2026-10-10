import heapq


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
    return heap[0][1] if heap else {}


x = "khansa"
code = huffman_code(x)
print(code)

