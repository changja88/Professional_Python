"""
클래스 펙토리
"""
"""
- 예를 들어 지금 애완동물 가게용 어플리케이션을 만들고 있는데, 개에 대한 데이터를 간단한 레코드로 처리하고 싶다고 하자
  다음과 같은 식상한 코드는 좋지않다
"""


class Dog:
    def __init__(self, name, weight, owner):
        self.name = name
        self.weight = weight
        self.owner = owner


dog = Dog('Rex', 30, 'Bob')
print(dog)  # repr()로 출력한 내용도 빙구 같다

"""
namedtuple()에서 힌드를 얻어 Dog같은 간단한 클래스를 즉석으로 생성하는 recode_factory()
"""


def recode_factory(cls_name, field_names):
    try:
        field_names = field_names.replace(',', ' ').split()
    except AttributeError:
        # replace()나 split()을 사용할 수 없다
        pass
    field_names = tuple(field_names)

    def __init__(self, *args, **kwargs):
        attrs = dict(zip(self.__slots__, args))
        attrs.update(kwargs)
        for name, value in attrs.items():
            setattr(self, name, value)

    def __iter__(self):
        for name in self.__slots__:
            yield getattr(self, name)

    def __repr__(self):
        values = ', '.join('{}={!r}'.format(*i) for i
                           in zip(self.__slots__, self))
        return '{}({})'.format(self.__class__.__name__, values)

    cls_attrs = dict(__slots__=field_names,
                     __init__=__init__,
                     __iter__=__iter__,
                     __repr__=__repr__)

    return type(cls_name, (object,), cls_attrs)
    # type(my_object)를 이용해서 객체의 클래스와 동일한 my_object.__class__를 가져오므로,
    # type을 일종의 함수로 생각하기 쉽다. 그러나 type은 클래스다
    # 다음과 같이 인수 세개를 받아서 호출하면 새로운 클래스를 생성하는 일종의 클래스처럼 작동한다
    # name, bases, dict 이며, 이때 dict는 새로운 클래스의 속성명과 속성의 매핑이다


Dog = recode_factory('Dog', 'name weight owner')
rex = Dog('Rex', 30, 'Bob')
print(rex)

name, weight, _ = rex
print(name, weight)

"{2}'s dog wieghs {1}kg".format(*rex)

rex.weight = 32
print(rex.weight)
