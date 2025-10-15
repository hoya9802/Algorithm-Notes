"""
7
A B C
B D E
C F G
D None None
E None None
F None None
G None None
"""

def pre_order(node):
    print(node.data, end=" ")
    if node.left != None:
        pre_order(tree[node.left])
    if node.right != None:
        pre_order(tree[node.right])

class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

n = int(input())
tree = {}

for _ in range(n):
    a, b, c = input().split()
    if b == "None":
        b = None
    if c == "None":
        c = None
    tree[a] = Node(a, b, c)

pre_order(tree['A'])    # output: A B D E C F G