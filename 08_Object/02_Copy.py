# 기본 복사는 얕은 복사
# - 리스트나 대부분의 내장 가변 컬렉션을 복사하는 가장 손쉬운 방법은 그 자료형 자체의 내장 생성자를 사용하는 것이다
l1 = [3, [55, 44], (7, 8, 9)]
l2 = list(l1)
print(l2)
print(l2 == l1)
print(l2 is l1)

# - 위에서처럼 생성자를 사용하거나 [:]을 사용하면 '얕은 사본'을 생성한다
l3 = l1[:]
print(l1 == l3)


# 객체의 깊은 복사와 얕은 복사
# - 내포된 객체의 참조를 공유하지 않도록 깊게 복사할 필요가 있는 경우가 있다
# - copy 모듀이 제공하는 deepcopy()함수는 깊은 복사를 copy 는 얕은 복사를 한다

class Bus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


import copy

bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
bus2 = copy.copy(bus1)
bus3 = copy.deepcopy(bus1)
print(id(bus1), id(bus2), id(bus3))

bus1.drop('Bill')
print(bus2.passengers)  # 얕은 복사에선 Bill이 없다
print(bus3.passengers)  # 깊은 복사에는 Bill이 있다
# - 일반적으로 깊은 사본을 만드는 일은 간단하지 않다. 객체 안에 순환 참조가 있으면 단순한 알고리즘은 무한 루프에 빠질수 있다
