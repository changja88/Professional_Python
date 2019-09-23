# 이것만 보지말고 01_Decorator도 무조건 봐야 한다 !!

# 데코레이터는 무조건 함수를 리턴해야 한다
# 데코레이터는 데코레이트된 함수가 정의 될때 호출 된다
def pretty0(param=True):  # 데코레이터 팩토리
    print('함수 호출 시점 1')

    def decorate(func):  # 실제 데코레이터
        print("함수 호출 시점 2")
        return func

    return decorate


@pretty0
def test1():
    pass


@pretty0()  # 데코레이터 팩토리를 호출 했음으로 '함수 호출 시점 2' 가 출련된다
def test2():
    pass


# 사용 방법 1 -> 데커레이트된 함수와 상관없이 할거 하고 데커레이트된 함수 그대로 돌려주기
# -----------------------------------------------------------------------------
a = []


def decorate(func):
    a.append(func)
    return func


@decorate
def f1():
    return 'f1'


print('사용방법 1 ' + f1())


# -----------------------------------------------------------------------------

# 사용 방법 2 -> 데커레이트 함수에 인자를 전달 하기 -> 데코레이터 팩토리 이용
# -----------------------------------------------------------------------------
def pretty(param):  # 데코레이터 팩토리

    def decorate(func):  # 실제 데코레이터
        return func

    return decorate


@pretty
def f2():
    return 'f2'


print('사용방법 2 ')

pretty(param='param')(f2)  # 첫번째 방법 이렇게 데코레이터 팩터리를 호출하고 반환된 decorate에 f2를 전달한다


@pretty(param='param')  # 두번째 방법 데코레이터 에서 미리 인수를 전달한다. 전달할 인수가 없으면 그냥 pretty() 이렇 해도 된다
def f3():
    return 'f3'


f3()  # 이미 param에 값을 전달했음으로 바로 호출 할 수 있다


# -----------------------------------------------------------------------------

# 사용 방법 3 -> 데코레이터에게 함수의 인자를 전달하는 방법
# -----------------------------------------------------------------------------
# 방법 1
def pretty(func):
    def decorate(a, b):
        result = func(a + 2, b)
        return result

    return decorate


# @pretty
# def f4(*args):
#     return sum(args)
#

@pretty
def f4(a, b):
    return a + b


print(f4(1, 2))


# 방법 2
def pretty(func):
    def decorate(*args):
        result = func(*args)
        return result

    return decorate


# @pretty
# def f4(*args):
#     return sum(args)
#

@pretty
def f5(a, b):
    return a + b


print(f5(1, 2))
# -----------------------------------------------------------------------------
