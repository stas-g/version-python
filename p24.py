class Number:
    def __init__(self, x):
        self.value = x
    def __repr__(self):
        return "%s" % self.value

class Complex:
    def __init__(self, a, b):
        self.real = a
        self.imag = b
    def __repr__(self):
        return "%s + %si" % (self.real, self.imag)

class Add:
    def __init__(self, l, r):
        self.left = l
        self.right = r
    def __repr__(self):
        return "%s + %s" % (self.left, self.right)

class Multiply:
    def __init__(self, l, r):
        self.left = l
        self.right = r
    def __repr__(self):
        return  "%s * %s" % (self.left, self.right)


#Add(Multiply(Number(1), Number(2)), Multiply(Number(3), Number(4)))

def reducible(expr):
    if expr.__class__ == Number or expr.__class__ == Complex:
        return False
    else:
        return True
    
#reducible(Number(10))
#reducbile(Add(45, 12))
