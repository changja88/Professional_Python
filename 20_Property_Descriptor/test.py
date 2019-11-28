# class P(object):
#     def __init__(self, fget=None):
#         self.fget = fget
#
#     def __get__(self, instance, owner):
#         if instance is None:
#             return self
#         if self.fget is None:
#             raise AttributeError('unreadable attribute')
#         return self.fget(instance)
#
#
# class A():
#     def __init__(self, name):
#         self._name = name
#
#     def name(self):
#         return self._name
#
#
# a = A('dahl')
# p = P(A.name)
# print(p.__dict__)
# print(p.__get__(a, A))

class Des(object):
    def __init__(self, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name, "")

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


class P(object):
    name = Des('name')
    print('name ', name.__dict__)


c = P()
print(c.name)
c.name = 'dahl'
print(c.name)
