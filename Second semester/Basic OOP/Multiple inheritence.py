class A:
    def __init__(self):
        self.xyz = 123


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


d = D()
print(d.xyz)