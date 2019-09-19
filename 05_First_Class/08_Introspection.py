# 매개변수에 대한 정보 읽기


import bobo


# - bobo가 hello() 함수의 내부를 조사해서 이 함수가 작동하려면 person이라는 매개변수가 필요하다는 것을 알아낸다는 것이다
#   그리고 나서 요청에서 해당 이름의 매개 변수를 가져와서 hello()에 전달하므로 프로그래머는 요청 객체를 건드릴 필요가 전혀 없다
@bobo.query('/')
def hello(person):
    return 'Hello %s!' % person


# - 함수 객체 안의 __defaults__ 속성에는 위치 인수와 키워드 인수의 기본값을 가진 튜플이 들어 있다
#   키워드 전용 인수의 기본값은 __kwdefaults__속성에 들어 있다. 그러나 인수명은 __code__속성에 들어 있는데,
#   이 속성은 여러 속성을 담고 있는 code 객체를 가리킨다
#   이속의 사용 방법은 다음과 같다

# 원하는 길이 가까이에 있는 공백에서 잘라서 문자열을 단축시키는 함수
def clip(text, max_len=80):
    """
    max_len 앞이나 뒤의 마지막 공백에서 잘라낸 텍스트를 반환한다
    """
    end = None
    if len(text) > max_len:
        space_before = text.rfind('', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind('', max_len)
            if space_after >= 0:
                end = space_after

    if end is None:
        end = len(text)
    return text[:end].rstrip()


# 함수 인수에 대한 정보 추출하기 -> 그다지 사용하기 편하게 배치되어 있지 않ㄷ
print(clip.__defaults__)
print(clip.__code__)
print(clip.__code__.co_varnames)
print(clip.__code__.co_argcount)
print('\n')

# 개선
from inspect import signature

sig = signature(clip)
print(sig)
for name, param in sig.parameters.items():
    print(param.kind, ':', name, '=', param.default)
# - inspect.signature()는 inspect.Signature 객체를 반환하며, 이 객체에 들어 있는 parameters 속성을 이용하면
#   정렬된 inspect.Parameter 객체를 읽을수 있다. 각 Parameter 객체 안에는 name, default, kind 등의 속성이 들어 있따
# - kind 속성은 _ParameterKind 클래스에 정의된 다음 다섯 가지 값중 하나를 가진다
#       - POSITIONAL_OR_KEYWORD : 위치 인수나 키워드 인수로 전달할 수 있는 매개변수 (대부분이다)
#       - VAR_POSITIONAL : 위치 매겨변수의 튜플
#       - VAR_KEYWORD : 키워드 매개변수의 딕셔너리
#       - KEYWORD_ONLY : 키워드 전용 매개변수
#       - POSITIONAL_ONLY : 위치 전용 매개변수, 현재 파이썬 함수 선언 구문에서는 지원 되지 않는다


