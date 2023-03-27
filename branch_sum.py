class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    if root is None:
        return []
    
    branch_left = branchSums(root.left)
    branch_right = branchSums(root.right)
    branch = branch_left + branch_right

    if branch:
        return [x + root.value for x in branch]
    else:
        return [root.value]


#Below is a binary tree we created to check the sample output
root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)
root.right.left = BinaryTree(6)
root.right.right = BinaryTree(7)

output = branchSums(root)
print(output)