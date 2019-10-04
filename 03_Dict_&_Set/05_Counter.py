# - Counter
#   - 모든 키에 정수형 카운터를 갖고 있는 매핑
#   - 기존 키를 갱신하면 카운터가 늘어난다
#   - 이 카운터는 해시 가능한 객체(키)나 한 항목이 여러 번 들어갈 수 있는 다중 집합에서 객체의 수를 세기 위해 사용할 수 있다
#   - Counter 클래스는 합계를 구하기 위한 + 와 - 연산자를 구현하며, n개의 가장 널리 사용된 항목과 그들의 카운터로 구성된
#     튜플의 리스트를 반환하다 most_common([n]) 등의 메서드를 제공한다
import collections

ct = collections.Counter('abracadabra')
print(ct)

ct.update('aaaaazzz')
print(ct)


# 가장 많이 사용된 상위 2개
print(
    ct.most_common(2)
)
