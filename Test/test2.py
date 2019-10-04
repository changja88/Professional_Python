def standalone(self, a=1, b=2):
    print('called standalone with : ', (self, a, b))
    if self is not None:
        print('self.attr = ', self.attr)


import functools


class MyClass:
    def __init__(self):
        self.attr = 'instance attribute'

    method1 = functools.partialmethod(standalone)
    method2 = functools.partial(standalone)


o = MyClass()
standalone(None)



o.method1()
o.method2()