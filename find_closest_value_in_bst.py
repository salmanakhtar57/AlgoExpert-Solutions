#Write a function that takes BST
#And Target integer value
#It should return the closest value to that target value in the BST.

def findClosestValueInBst(tree, target):
    closest_value = tree.value
    current_node = tree

    while current_node is not None:
        if abs(current_node.value - target) < abs(closest_value-target):
            closest_value = current_node.value
        if target < current_node.value:
            current_node = current_node.left
        elif target > current_node.value:
            current_node = current_node.right
        else:
            break
    return closest_value

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#To return the sample result we need to create a binary tree
tree = BST(10)
tree.left = BST(5)
tree.right = BST(15)
tree.left.left = BST(2)
tree.left.right = BST(5)
tree.right.left = BST(13)
tree.right.right = BST(22)
tree.left.left.left = BST(1)
tree.right.left.right = BST(14)

closest_value = findClosestValueInBst(tree, 12)
print(closest_value) #output: 13
closest_value = findClosestValueInBst(tree, 13)
print(closest_value) #output: 13

