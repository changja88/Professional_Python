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

# 포맷된 출력
# - format() 내장 함수와 str.format() 메서드는 실제 포맷 작업을 __format__ 메서드에 위임한다
# - format_spec은 포맷 명시자(format specifier)로서, 다음 두 가지 방법중 하나를 통해 지정한다
#   - format(my_obj, format_spec) 의 두번째 인수
#   - str.format()에 사용된 포맷 문자열 안에 {}로 구분한 대체 필드 안에서 콜론 뒤의 문자열
brl = 1 / 2.43
print(brl)
print(format(brl, '0.4f'))

print('1 BRL = {rate:0.2f} USD'.format(rate=brl))
# - 0.2f가 포맷 명시자다. 대체 필드 안에 있는 rate 문자열을 필드명이라고 한다. 이 문자열은 포맷 명시자와 상관 없지만
#   format() 인수중 어느 인수가 대체 필드에 들어갈 것인지 결정한다
# - 이 0.2f와 같은 포맷 명시자에 사용된 표기법을 '포맷 명시 간이 언어(Format Specification Mini-Language)라고 한다
# - 몇몇 내장 자료형은 포맷 명시 간이 언어에 자신만의 고유한 표현 코드를 가지고 있다
#   - int형의 경우 이진수를 나타내는 'b', 16진수를 나타내년 'x'코드를 지원 하고
#   - float 형의 경우 고정소수점을 나타내는 'f', 백분율을 나타내는 '%'코드를 지원한다
print(format(42, 'b'))
print(format(2 / 4, '.1%'))

# - 각 클래스가 format_spec인수를 자신이 원하는 대로 해석해서 포맷 명시 간이 언어를 확장 할 수 있다
#   - 예를 들어 datetime모듈의 클래스들은 자신의 __format__메서드에서 strtime()함수와 동일한 포맷 코드를 사용한다
from datetime import datetime

now = datetime.now()
print(format(now, '%H:%M:%S'))
print("It's now {:%I:%M %P}".format(now))

# - 클래스에서 __format__ 메서드를 정의하지 않으면, object에서 상속받은 메서드가 str(my_object)를 반환한다
# - Vector2d 는 __str__을 정의하고 있으므로 아래와 같이 실행 된다
v1 = Vector2d(3, 4)
print(format(v1))


# - 그러나 이때 포맷 명시자를 사용하면 TypeError를 발생한다
# format(v1, '.3f')
# - Vector2d 에 아래를 추가 하면 해결되고 __str__이 불리지 않기 때문에 출력이 달라진다
# def __format__(self, format_spec):
#     return "abc"


# 해시 가능한 Vector2d
# - 지끔까지 정의한 Vector2d는 해시 할 수 없다. 그러므로 집합 안의 항목으로 사용할 수 없다
# set = {Vector2d(1, 2), Vector2d(4, 4)} -> unHashable type Error
# - 집합안의 항목으로 사용 하기 위해서는 __eq__, __hash__를 구현 해야 한다
# - 해시 가능하다는 말의 의미는 -> 객체를 불변형으로 만들어야 한다

# 객체를 불변형으로 만들기
class Vector2d2:
    typecode = 'd'

    def __init__(self, x, y):
        self.__x = float(x)  # 언더바 두개로 시작하는 속성은 비공개로 만든다
        self.__y = float(y)

    @property  # 프로퍼티의 getter메서드를 나타낸다
    def x(self):  # 자신이 노출시키는 공개 속성명을 따라 getter메서드의 이름을 지정한다
        return self.__x

    @property
    def y(self):
        return self.__x

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)
    # __hash__
    #   - int형을 반환해야 한다
    #   - 동일하다고 판단되는 객체는 동일한 해시값을 가져야 하므로 __eq__메서드가 사용하는 개체의 속성을 이용해서
    #     해시를 계산하는 것이 이상적이다
    #   - 문서에서는 요소의 해시에 비트 타위 XOR연산자(^)를 사용하는 것을 권한장다


# 이제 집합 안의 항목으로 사용 할 수 있다
v1 = Vector2d2(1, 2)
v2 = Vector2d2(3, 4)
set([v1, v2])
