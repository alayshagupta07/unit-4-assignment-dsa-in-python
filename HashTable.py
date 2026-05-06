class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    # Hash function
    def hash_function(self, key):
        return key % self.size

    # Insert key-value pair
    def insert(self, key, value):
        index = self.hash_function(key)

        # Check if key already exists → update
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return

        # Otherwise add new pair (collision handled here)
        self.table[index].append([key, value])

    # Get value by key
    def get(self, key):
        index = self.hash_function(key)

        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]

        return None

    # Delete key-value pair
    def delete(self, key):
        index = self.hash_function(key)

        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return True

        return False

    # Display hash table
    def display(self):
        print("\nHash Table (Buckets):")
        for i in range(self.size):
            print(i, "->", self.table[i])


# ---------------- MAIN ----------------
if __name__ == "__main__":

    ht = HashTable(5)

    # Key-value pairs (chosen to create collisions)
    data = [
        (1, "A"),
        (6, "B"),
        (11, "C"),   # collision with 1 (1%5 = 6%5 = 11%5)
        (2, "D"),
        (7, "E"),
        (12, "F")
    ]

    print("Inserting elements:")
    for k, v in data:
        print(f"Insert ({k}, {v})")
        ht.insert(k, v)

    ht.display()

    # Get operations
    print("\nGet Operations:")
    print("Key 6 ->", ht.get(6))
    print("Key 11 ->", ht.get(11))
    print("Key 99 ->", ht.get(99))  # not present

    # Delete operations
    print("\nDelete Operations:")
    print("Delete Key 6:", ht.delete(6))
    print("Delete Key 99:", ht.delete(99))  # not present

    ht.display()