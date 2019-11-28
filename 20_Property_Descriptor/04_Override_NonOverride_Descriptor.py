"""
오버라이딩 디스크립터와 논 오버라이딩 디스크립터
"""
"""
- 파이썬이 속성을 처리하는 방식에는 커다란 비대칭성이 있을을 주의하라
- 일반적으로 객체를 통해 속성을 읽으면 객체에 정의된 속성을 반환하지만, 객체에 그 속성이 없으면 클래스 속성을 읽는다
- 한편 일반적으로 객채의 속성에 값을 할당하면 객체 안에 그 속성을 만들고 클래스에는 전혀 영향을 미치치 않는다 

- 이런 비대칭성이 디스크립터에도 영향을 미쳐 __set__메서드의 정의 여부에 따라 두가지 범주의 디스크립터를 생성한다
"""


class Overriding:
    """데이터 디스크립터 혹은 강제 디스크립터라고도 한다"""

    def __get__(self, instance, owner):
        print('Overriding', ' __get__')

    def __set__(self, instance, value):
        print('Overriding', ' __set__')


class OverridingNoGet:
    """__get()__이 없는 오버라이딩 디스크립터"""

    def __set__(self, instance, value):
        print('OverridingNoGet', ' __set__')


class NoOverriding:
    """비데이터 디스크립터 혹은 가릴 수 있는 디스크립터라고도 한다"""

    def __get__(self, instance, owner):
        print('NoOverriding', ' __get__')


class Managed:
    over = Overriding()
    over_no_get = OverridingNoGet()
    non_over = NoOverriding()

    def spam(self):
        pass
        # print('-> Managed.spam({})'.format(display(self)))


"""
- __set__메서드를 구현하는 디스크립터를 '오버라이딩 디스크립터'라고한다
- 비록 클래스 속성이기는 하지만, __set__메서드를 구현하는 디스크립터는 객체 속성에 할당하려는 시도를 가로채기 때문이다
- 프로퍼티도 오버라이딩 디스크립터라고 할 수 있다
- 세터함수를 제공하지 않더라도, property클래스에서 기본적으로 제공하는 __set__메서드가 읽기전용 속성임을 알려주기 위해
  AttributeError를 발생시킨
"""
obj = Managed()
obj.over = 10
obj.over
"""
- __get__이 없는 오버라이딩 디스크립터
- __set__만 있기 때문에 저장 연산만 디스크립터가 처리한다
- 객체를 통해 디스크립터를 확인해보면 읽기 접근을 처리하는 __get__이 없으므로 디스크립터 객체 자체가 반환된다
- 즉, 읽기 연산의 경우에만 객체 속성이 디스크립터를 가린다
"""
print()
obj.over_no_get = 10
obj.over_no_get  # 호출되지 않는다
