class Node:
    def __init__(self, value, child=None):
        self.value = value
        self.child = child

    def __str__(self):
        return str(self.value)

current = Node(1)
for i in range(2, 8):
    current = Node(i, current)


def LinkedToString(head):
    current = head
    lst = []
    while current:
        lst.append(str(current.value))
        current = current.child
    lst.append('(None)')
    return "->".join(lst)

print(LinkedToString(current))