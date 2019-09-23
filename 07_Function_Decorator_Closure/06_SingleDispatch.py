# 단일 디스패치를 이용한 범용 함수
import html


def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)


# 위 코드를 아래와 같이 개선 하고 싶
# - str : 개행 문자를 <br>\n으로 대체하고 <pre> 대신 <p>태그를 사용한다
# - int : 숫자를 10진수와 16 진수로 보여준다
# - list : 각 항목을 자료형에 따라 포맷한 HTML 리스트를 출력한다

# - 파이썬에서는 메서드나 함수의 오버로딩을 지원하지 않으므로, 서로 다르게 처리하고자 하는 자료형별로 서로 다른
#   시그너처를 가진 htmlize()를 만들 수 없다. 이때 파이썬에서는 일반적으로 htmlize를 디스패치 함수로 변경하고,
#   일련의 if/elif/elif 문을 이용해서 htmlize_str, htmlize_int 등의 특화된 함수를 호출한다.
#   그러면 이 모듀의 사용자가 코드를 확장하기 쉽지 않으며, 다루기도 어렵다.

# - singledispatch()를 활용하면
#   - singledispatch 데커레이터는 각 모듈이 전체 해결책에 기여할 수 있게 해주며, 여러분이 편집할 수 없는 클래스에
#     대해서도 특화된 함수를 쉽게 제공할 수 있게 해준다
#   - 일반 함수를 singledispatch로 데커레이트하면, 이 함수는 '범용 함수'가 된다
#     즉 일련의 함수가 첫 번째 인수의 자료형에 따라 서로 다른 방식으로 연산을 수행 하게 된다


from functools import singledispatch
from collections import abc
import numbers


@singledispatch # 객체형을 다룰 기반 함수를 표시한다
def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)


@htmlize.register(str) # 각각의 특화된 함수는 @<기반_함수>.register(<객체형>)으로 데커레이트 된다
def _(text):
    content = html.escape(text).replace('\n', '<br>\n')
    return '<p>{0}</p>'.format(content)


@htmlize.register(numbers.Integral) # 특화된 함수의 이름은 필요없으므로 언더바로 함수명을 지정한다
def _(n):
    return '<pre>{0} (0x{0:x})</pre>'.format(n)


@htmlize.register(tuple)# 동일한 함수로 여러 자료형을 지원하기 위해서 register 데커레이터를 여러개 쌓아 올리수 있다
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n<ul>'


# - 가능하면 int나 list와 같은 구상 클래스 보다 numbers.Integral 이나 abc.MutableSequence와 같은 추상 베이스 클래스를
#   처리하도록 특화된 함수를 등록하는 것이 좋다. 추상 베이스 클래스로 등록하면 호환되는 자료형을 폭넓게 지원 할 수 있다
#   예를 들어 파이썬 확장은 int형의 대안으로 고정된 길이의 비트를 numbers.Itegeral의 서브클래스로 제공 할 수 있다


# - singlepatch 메커니즘은 특화된 함수를 시스템 어디에나, 어느 모듀에나 등록할 수 있다는 장점이 있다
# - 나중에 새로운 사용자 정의 자료형이 추가된 모듀을 추가할 때도 추가된 자료형을 처리하도록 쉽게 추가할 수 있다

# - singlepatch 는 자바 스타일의 메서드 오버로딩을 파이썬에 적용하기 위해 설계된 것이 아니다
# - 장황하게 if문이 반복 되는 블록을 가진 단일 함수보다 오버로드된 여러 메서드를 가진 클래스가 더 좋지만,
#   이 두 방법 모두 단일 코드 유닛(클래스나 함수)에 너무 많은 책임을 부여하는 결함이 있다
# - 이를 해결 하기 위함이다