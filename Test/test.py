import functools


def standalone(self, a=1, b=2):
    print(' called standalone with : ', (self, a, b))
    if self is not None:
        print(' self.attr = ', self.attr)


class MyClass:

    def __init__(self):
        self.attr = 'instance attribute'

    method1 = functools.partialmethod(standalone)
    method2 = functools.partial(standalone)

o = MyClass()

print('standalone')
standalone(None)

print()
print('method 1 as partialmethod')
o.method1()

print()
print('method 2 as partialmethod')
try:
    o.method2()
except TypeError as err :
    print('ERROR:{}'.format(err))
