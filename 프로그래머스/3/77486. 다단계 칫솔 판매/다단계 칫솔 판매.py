class Node:
    def __init__(self, parent):
        self.total = 0
        self.parent = parent

    def divide(self, earn_money):
        tmp = int(earn_money * 0.1)
        if tmp > 0 and self.parent != None:
            self.parent.divide(tmp)
        self.total += (earn_money-tmp)
        

def solution(enroll, referral, seller, amount):
    
    tree = {}
    tree['-'] = None
    
    for e, r in zip(enroll, referral):
        if r == "-":
            tree[e] = Node(tree['-'])
            continue
        tree[e] = Node(tree[r])
    
    for s, a in zip(seller, amount):
        earn_money = a * 100
        tree[s].divide(earn_money)
    
    return [tree[x].total for x in enroll]
    