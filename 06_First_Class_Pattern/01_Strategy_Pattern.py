# 함수 객체를 이용해서 전략 패턴을 리팩토링하고, 비슷한 방법으로 명령 패턴을 단순화하는 방법을 살펴본다


# 사례 : 전략 패턴의 리팩토링(strategy pattern)
# - 전략 패턴
#   - 일련의 알고리즘을 정의하고 각각을 하나의 클래스 안에 넣어서 교체하기 쉽게 만든다.
#     전략을 이용하면 사용하는 클라이언트에 따라 알고리즘을 독립적으로 변경할 수 있다


# - 일반적인 strategy pattern
from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')


class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):  # __total 이라는 변수가 이 클래스안에 있는지 확인
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total : {:.2f} due : {:.2f}>'
        return fmt.format(self.total(), self.due())


class Promotion(ABC):  # 전략 : 추상 베이스 클래스

    @abstractmethod
    def discount(self, order):
        """할인액을 구체적인 숫자로 변환한다"""


class FidelityPromo(Promotion):
    """충성도 포인트가 100점 이상인 고객에게 전에 5% 할인 적용"""

    def discount(self, order: Order) -> float:
        return order.total() * 0.5 if order.customer.fidelity >= 100 else 0


class BulkItemPromo(Promotion):
    """20개 이상의 동일 상품을 구입하면 10% 할인 적용"""

    def discount(self, order: Order) -> float:
        discount = 0
        for item in order.cart:
            if item.quantity > 20:
                discount += item.total() * 0.1
        return discount


class LargeOrderPromo(Promotion):
    """10종류 이상의 상품을 구입하면 전체 7% 할인 적용"""

    def discount(self, order: Order) -> float:
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * .07
        return 0


joe = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1100)
cart = [
    LineItem('banana', 4, .5),
    LineItem('apple', 10, 1.5),
    LineItem('watermellon', 5, 5.0)
]
print(Order(joe, cart, FidelityPromo()))
print(Order(ann, cart, FidelityPromo()))
bannana_cart = [
    LineItem('banana', 30, .5),
    LineItem('apple', 10, 1.5)
]

print(Order(joe, bannana_cart, BulkItemPromo()))

long_order = [
    LineItem(str(item_code), 1, 1.0)
    for item_code in range(10)
]
print(Order(joe, long_order, LargeOrderPromo()))
print(Order(joe, cart, LargeOrderPromo()))


# 함수지향 strategy pattern
# - 구체적인 전략 객체를 일반 함수로 교체 할 수 있다(promo 객체들)
# - 추상 클래스가 사라졌다 + 각각의 구체적인 전략이 함수로 구현 되었다 (효과)
class Order:
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):  # __total 이라는 변수가 이 클래스안에 있는지 확인
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total : {:.2f} due : {:.2f}>'
        return fmt.format(self.total(), self.due())


def fidelity_promo(order):
    """충성도 포인트가 100점 이상인 고객에게 전에 5% 할인 적용"""
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0


def bulk_item_promo(order):
    discount = 0
    for item in order.cart:
        if item.quantity > 20:
            discount += item.total() * 0.1
    return discount


def lafte_order_promo(order):
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0


print()
print(Order(joe, cart, fidelity_promo)) # 함수를 인자로 전달
