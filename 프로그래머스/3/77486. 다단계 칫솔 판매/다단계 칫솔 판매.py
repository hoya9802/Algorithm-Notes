class Node:
    def __init__(self, parent):
        self.money = 0
        self.parent = parent
        
    def divider(self, earn_money):
        tmp = int(earn_money * .1)
        if tmp > 0 and self.parent != None:
            self.parent.divider(tmp)
        self.money += (earn_money-tmp)

def solution(enroll, referral, seller, amount):
    node_table = {}
    
    for en, re in zip(enroll, referral):
        if re == "-":
            node_table[en] = Node(None)
            continue
        node_table[en] = Node(node_table[re])
    
    for se, am in zip(seller, amount):
        earn_money = am * 100
        node_table[se].divider(earn_money)
    
    return [node_table[en].money for en in enroll]