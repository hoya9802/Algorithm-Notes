class Node:
    def __init__(self, parent):
        self.total = 0
        self.parent = parent
        
    def divider(self, money):
        div = int(money * .1)
        self.total += (money - div)
        if div > 0 and self.parent:
            self.parent.divider(div)

def solution(enroll, referral, seller, amount):
    N = len(enroll)
    rel_dict = {'-':None}
    ans = []
    
    for i in range(N):
        person = enroll[i]; parent = referral[i]
        if parent == '-':
            node = Node(rel_dict['-'])
        else:    
            node = Node(rel_dict[parent])
        rel_dict.update({person: node})

    for i in range(len(seller)):
        cost = amount[i] * 100
        rel_dict[seller[i]].divider(cost)
    
    return [rel_dict[enroll[i]].total for i in range(N)]