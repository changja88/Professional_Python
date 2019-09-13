import collections

# Sample 1
Card = collections.namedtuple('Card', ['rank', 'suit'])


# NameTuple
#   - 보통 튜플의 경우에는 인덱스를 통해서 튜플에 접근이 가능한다 namedtuple을 사용하면 키 값으로 접근이 가능하다
#   - dict처럼 작동하지만 tuple의 성질을 가지고 있다
#   - 아주 간단하게 객채를 정의 할 수 있다

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

    # __len__ , __getitem__ 구현 이유
    #   - 이걸 구현해야 list처럼 사용 할 수 있다 -> 슬라이싱, 반복문 등이 작동한다
    #   - 표준 파이썬 시퀀스처럼 작동하게 된다는 뜻
    #   - 구성 덕분에 __len__(), __getitem__() 메서드는 모든 작업을 list 객체는 self._cards에 떠넘길수 있다

    # _ 언더바의 사용 용도
    # 1. 인터프리터에서 사용 되는 경우에는 마지막으로 실행된 결과값이 _ 변수에 저장이 되어있다
    # 2. 값을 무시하고 싶은 경우 x,_,y = (1,2,3) -> x = 1, y =3
    # 3. 특별한 의미의 네이밍을 하는 경우
    #   - 파이썬은 지정한 의미의 private을 지원하고 있지 않기 때문에 완전히 private을 강제 할수는 없지만
    #   - 한 모듈에서만 사용하는 클래스/함수/변수/메서드 선언을 할때 사용하면 import시에 무시된다
    #   - 하지만 직접 _를 사용해서 접근 할수 있기 때문에 'weak internal use indicator' 라고 한다
    # 4. 숫자 리터럴값의 자릿수 구분을 위한 구분자로써 사용 가능
    #   - 1_000_000, 2_000

    # __ 던더의 사용 용도 (__이름__) -> 이거 아님 __이름 이거 말하는
    # 1. 컨벤션이라기보단 하나의 문법적인 요소이다. 던더는 클래스 속석명을 맹글링하여 클래스간 속성명의 충동을 방지 하기 위한 용도
    #   - 맹글링 : 컴파일이나 인터프리터가 변수/함수명을 그대로 사용하지 않고 일정한 규칙에 의해 변형시키는 것

    # __이름__ 의 사용 용도
    # 1. 매직 메서드라고 부른다
    # 2. 특정한 문법적 기능을 제공하거나 특정한 일을 수행한다
    #   - __init__의 경우에는 클래스의 인스턴스가 생성될 때 처음으로 실행되는 메서드이다
    # - 이 메서드는 사용자가 아니라 파이썬 인터프리터가 호출하기 위한 것이다
    #   - 우리는 object.__len__() 이렇게 호출하지 않고 len(object)와 같이 호출 한다
    #   - 위체서 처럼 호출하면 파이썬이 __len__()을 호출한다
    #   - 사용자가 자주 사용하는 경우는 __init__()이다
    # - 사용자 정의 속성을 만들때 __이름__ 형태의 속성명은 피하라 -> 지금 사용 되고 있지 않더라도 나중에 정의 될수 있기 때문


deck = FrenchDeck()
print(deck)

# 슬라이싱이 가능 하다
print(deck[12::13])

# 반복이 가능 하다
for card in reversed(deck):
    print(card)

# 컬렉션에 __contains__ 메서드가 없다면 in 연산자는 차례대로 검색한다
# FrenchDeck 클래스의 경우 반복할 수 있으므로 in 이 작동한다
Card('Q', 'hearts') in deck

# 정렬도 가능하다
suits_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(self):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suits_values) + suits_values[card.suit]


for card in sorted(deck, key=spades_high):
    print(card)
