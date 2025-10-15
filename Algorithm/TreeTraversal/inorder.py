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

def in_order(node):
    if node.left != None:
        in_order(tree[node.left])
    print(node.data, end=" ")
    if node.right != None:
        in_order(tree[node.right])

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

in_order(tree['A']) # output : D B E A F C G