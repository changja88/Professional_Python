from functools import partial, partialmethod

triple = partial(mul, 3)  # mul 함수의 첫번째 위치 인수를 3으로 바인딩해서 triple() 함수를 새로 만든다
print(('---------------------------------'))
print(triple(7))  # 테스트 이미 3이 들어가 있기 때문에 7을 넣어주면 21이 나온다

print(
    list(map(triple, range(1, 10)))  # 3이 첫번째 인수로 들어가 있기때문에 3을 1에서 10까지 곱한 값이 나온다
)
