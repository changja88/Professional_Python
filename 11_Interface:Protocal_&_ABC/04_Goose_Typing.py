"""
알렉스 마르텔리의 물새
"""
from abc import abstractmethod

"""
알렉스 마르텔리의 물새(에세이)
- 덕타이핑은 객체의 실제 자료형은 무시하고, 대신 객체가 용도에 맞는 메서드 이름, 시그니처, 의미를 구현하도록 보장하는데 주안점을 둔다
- 파이썬에서는 결국 자료형 검사를 위한 isinstance() 함수 사용의 회피를 의미한다
- 전반적으로 덕 타이핑 방법이 상당히 유용하게 사용되는 상황이 많지만, 그렇지 않은 상황에서는 다른 방법이 발전했다
"""


class Artist:
    def draw(self): pass


class Gunslinger:
    def draw(self): pass


class Lottery:
    def draw(self): pass


"""
- artist.draw()와 gunslinger.draw()가 관념적으로 대등하다고 결코 보장 할 수 없다
- 즉, 동일한 이름의 메서드를 호출한다고해서 의미가 비슷하다고 생각할 수 없다
"""
"""
- 구스타이핑(goose typing)으로 이를 보완하고자 한다
- 구스타이핑이라는 말은 cls가 ABC인 경우 즉, cls의 메타 클래스가 abc.ABCMeta인 경우에는
  isinstance(obj,cls)를 써도 좋다는 것을 의미한다
- 구상 클래스에 비해 ABC가 가진 여러 개념적 장점중 아주 큰 도움이 되는 register()라는 클래스가 있다
- 이 메서드는 어떤 클래스가 ABC의 '가상'서브클래스임을 '선언'할수 있게 해준다
    - 이렇게 선언하려면 등록할 클래스가 ABC의 메서드 이름 및 시그니처 요구사항을 만족해야 하며,
      특히 메서드의 의미를 지켜야 한다
"""


class Struggle:
    def __len__(self): return 23


import collections
from collections import abc

print(isinstance(Struggle(), abc.Sized))
"""
- 클래스를 ABC의 서브클래스로 인식시키기 위해 등록할 필요가 없는 경우도 있다
- 여기에서 볼 수 있는 것처럼 abc.Sized 클래스는 Struggle을 '일종의 서브클래스'로 인식한다
- 단지 __len__이라는 특별 메서드만 구현하면 되며, 등록할 필요도 없다
"""
"""
- 결론
- 여러분이 사용할 다른 프레임워크에 있는 ABC가 표현하는 개념을 실현하는 클래스를 구현할 때는 언제나 해당 ABC를 상속하거나
  해당 ABC에 등록하라
- 이 과정을 빠뜨리고 클래스를 정의한 라이브러리나 프레임워크를 사용하는 프로그램에서는 언제나 코드 시작 부분에서 여러분이
  클래스를 직접 등록하길 바란다. 
- 그리고 나서 예를 들어 인수가 '시퀀스'인지 검사해야 할 때는 다음과 같이 한다
"""
isinstance(Struggle, collections.abc.Sequence)

"""
GooseTyping 응용
ABC 상속하기
"""

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck2(collections.MutableSequence):
    ranks = [str(n) for n in range(2, 11)] + list("JKQA")
    suits = 'spades diamonds clubs heart'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    # 카드를 섞기 위해서 필요하다
    def __setitem__(self, position, value):
        self._cards[position] = value

    # MutableSequence를 상속 했으므로 구현해야 한다
    def __delitem__(self, position):
        del self._cards[position]

    # MutableSequence를 상속했으므로 구현해야 한다
    def insert(self, position, value):
        self._cards.insert(position, value)


"""
파이썬은 모듈을 로딩하거나 컴파일할 때가 아니라, 실행 도중 실제로 FrenchDeck2 객체를 생성할 때 추상 메서드의 구현 여부를 확인한
"""

"""
구상클래스 register 사용 예시
- 구스 타이핑의 본질적인 기능은 어떤 클래스가 ABC를 상속하지 않더라도 그 클래스의 '가상 서브클래스'로 등록 할수 있다는 것이다
- ABC의 register()를 호출하면 클래스가 등록된다
- 등록된 클래스는 ABC의 가상 서브클래스가되어 issubclass()와 isinstace()함수에 인식되지만
  ABC에서 상속한 메서드나 속성은 전혀 없다 
"""
import abc


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
        최소 한 개의 항목이 있으면 True를, 아니면 False를 반환한다
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


from random import randrange


@Tombola.register  # 가상 서브클래스로 등록한다
class TomboList(list):

    def pick(self):
        if self:
            position = randrange(len(self))
            return self.pop(position)
        else:
            raise LookupError('pop from empty TomboList')

    load = list.extend

    def loaded(self):
        return bool(self)

    def insect(self):
        return tuple(sorted(self))


Tombola.register(TomboList)  # @Tombola.register 둘중에 하나만 해주면 된
