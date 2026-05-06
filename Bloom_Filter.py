class BloomFilter:
    def __init__(self, size):
        self.size = size
        self.bit_array = [0] * size

    # Simple hash functions (toy version)
    def hash1(self, item):
        return hash(item) % self.size

    def hash2(self, item):
        return (hash(item) * 3) % self.size

    def hash3(self, item):
        return (hash(item) * 7) % self.size

    # Insert item
    def add(self, item):
        indexes = [self.hash1(item), self.hash2(item), self.hash3(item)]

        for i in indexes:
            self.bit_array[i] = 1

        print(f"Inserted: {item} -> bits {indexes}")

    # Check membership
    def check(self, item):
        indexes = [self.hash1(item), self.hash2(item), self.hash3(item)]

        for i in indexes:
            if self.bit_array[i] == 0:
                return "Definitely NOT present"

        return "Possibly present (may be false positive)"


# ---------------- MAIN ----------------
if __name__ == "__main__":

    bf = BloomFilter(10)

    # Insert items
    items = ["apple", "banana", "grape"]

    print("Inserting items:")
    for item in items:
        bf.add(item)

    print("\nBit Array:", bf.bit_array)

    # Queries
    print("\nQuery Results:")
    print("apple ->", bf.check("apple"))      # should be present
    print("banana ->", bf.check("banana"))    # should be present
    print("mango ->", bf.check("mango"))      # not inserted (may be false positive)