"""
- 키워드 전용 인수란, 위치가 정해지지 않은 인수를 말한다
- *이 사용된 인수 다음 부터는 키워드 전용 인수가 된다
- 이름이 없는 키워드 전용 인수를 만들기 위해서는 그냥 *를 추가하면 된다
"""
from inspect import signature


def tag(name, *content, cls=None, **attrs):
    print('name : ', name)
    print('content : ', content)
    print('cls : ', cls)
    print('attrs : ', attrs)


# tag(1, 2, 3, 4,  cls='abcd', attrs=dict(one=1))
# tag(1, 2, 3, 4,  cls='abcd', id=11,abc=1111)
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


sig = signature(clip)
for name, param in sig.parameters.items():
    print(param.kind, " : " , name, ' = ',param.default)
