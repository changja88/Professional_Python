# http://schoolofweb.net/blog/posts/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%8D%B0%EC%BD%94%EB%A0%88%EC%9D%B4%ED%84%B0-decorator/
"""
1. 데코레이터 작동 원리
"""


def decoratoor_function1(original_function):
    print('a')

    def wrapper_function():
        print('b')
        return original_function()

    return wrapper_function


def display():
    print('display is called')


decorated_display = decoratoor_function1(display)
decorated_display()
print()
"""
2. 데코레이터를 사용 하는 이유
- 기존의 코드를 수정하지 않고도, 패러(wrapper)함수를 이용하여 여러가지 기능을 추가할 수 있기 때문이다
- 하나의 데코레이터를 만들어서 두개의 함수에 기능을 추가할 수 있
"""


def decorator_function2(original_function):
    def wrapper_function():
        print('{} 함수가 호출되기전 입니다.'.format(original_function.__name__))
        return original_function()

    return wrapper_function


@decorator_function2
def display_1():
    print('display_1 함수가 실행됐습니다')


@decorator_function2
def display_2():
    print('display_2 함수가 실행됐습니다')


# display_1 = decorator_function2(display_1)
# display_2 = decorator_function2(display_2)
#
print()
display_1()
display_2()
print()

"""
3. 인수를 받는 데코레이트된 함수를 만드는 방법
"""


def decorator_function3(original_function):
    def wrapper_function(*agrs, **kwargs):
        print('{} 함수가 호출되기전 입니다.'.format(original_function.__name__))
        return original_function(*agrs, **kwargs)

    return wrapper_function


@decorator_function3
def display_info(name, age):
    print('display_info({},{}) 함수가 실행됐습니다'.format(name, age))


print()
display_info('Jhon', 25)
print()
"""
4. 데코레이터 클래스를 만드는 방법
"""


class DecoratorClass:
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('{} 함수가 호출되기전 입니다.'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)

@DecoratorClass  #3
def display_info(name, age):
    print ('display_info({}, {}) 함수가 실행됐습니다.'.format(name, age))


print()
display_info('John', 25)
print()
