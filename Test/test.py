# 참조로서의 함수 매개 변수
# call by sharing 매개 변수 전달 방식만 지원한다
# 함수는 인수로 전달 받은 모든 가변 객체를 변경 할 수 었지만, 객체의 정체성 자체는 변경 할 수 없다
# 즉, 어떤 객체를 다른 객체로 바꿀 수는 없다


def f(a, b):
    a += b
    return a


x = 1
y = 2
print(f(x, y))
print(x, y)

a = [1, 2]
b = [3, 4]
print(f(a, b))
print(a, b)

# 따라서 가변형 매개변수를 기본값으로 사용하는 것은 좋지 않은 생각이다

print('------------------------------------------')


class HauntedBus:
    def __init__(self, passengers=[]):
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


bus1 = HauntedBus(['alice', 'bill'])
print(bus1.passengers)
bus1.pick('charie')
print(bus1.passengers)
print('------------------------------------------')

bus2 = HauntedBus()
bus2.pick('charie')
print(bus2.passengers)
print('------------------------------------------')

bus3 = HauntedBus()
print(bus3.passengers)
print(bus2 == bus3)
print('------------------------------------------')

bus3.pick('dave')
print(bus2.passengers)
print('------------------------------------------')


# bus2와 bus3의 passengers가 동일한 리스트를 참조 한다는 것이다
# 그러나 bus1.passengers는 별개의 리스트이다 -> 이유는 passengsers 매개변수 기본값의 별명이 되기 때문이다


class Bus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)


class TwilightBus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = passengers


    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

basketball_team = ['Sue', 'Tina', 'Maya', 'Diana', 'Pat']
bus = TwilightBus(basketball_team)

bus.drop('Tina')
bus.drop('Pat')
print(basketball_team)




