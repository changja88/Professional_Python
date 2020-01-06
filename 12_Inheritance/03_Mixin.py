"""
믹스인(Mixin)
"""
"""
- 믹스인이란 클래스에서 제공해야 하는 추가적인 메서드만 정의하는 작은 클래스를 말한다
    - 인스턴스 속성을 정의하지 않으며
    - __init__생성자를 호출하도록 요구하지 않는

- 파이썬은 다중 상속을 다루기 쉽게 하는 기능을 내장한 객체지향 언어이다. 다중상속으로 얻는 편리함과 캡슐화가 필요하다면 
  대신 믹스인을 작성하는 방안을 고려해야한다.
- 다른 클래스간 기능을 공유하고자 할 때 유용하다
- 동일한 코드를 반복하는 대신 공통 기능을 믹스인으로 그룹화 하고, 이를 필요하는 각 클래스로 상속받을 수 있다
"""

"""
사용처 : 한 클래스에 대해 많은 선택 기능을 제공할 때
- 즉 다중상속을 받아놓고, 상속받은 클래스에 있는 메서드를 골라서 사용하고 싶을 때
"""


class HasMethod1(object):
    def method(self):
        return 1


class HasMethod2(object):
    def method(self):
        return 2


class UsesMethod10(object):
    def usesmethod(self):
        return self.method() + 10


class UsesMethod20(object):
    def usesmethod(self):
        return self.method() + 20


class C1_10(HasMethod1, UsesMethod10):
    pass


class C1_20(HasMethod1, UsesMethod20):
    pass


class C2_10(HasMethod2, UsesMethod10):
    pass


class C2_20(HasMethod2, UsesMethod20):
    pass


print(C1_10().usesmethod() == 11)
print(C1_20().usesmethod() == 21)
print(C2_10().usesmethod() == 12)
print(C1_20().usesmethod() == 22)

"""
사용처 : 많은 다른 클래스에서 하나의 특정 기능을 사용하려고 할 때때
즉, 상속받은 클래스에 있는 메소드를 사용하고 싶을 
"""


class HasMethod1(object):
    def hasmethod1(self):
        return 1


class HasMethod2(object):
    def hasmethod2(self):
        return 2


class UsesMethod10(object):
    def usesmethod10(self):
        return self.method() + 10


class UsesMethod20(object):
    def usesmethod20(self):
        return self.method() + 20


class C1(HasMethod1, HasMethod2, UsesMethod10, UsesMethod20):
    def method(self):
        return 10


print(
    C1().hasmethod1(),
    C1().hasmethod2(),
    C1().usesmethod10()
)
