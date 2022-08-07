
class A:
    def __init__(self, a: int, b: str, c: list, d: int):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __repr__(self):
        return f"Hello this is repr function "
    def __call__(self):
        return f"This is call function."



B = A(a=5, b='fujg', c=[3, 5], d=8)


print(B)
print(B())