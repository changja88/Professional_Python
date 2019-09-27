from math import hypot


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


# __repr__
#   - 이걸 구현하지 않으면 콘솔에 <Vector object at 0x10e100070>과 같은 형태로 출력이 된다
#   - 반환하는 문자열은 명확해야 하며, 가능하면 표현된 객체를 재생성하는 데 필요한 소스코드와 일치해야 한다
#   - __str__ 과 __repr__ 중에 하나를 구현해야 한다면 __repr__을 구현하는 것이 좋다
#     __str__이 구현 되어 있지 않으면 __repr__이 호출 되기 때문

# __add__, __mul__
#   - + 연산자와 * 연산자를 구현 한다
#   - 중위 연산자는 의례적으로 피연산자를 변경하지 않고 객체를 새로 만든다

# __bool__
#   - 사용자 정의형의 불리언 값
#   - if나 while문에 등에 대한 피연산자로서 불리언형이 필요한 곳에서 사용할수 있게 해준다
#   - 구현을 해주지 않으면 파이썬은 기본적으로 사용자 정의 클래스의 객체는 True라고 간주한다
#   - 구현되어 있지 않으면 __len__()을 호출하며 이 메서드가 0을 반환하면 False 그렇지 않으면 True를 반환한다


a = Vector(3, 4)
print(a)

v1 = Vector(2, 4)
v2 = Vector(2, 1)
v1 + v2

v = Vector(3, 4, )
abs(v)

v * 3
