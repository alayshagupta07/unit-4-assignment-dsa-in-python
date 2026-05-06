import heapq

# Min-Heap implementation using Python's heapq
class MinHeap:
    def __init__(self):
        self.heap = []

    # Insert element
    def insert(self, val):
        heapq.heappush(self.heap, val)

    # Peek (get minimum without removing)
    def peek(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    # Extract minimum element
    def extract_min(self):
        if len(self.heap) == 0:
            return None
        return heapq.heappop(self.heap)

    # Display heap state
    def display(self):
        print(self.heap)


# ---------------- MAIN ----------------
if __name__ == "__main__":

    pq = MinHeap()

    # Input priorities (fixed dataset for lab)
    priorities = [40, 10, 30, 50, 20]

    print("Inserting elements:")
    for p in priorities:
        pq.insert(p)
        print(f"Inserted {p}, Heap: {pq.heap}")

    print("\nPeek (Min Element):", pq.peek())

    print("\nExtracting elements (Priority Order):")
    extracted_order = []

    while pq.peek() is not None:
        val = pq.extract_min()
        extracted_order.append(val)
        print(f"Extracted {val}, Heap: {pq.heap}")

    print("\nFinal Extraction Sequence:")
    print(extracted_order)