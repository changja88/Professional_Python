# 위치 매개변수에서 키워드 전용 매개변수까지

# - 키워드 전용 인수 (keyword-only argument)를 이용해서 향상된, 파이썬 3의 지그깋 융통성 있는 매게 변수 처리
#   메커니즘은 파이썬 함수에서 볼 수 있는가장 훌륭한 기능 중 하나다
#   함수를 호출할 때 반복 기능 객체나 매핑형을 별도의 인수로 '폴발'시키는 * 와 ** 기호도 이 캐머니즘과 밀접하게 연관되어 있다


def tag(name, *content, cls=None, **attrs):
    """하나 이상의 HTML 태그를 생성한다."""
    if cls is not None:
        attrs['class'] = cls

    if attrs:
        attr_str = ''.join(' %s="%s"' * (attr, value)
                           for attr, value
                           in sorted(attrs.items()))

    else:
        attr_str = ''

    if content:
        return '\n'.join('<%s%s>%s<\%s>' %
                         (name, attr_str, c, name) for c in content)

    else:
        return '<%s%s \>' % (name, attr_str)
