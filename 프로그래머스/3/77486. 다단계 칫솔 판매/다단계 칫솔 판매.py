class Node:
    def __init__(self, parent):
        self.value = 0
        self.parent = parent
        
    def divider(self, earn_money):
        tmp = int(earn_money * 0.1)
        if tmp > 0 and self.parent != None:
            self.parent.divider(tmp)
        self.value += (earn_money - tmp)

def solution(enroll, referral, seller, amount):
    tree = {}
    n = len(enroll)
    for i in range(n):
        if referral[i] == '-':
            tree[enroll[i]] = Node(None)
        else:
            tree[enroll[i]] = Node(tree[referral[i]])
    
    for i in range(len(seller)):
        earn_money = amount[i] * 100
        tree[seller[i]].divider(earn_money)
    
    return [tree[x].value for x in enroll]