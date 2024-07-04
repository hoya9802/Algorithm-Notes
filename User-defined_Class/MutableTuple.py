class MutableTuple:
    def __init__(self, *t):
        self.tp = t
    
    def __str__(self):
        return str(self.tp)
    
    def __getitem__(self, idx):
        return self.tp[idx]
    
    def __setitem__(self, idx, val):
        self.tp = list(self.tp)
        self.tp[idx] = val
        self.tp = tuple(self.tp)

    def __len__(self):
        return len(self.tp)
    
    def count(self, value):
        return self.tp.count(value)

c = MutableTuple(1,2,3)

print(c)            # (1, 2, 3)
print(c[1])         # 2
c[1] = 100          # Try to use change() function instead
print(c)            # (1, 100, 3)
print(len(c))       # 3
print(c.count(3))   # 1