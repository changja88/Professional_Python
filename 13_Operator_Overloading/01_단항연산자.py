import itertools
import math
import numbers

"""
연산자 오버로딩 : 제대로 하기
"""
"""
연산자 오버로딩 기본 지식
- 연산자 오버로딩은 부작용이 많기 때문에 제한을 두어 융통성, 사용성, 안전성을 적절히 유지한다
    - 내장 자료형에 대한 연산자 오버로딩은할 수 없다
    - 새로운 연산자를 생성할 수 없으며, 기존 연산자를 오버로딩만 할 수 있다
    - is, and, or, not 연산자는 오버로딩할 수 없다(그러나 &, |, ~ 비트 연산자는 가능하다)
"""
"""
단항 연산자
- '-' (__neg__) -> 빼기가 이니라 - 부호 붙이는 것
- '+' (__pos__) -> 더하기가 이날 + 부호 붙이는 
- '~' (__invert__)
    - 정수형의 비트 반전
- 단항 연산자는 구현하기 쉽다. 단지 self인수 하나를 받는 적절한 특별 메서드를 구현하면 된다
  특히, '언제나 새로운 객체를 반환해야 한다'라는 연산자의 핵심 규칙을 지켜야 한다
  즉, self를 수정하지 말고 적절한 자료형의 객체를 새로 생성해서 반환해야 한다
"""


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __bool__(self):
        return bool(abs(self))

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __neg__(self):
        """
        객체앞에 - 기호를 붙일 수 있게 해준다
        self나 other의 값을 변경하지 않고 새로운 객체를 리턴한다
        """
        return Vector(-x for x in self)

    def __pos__(self):
        """
        객체앞에 + 기호를 붙일 수 있게 해준다
        self나 other의 값을 변경하지 않고 새로운 객체를 리턴한다
        """
        return Vector(self)

    def __add__(self, other):
        """
        Vector객체간 + 를 가능하게 해준다
        self나 other의 값을 변경하지 않고 새로운 객체를 리턴한다
        """
        pairs = itertools.zip_longest(self, other, fillvalue=0)
        return Vector(a + b for a, b in pairs)

    def __radd__(self, other):
        """
        역순 또는 오른쪽
        오른쪽 피연산자의 메서드를 호출한
        """
        return self + other

    def __mul__(self, scalar):
        if isinstance(scalar, numbers.Real):
            return Vector(n * scalar for n in self)
        else:
            return NotImplemented

    def __rmul__(self, scalar):
        return self * scalar


"""
파이썬의 '더하기' 연산 절차
- 1. __add()__ 정의를 확인한다 -> NotImplemented가 아니면 반환
- 2. __radd()__ 정의를 확인한다 -> NotImplemented가 아니면 반환 (radd 는 add의 역순)
- 3. 둘다 없으면 TypeError를 반환다
"""
Vector(1, 2) + (1, 2)
