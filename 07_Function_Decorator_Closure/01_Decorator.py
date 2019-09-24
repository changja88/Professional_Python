# Chapter 목적
# - 함수 데커레이터는 소스 코드에 있는 함수를 '표시'해서 함수의 작동을 개선할 수 있게 해준다
#   강력한 기능이지만 데커레이터를 자유자재로 사용하려면 먼저 클로저를 알아야 한다

# - 클래스 중심의 엄격한 객체지향 방식을 고수한다면 nonlocal 기능을 사용하지 않고도 파이썬 프로그래머로서의 삶에 아무런
#   지장을 받지 않을 수 있다. 그러나 자기많의 데커레이터를 구현하고자 한다면 클로저를 속속들이 이해 해야 하며,
#   nonlocal이 필요 해진다

# - 데커레이터에서 사용하는 것 외에도, 클로저는 콜백을 이용한 효율적인 비동기 프로그래밍과 필요에 따라 함수형 스타일로
#   코딩하는 데에도 필수 적이다.


# 데코레이터 기본 지식
# - 데코레이터는 함수를 리턴해야 한다
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


target()  # 모듈이 로딩 될때 바로 실행되기 때문에 running target()이 프린트 되지 않는다

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


def f3():
    print('running f3()')


def main():
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()


if __name__ == '__main__':
    main()

# 결과에서 알 수 있는 것 : 함수 데커레이터는 모듈이 임포트되자마자 실행되지만,
#                     데커레이트된 함수는 명시적으로 호출될 때 만 실행된다 -> '임포트 타임' '런타임'의 차이를 보여준다
# 위 예제와 실제 사용 간의 차이
#   - 데커레이터 함수가 데커레이트되는 함수와 같은 모듈에 정의 되어 있다. 일반적으로 실제 코드에서는 데커레이터를 정의하는
#     모듈과 데커레이터를 적용하는 모듈을 분리해서 구현한다
#   - register() 데커레이터가 인수로 전달된 함수와 동일한 함수를 반환하지만,
#     실제 코드에서 대부분의 데커레이터는 내부 함수를 정의해서 반환한다


# 데커레이터로 개선된 전략 패턴
promos = []


def promotion(promo_func):
    promos.append(promo_func)
    return promo_func


@promotion
def fidelity(order):
    """충성도 포인트가 1000점 이상인 고객에게 전체 5% 할인 적용"""
    return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0


@promotion
def bulk_item(order):
    """20개 이상의 동일 상품을 구입하면 10% 할인 적용"""
    discount = 0
    for item in order.cart:
        discount += item.total() * .1
    return discount


@promotion
def large_order(order):
    """10종류 이상의 상품을 구입하면 전체 7% 할인 적용"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) > 10:
        return order.totla() * .07
    return 0


def best_promo(order):
    """최대로 할일받을 금액을 반환한다"""
    return max(promo(order) for promo in promos)


# 대부분의 데커레이터는 데커레이트된 함수를 변경한다
# - 즉 내부 함수를 정의하고 그것을 반환하여 데커레이트된 함수를 대체한다
# - 내부 함수를 사용하는 코든는 제대로 작동하기 위해 거의 항상 클로저에 의존한다.


# 간단한 데커레이터 구현하기

def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)  # clockecd()에 대한 클로저에 자유변수 func가 들어가야 이 코드가 작동한다
        elapsed = time.perf_counter()
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, args, result))
        return result

    return clocked


@clock
def snooze(seconds):
    time.sleep(seconds)


@clock
def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


# factorial 실제로 작동 하는 순서 --------------------
factorial = clock(factorial)
# ------------------------------------------------

if __name__ == '__main__':
    print('*' * 40, 'Calling snooze(.123)')
    snooze(.123)
    print('*' * 40, 'Calling factorial(6)')
    print('6! =', factorial(6))

# 누적된 데커레이터
# @d1
# @d2
# def f():
#     print('f')
#   - 위 코드는 아래와 동일하다 즉 아래에서 위로 전달이 된다
# f = d1(d2(f))


# 매개변수화된 데커레이터
# - 소스 코드에서 데커레이터를 파싱할 때 파이썬은 데커레이트된 함수를 가져와서 데커레이터 함수의 첫번째 인수로 넘겨준다
# - 어떻게 다른 인수를 받는 데커레이터를 만들 수 있을까?
#   - 데커레이터를 반환하는 데커레이터 팩토리를 만들고 나서, 데커레이트될 함수에 데커레이터 팩토리를 적용하면 된다
# 기본 ---------------------------------------------------------------------------
print()
registry = []


def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func


@register
def f1():
    print('running f1()')


print('running main()')
print('registry ->', registry)
f1()
# 기본 ---------------------------------------------------------------------------

# 매개변수화된 데코레이터 1 ---------------------------------------------------------
print()
registry = set()


def register(active=True):  # 이함수가 데커레이터 팩토리
    def decorate(func):  # 이게 데커리이터임으로 함수를 반환해야 한다
        print('running register(active=%s) -> decorate(%s)' % (active, func))
        if active:  # 클로저에서 읽어온 active
            registry.add(func)
        else:
            registry.discard(func)
        return func

    return decorate


@register(active=False)
def f1():
    print('running f1()')


@registerb
def f2():
    print('running f2()')


def f3():
    print('running f3()')


print('running main()')
print('registry ->', registry)

register()(f3)  # register()까지 하면 decorate()를 나오고, 이게 f3()에 적용된다
register(active=False)(f3)  # 팩토리로 사용되기 때문에 register()를 호출하고 (f3)을 해준다
# 매개변수화된  데코레이터 1 ---------------------------------------------------------


# 매개변수화된 데코레이터 2 -------------------------------------------------------------
import time

DEFAULT_FMT = '[{elapsed:0.8f {name}({args}) -> {result}]'


def clock(fmt=DEFAULT_FMT):  # 매개변수화된 데커레이터 팩토리
    def decorate(func):  # 실제 데커레이터
        def clocked(*_args):  # 데커레이터된 함수를 래핑한다, _args가 실제 clocked()의 인수를 담고 있다
            t0 = time.time()
            _result = func(*_args)  # 데커레이터된 함수의 결과를 저장한다
            elapsed = time.time() - t0
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)
            result = repr(_result)
            print(fmt.format(**locals()))  # **locals()를 사용하면 fmt가 clocked()의 지역 변수를 모두 참조할수 있게 해준다
            return _result

        return clocked

    return decorate


if __name__ == '__main__':
    print()


    @clock('{name}: {elapsed}s')
    def snooze(seconds):
        time.sleep(seconds)


    for i in range(3):
        snooze(.123)  # 매개변수화된 데코레이터1 과 사용 방법이 다른 이유는 clockec가 직접 snooze()의 결과 값을 리턴하기 때문
# 매개변수화된 데코레이터 2 -------------------------------------------------------------
