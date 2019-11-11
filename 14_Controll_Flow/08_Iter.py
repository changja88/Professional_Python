"""
iter() 함수 들여다 보기
"""
from random import randint

"""
- 파이썬은 어떤 객체를 반복해야 할 때 iter()를 호출한다
- 그러나 이 함수는 일반 ㅎ마수나 콜러블 객체로부터 반복자를 생성하기 위해 두 개의 인수를 전달해서 호출 할 수도 있다
  이렇게 사용하려면, 첫 번째 인수는 값을 생성하기 위해 인수 없이 반복적으로 호출되는 콜러블이어야 하며,
  두 번째 인수는 구분 표시로서, 콜러브레엇 이 값이 반환되면 반복자가 StopIteration예외를 발생시키도록 만든다
"""


def d6():
    return randint(1, 6)


d6_iter = iter(d6, 1)
print(d6_iter)

for roll in d6_iter:
    print(roll)

# 파일에서 빈 줄을 발견하거나 파일의 끝에 도달할 때까지 한 줄씩 읽어 나간
with open('abc.txt') as fp:
    for line in iter(fp.readline, ''):
        pass

print()
