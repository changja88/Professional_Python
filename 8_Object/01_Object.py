# 변수는 상자가 아니다
# - 파이썬 변수는 자바에서의 참조 변수와 같으므로 변수는 객체에 붙은 레이블이라고 생각하는 것이 좋다
# - 변수는 상자라도 이해 할수 없는 예제
a = [1, 2, 3]
b = a
a.append(4)
b  # [1,2,3,4


# - 객체는 변수가 할당되기 전에 생성된다
class Gizmo:
    def __init__(self):
        print('Gizmo id: %d' % id(self))


x = Gizmo()
# y = Gizmo() * 100 # 에러가 발생하지만 곱셈을 시도하기 전에 두번째 기지모 객체가 실제로 생성되었음을 알 수 있따
print(dir())  # 하지만 윗줄에서 에러가 발생하였기 때문에 변수 y는 생성되지 않는

# - 변수는 단지 레이블일 뿐이므로 객체에 여러 레이블을 붙이지 못할 이유가 없다.
#   여러 레이블을 붙이는 것을 'alias(별명)'이라고 한다

# 정체성, 동질성, 별명

charls = {'name': 'Charles L. Dodgson', 'born': 1832}
lewis = charls
print(lewis is charls) # True
print(
    id(charls), id(lewis)
)
lewis['balance'] = 950
print(charls)
