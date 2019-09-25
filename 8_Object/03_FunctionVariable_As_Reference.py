# 참조로서의 함수 매개변수
# - 파이썬은 '공유로 호출(CALL BY SHARING)하는 매겨 변수 전달 방식만 지원한다.
# - 이 방식은 루비, 스몰토크, 자바(참조 자료형일 때만 동일, 기본 자료형으 '값으로 호출(CALL BY VALUE)'방식 호출)
#   과 동일하다
# - 대부분의 객체지향 언어에서 사용하는 방식과 동일하다
# - 공유로 호출한다는 말은 함수의 각 매개변수가 인수로 전달받은 각 참조의 사본을 받는다는 의미다
# - 달리말하면, 함수 안의 매개변수는 실제 인수의 별명이 된다

# - 결과적으로, 함수는 인수로 전달받은 모든 가변 객체를 변경 할 수 있디만, 객체의 정체성 자체는 변경할 수 없다.
# - 즉, 어떤 객체를 다른 객체로 바꿀 수는 없다


def f(a, b):
    a += b
    return a


X = 1
Y = 2
print(f(X, Y))
print(X, Y)  # 숫자 X는 변경되지 않는다

A = [1, 2]
B = [3, 4]
print(f(A, B))
print(A, B)  # 리스트 A는 변경된다

T = (10, 20)
U = (30, 40)
print(f(T, U))
print(T, U)  # 튜플 A는 변경되지 않는다

# 가변형을 매개변수 기본값으로 사용하기 : 좋지 않은 생각
print()


class HauntedBus:
    def __init__(self, passengers=[]):
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


bus1 = HauntedBus(['Alice', 'Bill'])
print(bus1.passengers)
bus1.pick('Charie')
print(bus1.passengers)

bus2 = HauntedBus()
bus2.pick('Carrie')
print(bus2.passengers)

bus3 = HauntedBus()
print(bus3.passengers)  # 미친 기본값이 더이상 빈 리스트가 아니다

bus3.pick('Dave')
print(bus2.passengers)  # 미친 bus3에 집어넣은 Dave가 bus2에 나온다

print(bus2.passengers is bus3.passengers)


# -> 문제는 bus2.passengers와 bus3.passensgers가 동일한 리스트를 참조한다는 것이다
# -> 그러나 bus1.passengers는 별개의 리스트이다
# 원인 : self.passengers가 passengers 매개변수 기본값이 별명이 되기 때문이다
class Bus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []  # 새로 만든다
        else:
            self.passengers = list(passengers)


# - 이렇게 해야 한다


# 가변 매개변수에 대한 방어적 프로그래밍
# - 가변 매개변수를 받는 함수를 구현할 때는, 전달된 인수가 변경될 것이라는 것을 호출자가 예상할 수 있는 없는지 고려해야 한다
# - 받은 인수를 변경하는 위험성을 보여주는 클래스 예제
class TwilightBus:
    """승객이 사라지게 만드는 버스 모델"""

    def __init__(self, passensgers=None):
        if passensgers is None:
            self.passengers = []
        else:
            self.passengers = passensgers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


print()
basketball_team = ['Sue', 'Tina', 'Maya', 'Diana', 'Pat']
bus = TwilightBus(basketball_team)
bus.drop('Tina')
bus.drop('Pat')
print(basketball_team)  # 농구팀 선수가 사라졌다


# 원인 : self.passenger는 passengers에 대한 별명이 되기때문

# 아래 처럼 고쳐야 농구팀 선수가 사라지지 않는다
class TwilightBus2:
    """승객이 사라지게 만드는 버스 모델"""

    def __init__(self, passensgers=None):
        if passensgers is None:
            self.passengers = []
        else:
            self.passengers = list(passensgers)


# 또는 아래 처럼 하면 사라지지 않는다
import copy

bus = TwilightBus(copy.copy(basketball_team))
