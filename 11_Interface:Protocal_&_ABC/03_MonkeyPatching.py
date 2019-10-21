"""
런타임에 프로토콜을 구현하는 멍키 패칭
"""
from random import shuffle
import collections

l = list(range(10))
shuffle(l)
print(l)

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs heart'.split()

    def __init__(self):
        # 반복문으로 List 구성 하는 방법
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


deck = FrenchDeck()
# shuffle(deck)
"""
- 위에꺼는 되는데 FrenchDeck은 에러가 발생한다
- 에러 메세지에 객체 할당을 지원하지 않기 때문이라고 나온다 -> __setitem__메소드를 지원 해줘야 한다는 뜻
- 동적으로 FrenchDeck에 __setitem__을 추가해주자 -> Monkey Patching
- '멍키 패칭' 이란 소스코드를 건드리지 않고 런타임에 클래스나 모듈을 변경하는 행위를 말한다
"""


def set_card(deck, position, card):
    deck._cards[position] = card


FrenchDeck.__setitem__ = set_card
shuffle(deck)
print(deck[:5])
"""
- 프로토콜이 동적이라는 것을 보여주는 사례이기도 하다
- random.shuffle() 함수는 자신이 받는 인수의 자료형에 대해서는 신경쓰지 않는다 
  단지 받은 객체가 일부 가변 시퀀스 프로토콜을 구현하고 있드면 될 뿐이다
  심지어 객체가 필요한 메서드를 '원래부터'가지고 있었는지, 아니만 나중에 얻었는지는 전혀 문제가 되지 않는다
"""
