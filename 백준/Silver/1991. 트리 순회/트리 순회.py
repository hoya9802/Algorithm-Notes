import sys
input = sys.stdin.readline

class node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

def pre_order(node):
    print(node, end="")
    if tree[node].left_node != None:
        pre_order(tree[node].left_node)
    if tree[node].right_node != None:
        pre_order(tree[node].right_node)

def in_order(node):
    if tree[node].left_node != None:
        in_order(tree[node].left_node)
    print(node, end= "")
    if tree[node].right_node != None:
        in_order(tree[node].right_node)

def post_order(node):
    if tree[node].left_node != None:
        post_order(tree[node].left_node)
    if tree[node].right_node != None:
        post_order(tree[node].right_node)
    print(node, end="")
tree = {}
for _ in range(int(input())):
    d, l, r = input().split()
    if l == '.':
        l = None
    if r == '.':
        r = None
    tree[d] = node(d,l,r)

pre_order('A')
print()
in_order('A')
print()
post_order('A')