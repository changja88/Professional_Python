# 파이썬스러운 객체

# - 파이썬 데이터 모델 덕분에 사용자가 정의한 자료형도 내장 자료형과 마찬가지로 자연스럽게 동작 할 수 있다.
#   상속하지 않고도 덕 타이핑 메커니즘을 통해 이 모든 것이 가능하다
#   단지 객체에 필요한 메서드를 구현하면 기대한 대로 동작한다

# 객체 표현
# - repr : 객체를 개발자가 보고자 하는 형태로 표현한 문자열을 반환한다
# - str : 객체를 사용자가 보고자하는 형태로 표현한 문자열을 반환한다
# __repr__, __str__을 구현 해줘야 한다


# 벡터 클래스의 부활
import math
from array import array


class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r},{!r})'.format(class_name, *self)  # *self 는 format()에 x,y 속성을 제공한다

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:].cast(typecode))
        return cls(*memv)
    # 클래스 메서드
    # - self 매개변수가 없다. 대신 클래스 자신이 cls 매개변수로 전달된다


v1 = Vector2d(3, 4)
print(v1.x, v1.y)

x, y = v1  # 언팩킹이 가능하다 __iter__를 구현했기 때문
print(x, y)

print(v1)

v1_clone = eval(repr(v1))
print(v1 == v1_clone)  # 그 어떤 반복형 객체도 동일한 숫자값을 가졌다면 True를 반환한다(기능 일수도 버그 일수도)

octets = bytes(v1)
print(octets)

print(abs(v1))

print(bool(v1))
print(bool(Vector2d(0, 0)))
