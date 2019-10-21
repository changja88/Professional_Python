"""
표준 라이브러리의 ABC
"""

"""
- 대부분의 ABC는 collections.abc 모듈에 정의되어 있으며, 이 모듈에 정의된 ABC들이 가장 많이 사용된다
"""
import abc
import random


class Tombola(abc.ABC):
    @abc.abstractmethod
    def load(self, iterable):
        """iterable의 항목들을 추가한다"""

    @abc.abstractmethod
    def pick(self):
        """
        무작위로 항목을 하나 제거하고 반환한다.
        객체가 비어 있을 때 이 메서드를 실행하면 'LookupError'가 발생한다
        """

    def loaded(self):
        """
        최소 한 개의 항목이 있으면 True를, 아니면 False를 반환한ㄷ
        """
        return bool(self.inspect())

    def inspect(self):
        """현재 안에 있는 항목들로 구성된 정렬된 튜플을 반환한다"""
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break

        self.load(items)
        return tuple(sorted(items))


"""
- 추상 메서드도 실제 구현 코드를 가질 수 있다.
  추상 메서드가 실제 구현 코드를 담고 있더라도 서브클래스는 이 메서드를 오버라이드해야 한다
  하지만 서브클래스에서는 처음부터 모든 기능을 구현하는 대신 super()를 이용해서 추상 메서드가 구현한 기능을 재사용할 수 있다
"""

"""
ABC 상세 구문
- ABC를 선언할 때는 abc.ABC나 다른 ABC를 상속하는 방법이 가장 좋다
- @abstractmethod 외에도 @abstractclassmethod, @abastractstaticmethod @abstractproperty 데커레이터를 정의한다
- 하지만 사라졌다 -> 이유는 데커레이터를 쌓을수 있게 되었기 때문
- @abstractclassmethod -> @abstractmethod @classmethod 두개를 쌓아 올리면 된다
- 보통 데커레이터 순서는 중요하지 않지만 @abstractmethod의 경우는 반듯이 맨 아래 와야 한다
"""


class BingoCage(Tombola):
    def __init__(self, items):
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)

    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        self.pick()
