"""
포맷된 출력
- format() 내장 함수와 str.format()메서드는 실제 포맷 작업을 __format__(format_spec)메서드에 위임하다
  format_spec은 포맷 명시자로서, 다음 두가지 방법중 하나를 통해 지정한다
    - format(my_obj, format_spec)의 두번째 인수
    - str.format()에 사용된 포맷 문자열 안에 {}로 구분한 대체 필드 안에서 콜론 뒤의 문자열
"""
"""
- 포맷 명시자를 -> 포맷 명시 간이 언어(Format Specification Mini-Language)라고 한다
- 몇몇 내장 자료형은 포맷 명시 간이 언어에 자신만의 고유한 표현 코드를 가지고 있다
    - int -> b: 2진수, x: 16진수
    - float -> f: 고정소수, % : 백분율
"""
brl = 1 / 2.43
print(format(brl, '0.4f'))  # -> 0.4f가 포맷 명시자이다
print('1 BRL = {rate:0.2f} USD'.format(rate=brl))  # -> 0.2f가 포맷 명시자다

"""
- 각 클래스가 format_spec 인수를 자신이 원하는 대로 해석해서 포맷 명시 간이 언어를 확장 할 수 있다
"""
from datetime import datetime

now = datetime.now()
print(format(now, '%H:%M:%S'))
print("It's now {:%I:%M %P}".format(now))

"""
- 클래스에서 __format__메서드를 정의하지 않으면, object에서 상속받은 메서드가 str(my_object)를 반환한다
"""


class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __str__(self):
        return str(tuple(self))

    def __format__(self, format_spec=''):
        components = (format(c, format_spec) for c in self)
        return '({}, {})'.format(*components)


v1 = Vector2d(3, 4)
print(format(v1))
format(v1,'.3f') # -> _format__은 정의하지 않으면 이건 에러가 발생한다
