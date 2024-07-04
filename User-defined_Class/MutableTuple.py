class MutableTuple:
    def __init__(self, *t):
        self.tp = t

    def change(self, idx, val):
        self.tp = list(self.tp)
        self.tp[idx] = val
        self.tp = tuple(self.tp)
    
    def __str__(self):
        return str(self.tp)
    
    def __getitem__(self, idx):
        return self.tp[idx]
    
    def __setitem__(self, idx, val):
        try:
            self.tp[idx] = val
        except:
            print('Try to use change() function instead')

c = MutableTuple(1,2,3)
print(c)
c.change(1,100)
print(c[1])
c[1] = 1
print(c)