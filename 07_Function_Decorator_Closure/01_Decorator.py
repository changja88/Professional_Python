# Chapter 목적
# - 함수 데커레이터는 소스 코드에 있는 함수를 '표시'해서 함수의 작동을 개선할 수 있게 해준다
#   강력한 기능이지만 데커레이터를 자유자재로 사용하려면 먼저 클로저를 알아야 한다

# - 클래스 중심의 엄격한 객체지향 방식을 고수한다면 nonlocal 기능을 사용하지 않고도 파이썬 프로그래머로서의 삶에 아무런
#   지장을 받지 않을 수 있다. 그러나 자기많의 데커레이터를 구현하고자 한다면 클로저를 속속들이 이해 해야 하며,
#   nonlocal이 필요 해진다

# - 데커레이터에서 사용하는 것 외에도, 클로저는 콜백을 이용한 효율적인 비동기 프로그래밍과 필요에 따라 함수형 스타일로
#   코딩하는 데에도 필수 적이다.


# 데코레이터 기본 지식
# - 데코레이터는 다른 함수를 인수로 받는 콜러블(데커레이트된 함수)이다.
# - 데코레이터는 데커레이트된 함수에 어떤 처리를 수행하고, 함수를 반환하거나 함수를 다른 함수나 콜러블 객체로 대채한다


# - 1. 데커레이터는 함수를 다른 함수로 대체하는 능력이 있다
# - 2. 데커레이터는 모듈이 로딩될 때 바로 실행된
# - 엄밀히 말해 데커레이터는 편리 구문(syntactic sugar)일 뿐이다. 아래 예저처럼 데커레이터는 다른 하수를 인수로 전달해서
#   호출하는 일반적인 콜러블과 동일하다. 그렇지만 런타임에 프로그램 행위를 변경하는 '메타프로그래밍'을 할 때 상당히 편하다
def deco(func):
    def inner():
        print('running inner()')

    return inner


@deco
def target():
    print('running target()')


target() # 모듈이 로딩 될때 바로 실행되기 때문에 running target()이 프린트 되지 않는

# - 2. 데커레이터의 핵심 특징은 데커레이트된 함수가 정의된 직후에 실행이다는 것이다
# - 일반적으로 파이썬이 모듈을 로딩하는 시점, 즉 '임포트 타임'에 실행 된다

print()
registry = []

def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func

@register
def f1():
    print('running f1()')

@register
def f2():
    print('running f2()')

@register
def f3():
    print('running f3()')

def main():
    print('running main()')
    print('registry ->',registry)
    f1()
    f2()
    f3()

main()