"""
파이썬 네이밍 규칙
- __ 가 앞에 붙어 있으면 -> private
- _ 가 앞에 붙어 있으면 -> protecrted
- 물론 파이썬에서는 직접 접근이 가능하지만 웬만 하면 건들지 말라는 약속이다
"""


class Test:
    def __init__(self):
        self.public_filed = 5
        self.__private_field = 6
        self._protected_filed = 7

    def _private_method(self):
        pass


t = Test()
t.public_filed = 10
t.__private_field = 11
t._protected_filed = 12

"""
파이썬 getter, setter
당연히 파이썬 에서도 겟터,셋터를 만들어서 사용 할수 있다
하지만 여전히 직접 접근도 가능하다
"""


class Test1:
    def __init__(self):
        self.color = 'red'

    def set_color(self, clr):
        self.color = clr

    def get_color(self, clr):
        return self.color


t1 = Test1()
t1.set_color('blue')
t1.color = 'blue'

"""
@property 으로도 할 수 있다
"""


class Test2:
    def __init__(self):
        self.__color = 'red'

    @property  # -> getter 역활을 한다
    def color(self):
        return self.__color

    @color.setter  # -> setter 역활을 한다
    def color(self, clr):
        self.__color = clr


t2 = Test2()
t2.color = 'blue'
t2.__clor = 'blue'  # 이것도 파이썬에서는 가능하다
