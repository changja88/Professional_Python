# 배열

# - 리스트형은 융통성 있고 사용하기 편하지만, 세부 요구사항에 따라 더 나은 자료형이 있다
# - 예를 들어 실수를 천만 개 저장해야 할때는 배열이 훨씬 더 효율 적이다
# - 배열은 모든 기능을 갖춘 float객체 대신 C언어의 배열과 마찬가지로 기계가 사용하는 형태로 표현된 바이트 값만 저장하기 때문

# - 리스트 안에 숫자만 들어 있다면 배열이

from array import array
from random import random

floats = array('d', (random() for i in range(10 ** 7)))
print(floats[-1])
fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()

floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10 ** 7)
fp.close()
print(floats2[-1])

print(floats == floats2)
