# 위치 매개변수에서 키워드 전용 매개변수까지

# - 키워드 전용 인수 (keyword-only argument)를 이용해서 향상된, 파이썬 3의 지극 융통성 있는 매게 변수 처리
#   메커니즘은 파이썬 함수에서 볼 수 있는가장 훌륭한 기능 중 하나다
#   함수를 호출할 때 반복 기능 객체나 매핑형을 별도의 인수로 '폭발'시키는 * 와 ** 기호도 이 캐머니즘과 밀접하게 연관되어 있다
# - 키워드 전용 인수란, 위치가 정해지지 않은 인수를 말한다
#   - * 이 사용된 인수 다음 부터는 키워드 전용 인수가 된다
#   - 이름이 없는 키워드 전용 인수를 만들기 위해서는 그냥 *를 추가하면 된다 (맨 마지마가에 예시 있음)
# - 즉 !!!!!! -> *이 분인 인수 다음 또는 그냥 * 다음 부터가 키워드 전용 인수 이다 !!!!

def tag(name, *content, cls=None, **attrs):
    """하나 이상의 HTML 태그를 생성한다."""
    if cls is not None:
        attrs['class'] = cls

    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value)
                           for attr, value
                           in sorted(attrs.items()))

    else:
        attr_str = ''

    if content:
        return '\n'.join('<%s%s>%s<\%s>' %
                         (name, attr_str, c, name) for c in content)

    else:
        return '<%s%s \>' % (name, attr_str)


print(tag('br'))
print("------------------------------------------------")
print(tag('p', 'hello'))
print("------------------------------------------------")
print(tag('p', 'hello', 'world'))  # 첫번째 이후의 인수들은 모두 *content 매개변수에 튜플로 전달된다
print("------------------------------------------------")
# tag 시그니처에 명시적으로 이름이 지정되지 않은 키워드 인수들은 딕셔너리로 **attrs에 인수에 전달된다
print(tag('p', 'hello', id=33))
print("------------------------------------------------")
# cls 매개 변수만 키워드 인수로 전달된다
print(tag('p', 'hello', 'world', cls='sidebar'))
print("------------------------------------------------")
print(tag(content='testing', name='img'))
print("------------------------------------------------")
my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'cls': 'framed'}
print(tag(my_tag))


# - 키워드 전용 인수는 파이썬3에 사로 추가된 기능이다
# - cls 매개변수는 키워드 인수만 전달될수 있으며 결코 익명의 위치 인수(positional argument)로는 전달되지 않는다
# - 함수를 정의할 때 키워드 전용 인수를 지정하려면 *가 붙은 인수뒤에 이름을 지정한다
# - 가변 개수의 위치 인수를 지원하지 않으면서 키워드 전용 인수를 지원 하고 싶으면 아래와 같이 *만 시그니처에 포함 시키면 된다
def f(a, *, b):
    return a, b


print(f(1, b=2))
