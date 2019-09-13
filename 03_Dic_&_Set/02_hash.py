# 파이썬에서 해시 가능하다는 발은
# - 수명 주기 동안 결코 변하지 않는 해시값을 갖고 있고 다른 객체와 비교할 수 있으면 객체를 해시 가능하다고 한다.
#   동일하다고 판단되는 개체는 방드시 해시값이 동일해야 한다

tt = (1, 2, (30, 40))
print(
    hash(tt)
)

t1 = (1, 2, [30, 40])  # 리스트는 해시 불가능 하다
print(
    hash(t1)
)

# - forzenset은 언제나 해시 가능하다
tf = (1, 2, frozenset([30, 40]))
print(
    hash(tf)
)

# - 사용자 정의 자료형은 기본적으로 해시 가능하다. 기본적으로 객체의 해시값은 id()를 이용해서 구하므로
#   모든 객체가 서로 다르기 때문이다. 객체가 자신의 내부 상태를 평가해서 __eq__()메서드를 직접 구현하는 경우에는
#   해시값 게산에 사용되는 속성이 모두 불변형일 때만 해시 가능 하다
