#Write a function that takes in a binary tree
#Return the sum of its node's depth

def nodeDepths(root, depth=0):
    return 0 if root is None else depth + nodeDepths(root.left, depth+1) + nodeDepths(root.right, depth+1)

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#create a binary tree to check the sample output
tree = BinaryTree(1)
tree.left = BinaryTree(2)
tree.left.left = BinaryTree(4)
tree.left.right = BinaryTree(5)
tree.left.left.left = BinaryTree(8)
tree.left.left.right = BinaryTree(9)
tree.right = BinaryTree(3)
tree.right.left = BinaryTree(6)
tree.right.right = BinaryTree(7)

print(nodeDepths(tree))  # Output: 16