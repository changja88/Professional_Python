import numpy

# numpy 로 행렬 계산하기
a = numpy.arange(12)

print(a)
print('----------------\n')

print(a.shape)
print('----------------\n')

a.shape = 3, 4
print(a)
print('----------------\n')

print(a[2])
print('----------------\n')

print(a[:, 1])  # 1번 열을 가져온다
print('----------------\n')

print(a.transpose())

# 덱 및 기타 큐
# - append 와 pop을 이용해서 리스트를 스택이나 큐처럼 사용 할수 있다
# - 그러나 리스트 왼쪽에 삽입하거나 삭제하는 연산은 전체 리스트를 이동시켜야 하므로 처리 부담이 크다
# - 덱(collections.deque)클래스는 큐의 양쪽 어디에서든 빠르게 삽입 및 삭제할 수 있도록 설계된 스레드 안전한 양방향 큐다
# - 덱은 '최근에 본 항목'이나 이와 비슷한 것들의 목록을 유지할 때도 사용할 수 있다
# - 덱은 최대 길이를 성정해서 제한된 항목만 유지할 수도 있으므로 덱이 꽉찬 후에는 새로운 항목을 추가할때 반대쪽 항목을 버린다
from collections import deque

print('----------------\n')
print('----------------\n')
print('----------------\n')

dq = deque(range(10), maxlen=10)
print(dq)

dq.rotate(3)  # 양수를 받으면 오른쪽으로 n칸씩 이동 음수를 받으면 왼쪽으로 n칸씩이동
print(dq)

dq.appendleft(-1)  # 리스트 왼쪽에 n값을 추가
print(dq)

dq.extend([11, 22, 33])  # 오른쪽에 값을 추가
print(dq)

dq.extendleft([10, 20, 30, 40])
print(dq)

# - deque 모듈에서는 동기화된(쓰레드 안전한) Queue, LifoQueue, ProiorityQueue 클래스를 제공한다
# - 이 클래스들은 스레드 간에 안전한게 통신하기 위해 사용된다. 세 클래스 모두 0보다 큰 maxsize 인수를 생성자에 전달해서
#   바인딩 할 수있다. 그렇지만 덱과 달리공간이 꽉찼을 때 항목을 버리지 않는다. 대신 새로운 항목의 추가를 블로킹하고
#   다른 쓰레드에서 큐 안의 항목을 제거해서 공간을 확보해줄 때까지 기다린다 -> 활성화된 쓰레드 수를 조절하기 좋다

