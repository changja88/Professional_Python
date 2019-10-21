# @classmothod
# - 객체가 아닌 클래스에 연산을 수행하는 메서드를 정의한다는 것을 알 수 있다
# - 메서드가 호출되는 방식을 변경해서 클래스 자체를 첫 번째 인수로 받게 만들며, 대안 생성자를 생성 하기 위해 자주 사용 된다
#   ex)바이트로 부터 객체 만들기

# @staticmethod
# - 메서드가 특별한 첫 번째 인수를 받지 않도록 메서드를 변경한다
# - 본직적으로 정적 메서드는 모듀 대신 클래스 본체 안에 정의된 평범함 함수일 뿐이다
# - 그냥 평범한 일반적인 함수와 동일 하게 작동한다
# - 사실 왜 있는지 모르겠다. 클래스와 연관성 있는 함수를 작성하기 위함은 알겠는데, 굳이 클래스 안에까지 들어 와야 하나

# 두 데코레이터의 동작 비교
class Demo:
    a = 3

    def __init__(self, b):
        print('init')
        self.b = b

    @classmethod
    def klassmeth(*args):
        return args

    @staticmethod
    def statmeth(*args):
        return args


# 이게 또 존나 신기 방기하다
# a = Demo(b = 3)
# print(a)


test = Demo.klassmeth()[0]  # 클래스가 나와 버린다
print(test.a)

print()
print(Demo.klassmeth())
print(Demo.klassmeth('spam'))

print()
print(Demo.statmeth())
print(Demo.statmeth('spam'))


# 따로 찾은 classmethod, staticmethod 설명
class CustomClass:

    def add_instance_method(self, a, b):
        return a + b

    @classmethod
    def add_class_method(cls, a, b):
        return a + b

    @staticmethod
    def add_static_method(a, b):
        return a + b


print(CustomClass.add_instance_method(None, 3, 5))

# 첫번째 인자가 클래스지만 생략하고 접근 해야한다
print(CustomClass.add_class_method(3, 5))

print(CustomClass.add_static_method(3, 5))

# classmethod도 staticmethod도 객체에서 접근이 가능하다

a = CustomClass()
print(a.add_class_method(5, 5))
print(a.add_static_method(5, 5))


# 둘의 차이는 상속에서 차이다 두드러 진다
class Language:
    default_language = "English"

    def __init__(self):
        self.show = '나의 언어는' + self.default_language

    @classmethod
    def class_my_language(cls):
        return cls()

    @staticmethod
    def static_my_language():
        return Language()

    def print_language(self):
        print(self.show)


class KoreanLanguage(Language):
    default_language = '한국어'


a = KoreanLanguage.static_my_language()
b = KoreanLanguage.class_my_language()

# staticmethod에서는 부모클래스의 클래스속성 값을 가져오지만, classmethod에서는 cls인자를 활용하여 cls 클래스 속성을
# 가져 오는 것을 알 수 있다
a.print_language()
b.print_language()
