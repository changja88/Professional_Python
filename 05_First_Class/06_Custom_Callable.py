# 사용자 정의 콜러블 형
# - 파이썬 함수가 살제 객체일 뿐만 아니라, 모든 파이썬 객체가 함수처럼 동작하게 만들수 있다
# - 단지, __call__() 인스턴스 메서드를 구현하면 된다


import random


class BingoCage:

    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('Pick from empty BingoCage')

    def __call__(self, *args, **kwargs): # 이걸 구현 해줘야 객체 자체를 콜 할수 있다
        return self.pick()


bingo = BingoCage(range(3))

print(
    bingo.pick()
)
print(
    bingo() # 객체 콜이 가능하다 __call__을 구현 했기 때문
)

print(
    callable(bingo)
)