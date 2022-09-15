# universal value tree.


#    0
#  /   \
# 1     0

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


tree = Node(0, Node(1), Node(0))


def is_unival(root):
    if root is None:
        return True
    if root.left is not None and root.left.value != root.value:
        return False
    if root.right is not None and root.right.value != root.value:
        return False
    if is_unival(root.left) and is_unival(root.right):
        return True
    return False

print(is_unival(tree))