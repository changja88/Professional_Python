# 메모리 뷰
# - 공유 메모리 시퀀스형으로서 bytes를 복사하지 않고 배열의 슬라이스를 다룰 수 있게 해준다
# - 메모리 뷰틑 본질적으로 파이썬 자체에 들어 있는 Numpy 배열 구조체를 일반화한 것이다
#   메모리 뷰는 PIL 이미지, SQLite 데이터베이스 NumPy 배열 등데이터 구조체를 복사하지 않고 메모리 공유 할수 있게 해준다
#   데이터셋이 커지는 경우 이것은 아주 중요한 기법니다

import array

numbers = array.array('h', [-2, -1, 0, 1, 2])

memv = memoryview(numbers)
print(len(memv))

memv_oct = memv.cast('B')
print(memv_oct.tolist())

memv_oct[5] = 4
print(numbers)
