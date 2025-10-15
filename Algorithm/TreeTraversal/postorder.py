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

def post_order(node):
    if node.left != None:
        post_order(tree[node.left])
    if node.right != None:
        post_order(tree[node.right])
    print(node.data, end=" ")

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

post_order(tree['A'])   # output: D E B F G C A