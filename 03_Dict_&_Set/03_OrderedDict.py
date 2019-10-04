# - collections.OrderedDict
#   - 키를 삽입한 순서대로 유지함으로써 항목을 반복하는 순서를 예측할 수 있다
#   - popitem()메서드는 기본적으로 최근에 삽입한 망목을 꺼내지만, popitme(last=True)로 하면 처음 삽힙한 항목을 꺼낸다


import collections

orderedDict = collections.OrderedDict(
    one=1, two=2, three=3
)

print(
    orderedDict.popitem(False)
)
print(
    orderedDict.popitem(True)
)

