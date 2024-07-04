class str_:
    def __init__(self, s):
        self.s = str(s)
    
    def __getitem__(self, idx):
        return self.s[idx]
    
    def __setitem__(self, idx, val):
        self.s = list(self.s)
        self.s[idx] = val
        self.s = ''.join(self.s)

    def __str__(self):
        return self.s
    
a = str_('안녕')
a[0] = '원'
print(a)         # 원녕