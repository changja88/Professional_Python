"""
속성 디스크립터
- 파이썬을 정복하려면 디스크립터를 알아야한다!
"""
"""
- 디스크립터를 이용하면 여러 속성에 대한 동일한 접근 논리를 재사용할 수 있다
- 디스크립터는 __get__, __set__, __delete__메서드로 구성된 프로토콜을 구현하는 클래스이다
- property 클래스는 디스크립터 프로토콜을 완벽히 구현한다
- 대부분의 디스크립터는 __get__과 __set__메서드만 구현하고 둘 중 하나만 구현한 것도 많다

- 디스크립터는 파이썬의 독특한 특징으로서, 어필리케이션 수준뿐만 아니라 언어의 기반 구조에도 적용되어 있다
- 프로퍼티 외에도 메서드 및 @classmethod와 @staticmethod데커레이터가 디스크립터를 활용하는 파이썬 기능이다 
"""

"""
- 프로퍼티 팩토리를 사용하면 함수형 프로그래밍 스타일을 적용함으로써 똑같은 게터와 세터를 반복해서 구현할 필요가 없다.
- 프로퍼티 함수는 고위 함수로서 일련의 접근자 함수를 매개변수화하고 stroage_name과 같은 환경변수를 클로저에 담아서 
  사용자 정의 프로퍼티 객체를 생성한다
- 이와 동일한 문제를 객체지향방식으로 해결한 것이 디스크립터 클래스다
"""

"""
- 디스크립터 클래스 
    - 디스크립터 프로토콜을 구현하는 클래스 
    - 19_Meta_Programming -> 04_Property_Factory 의 quantity
    
- 관리 대상 클래스 
    - 디스크립터 객체를 클래스 속성으로 선언하는 클래스 
    - 19_Meta_Programming -> 04_Property_Factory 의 Lineitem
    
- 디스크립터 객체 
    - 관리 대상 클래스의 클래스 속성으로 선언된, 디스크립터 클래스의 객체

- 관리 대상 객체
    - 관리 대상 클래스의 객체.
    - 이 예제에서는 LineItem클래스의 객체들이 관리 대상 객체가 된다

- 저장소 속성
    - 관리 대상 객체 안의 관리 대상 송값을 담을 속성
    - LineItem객체의 weight와 price 속성이다
    - 이들은 디스크립터 객체와는 별개의 속성으로, 항상 클래스 속성이다
    
- 관리 대상 속성
    - 디스크립터 객체에 의해 관리되는 관리 대상 클래스 안의 공개 속성으로, 이 속성의 값을 저장소 속성에 저장된다.
    - 즉, 디스크립터 객체와 저장소 속성이 관리 대상 속성에 대한 기반을 제공한다 
"""


class Quantity:
    def __init__(self, storatge_name):
        self.storage_name = storatge_name

    def __set__(self, instance, value):
        if value > 0:
            instance.__dict__[self.storage_name] = value
            # setattr() 내장함수를 호출하면 다시 __set__이 호출되어서 무한 루프가 되니 주
        else:
            raise ValueError('value must be > 0')


class LineItem:
    weight = Quantity('weight')
    price = Quantity('price')

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


"""
문제점 -> weight = Quantity('weigh')은 할당문이기때문에 오른쪽이 먼저 실행이 되는데, 이때 변수는 존재하지 않는다
        디스크립터 객체를 생성하기 위해 Quantity() 표현식이 평가되는데, 이때 Quantity클래스 안에 있는 코드에서는
        디스크립터 객체를 어떤 이름의 변수(예를 들면 weight또는 price)에 바인딩해야 할지 알 수 없다는 것이다
        그렇기 때문에 위 예제 코드에서는 명시적으로 지정하고 있다
"""


class Quantity2:
    __counter = 0 # Quantity2 객체의 수를 센다

    def __init__(self):
        cls = self.__class__
        prefix = cls.__name__
        index = cls.__counter
        self.storage_name = '_{}#{}'.format(prefix, index)
        cls.__counter += 1

    def __get__(self, instance, owner):
        return getattr(instance, self.storage_name)

    def __set__(self, instance, value):
        if value > 0:
            setattr(instance, self.storage_name, value)
        else:
            raise ValueError('value must be >0')


class LineItem2:
    weight = Quantity2()
    price = Quantity2()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price
