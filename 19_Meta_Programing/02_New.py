"""
__new__를 이용한 융통성 있는 객체 생성
"""
"""
- __init__메서드를 생성자 메서드라고 부르지만, 생성자라는 말은 다른 언어에서 빌려온 용어일 뿐이다
- 실제로 객체를 생성하는 특별 메서드는 __new__이다
  이 메서드는 클래스 메서드로서(특별 대우를 받기때문에 @classmethod데커레이터를 사용하지 않는다)반드시 객체를 반환한다
  그리고 나서 그 객체가 __init__메서드의 첫 번째 인수 self로 전달된다
- __init__은 호출될 때 객체를 받으며 아무 것도 반환할 수 없으므로, 실제로 __init__은 '초기화 메서드'일 뿐이다
- 실제 생성자인 __new__메서드는 object클랫에서 상속받은 메서드로도 충분하므로 직접 구현할 일은 거의 없다 
"""

from collections import abc
from keyword import iskeyword


class FrozenJSON:
    def __new__(cls, arg):
        if isinstance(arg, abc.Mapping):
            return super().__new__(cls)
        elif isinstance(arg, abc.MutableSequence):
            return [cls(item) for item in arg]
        else:
            return arg
