class Studnet:
    old = -1

    def __init__(self, name, old=17):
        self.name = name
        self.old = old

    def print_name(self):
        print(self.name)

    def print_old(self):
        print(self.old)


s = Studnet('ABC', 20)
Studnet.print_name(s)  # unbound method call -> 클래스를 통해 함수를 호출하며, 인스턴스 객체를 parameter로 전달한다
s.print_name()  # bound method call -> 인스턴스 객체에 bind된 함수를 호출 한다

"""
메소드에서 self가 붙은 것 -> bound method, 즉 오브젝트 안에 있는 매소드들
메소드에서 self가 없는 것 -> unbound method, 즉 오브젝트와 상관없이 존재하는 매소드들
라고 한다
"""

"""
메서드 호출에는 bound와 unbound방식이 있다
두방식은 객체를 참조한다는 점에서 같지만, 메서드를 정의할 때 작성한 self가 객체와 자동으로 binding되어 있느냐의 차이이다
따라서 메서드를 호출할 때 인자로 객체를 넣어줘야 한다면 unbound 방식이고, 그렇지 않다면 bound 방식이다

여기에서 self는 객체 자기 자신을 의미하는 키워드이며, 메서드를 정의 할 때 첫번째 파라미터에 위치한다
"""


class Point:
    def set_x(self, x):
        self.x = x

    def get_x(self):
        return self.x

    def set_y(self):
        self.y = yield

    def get_y(self):
        return self.y


def unbound_class_call():
    p = Point
    Point.set_x(p, 10)
    Point.set_y(p, 20)
    print(Point.get_x(p), Point.get_y(p))


def bound_instance_call():
    p = Point()
    p.set_x(10)
    p.set_y(20)
    print(p.get_x(), p.get_y())


unbound_class_call()
bound_instance_call()
