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
