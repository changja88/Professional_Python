# - collections.ChainMap
#   - 매핑들의 목록을 담고 있으며 한꺼번에 모두 검색할 수 있다
#   - 각 매핑을 차례대로 검색하고, 그중 하나에서라도 키가 검색되면 성공한다
#   - 즉 dict를 몰아서 한군데에 저장을 하고 싹다 한번에 검색이 가능하다

import collections

chainmap = collections.ChainMap(
    dict(one=1, two=2), dict(three=3, four=4)
)

a = chainmap.pop('one')
print(a)


chainmap = collections.ChainMap(
    dict(one=10, two=2), dict(one=3, three=3)
)

v1 = chainmap.pop('one')
print(v1) # 중복된 키가 있다면 선입된 값이 나옴