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


# Find minimum value node (used for inorder successor)
def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


# Delete function (handles all 3 cases)
def delete_node(root, key):
    if root is None:
        return root

    # Search node
    if key < root.val:
        root.left = delete_node(root.left, key)
    elif key > root.val:
        root.right = delete_node(root.right, key)
    else:
        # Case 1: Leaf node (no child)
        if root.left is None and root.right is None:
            return None

        # Case 2: One child
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        # Case 3: Two children
        successor = find_min(root.right)
        root.val = successor.val
        root.right = delete_node(root.right, successor.val)

    return root


# Inorder traversal
def inorder(root, result):
    if root:
        inorder(root.left, result)
        result.append(root.val)
        inorder(root.right, result)


# ---------------- MAIN ----------------
if __name__ == "__main__":

    # Fixed dataset
    keys = [50, 30, 70, 20, 40, 60, 80]

    root = None

    # Insert nodes
    for key in keys:
        root = insert(root, key)

    print("Initial BST (Inorder):")
    result = []
    inorder(root, result)
    print(result)

    # Deletions
    delete_keys = [20, 30, 50]   # test leaf, one child, two children

    for key in delete_keys:
        print(f"\nDeleting {key}...")
        root = delete_node(root, key)

        result = []
        inorder(root, result)

        print("Inorder after deletion:")
        print(result)