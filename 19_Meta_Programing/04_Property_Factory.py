"""
속성을 검증하기 위해 프로퍼티 사용하기
"""


class LineItem:
    def __int__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


"""
문제점 -> 음수가 들어올 수 있다
"""


class LineItem2:
    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if value > 0:
            self.__weight = value
        else:
            raise ValueError('value mush be > 0')


# a = LineItem2('hello', -20, 20)
# 데커레이터를 사용하지 않는 방식(고전적인 방식)
class LineItem3:
    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

    def get_weight(self):
        return self.__weight

    def set_weight(self, value):
        if value > 0:
            self.__weight = value
        else:
            raise ValueError('value mush be > 0')

    wieght = property(get_weight, set_weight)  # property객체를 생성하고 클래스의 공개 속성에 할당한


a = LineItem3('hello', 20, -500)

"""
문제점 -> 이제 weight에 음수가 들어 갈수는 없지만 price에도 음수가 들어가지 않도록 하려면 똑같은 짓을 반복해야 한다
"""

"""
- 해결 방법 :
    - 프로퍼티를 추상환한다
    - 프로퍼티를 추상화하려면 프로퍼티 팩토리나 디스크립터(descriptor clas)를 사용한다
    - 디스크립터 클래스는 융통성이 뛰어나다
    - 프로퍼티 자체도 사실은 디스크립터 클래스로 구현된다
    
- 내장된 property()는 데커레이터로 사용되는 경우가 많지만, 사실상 클래스다 
"""

"""
프로퍼티 팩토리 구현하기

"""


def quantity(storage_name):
    def qty_getter(instance):
        return instance.__dict__[storage_name]

    def qty_setter(instance, value):
        if value > 0:
            instance.__dict__[storage_name] = value
        else:
            raise ValueError('value must be > 0')

    return property(qty_getter, qty_setter)


class LineItem3:
    weight = quantity('weight')
    price = quantity('price')

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price
