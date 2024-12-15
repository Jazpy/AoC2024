from functools import singledispatchmethod


class Vec2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self, o):
        return abs(self.x - o.x) + abs(self.y - o.y)

    def colinear(self, o0, o1):
        return (self.y - o0.y) * (self.x - o1.x) == (self.y - o1.y) * (self.x - o0.x)

    def __add__(self, o):
        return Vec2(self.x + o.x, self.y + o.y)

    def __sub__(self, o):
        return Vec2(self.x - o.x, self.y - o.y)

    @singledispatchmethod
    def __mul__(self, o):
        raise NotImplementedError(o)

    @__mul__.register
    def __mul_int__(self, s : int):
        return Vec2(self.x * s, self.y * s)

    def __mod__(self, o):
        return Vec2(self.x % o.x, self.y % o.y)

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, o):
        return self.x == o.x and self.y == o.y

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def vsmart_get(mat, v, modulo=False):
        return Vec2.smart_get(mat, v.x, v.y, modulo)

    def smart_get(mat, x, y, modulo=False):
        if modulo:
            x %= len(mat[0])
            y %= len(mat)
        if x < 0 or x >= len(mat[0]) or y < 0 or y >= len(mat):
            return None
        return mat[y][x]

@Vec2.__mul__.register
def __vec2_mul__(self, o : Vec2):
    return Vec2(self.x * o.x, self.y * o.y)
