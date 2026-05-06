class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# Insert function
def insert(root, key):
    if root is None:
        return Node(key)

    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    return root


# Search function
def search(root, key):
    if root is None:
        return False

    if root.val == key:
        return True
    elif key < root.val:
        return search(root.left, key)
    else:
        return search(root.right, key)


# Inorder traversal (Left -> Root -> Right)
def inorder(root, result):
    if root:
        inorder(root.left, result)
        result.append(root.val)
        inorder(root.right, result)


# ---------------- MAIN ----------------
if __name__ == "__main__":
    # Fixed dataset (you can change if needed)
    keys = [50, 30, 70, 20, 40, 60, 80]

    root = None

    # Insert nodes
    for key in keys:
        root = insert(root, key)

    # Inorder traversal
    result = []
    inorder(root, result)

    print("Inorder Traversal (Sorted Output):")
    print(result)

    # Search keys
    search_keys = [40, 90]

    print("\nSearch Results:")
    for key in search_keys:
        if search(root, key):
            print(key, "Found")
        else:
            print(key, "Not Found")