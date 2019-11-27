class Quantity:
    __counter = 0  # Quantity2 객체의 수를 센다

    def __init__(self):
        cls = self.__class__
        prefix = cls.__name__
        index = cls.__counter
        self.storage_name = '_{}#{}'.format(prefix, index)
        cls.__counter += 1

    def __get__(self, instance, owner):
        # - instance.__dict__대신 고수준 getattr 내장 함수를 이용해서 값을 저장할 수 있다
        # - 관리 대상 속성과 저장소 속성의 이름이 다르기 때문에 저장소 속성에 getattr을 호출하더라도
        #   디스크립터를 실행하지 않으므로 재귀가 발생하지 않는다
        # - owner는 관리 대상 클래스(즉,LineItem)에 대한 참조며, 디스크립터를 이용해서 클래스의
        #   속성을 가져올때 유용하게 사용할 수 있다
        if instance is None:
            return self
        else:
            return getattr(instance, self.storage_name)

    def __set__(self, instance, value):
        if value > 0:
            setattr(instance, self.storage_name, value)
        else:
            raise ValueError('value must be > 0')


class LineItem2:
    weight = Quantity()
    price = Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price
