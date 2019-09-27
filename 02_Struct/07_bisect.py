# bisect
#   - bisect 모듈은 bisect()와 insort() 함수를 제공한다
#   - bisect()는 이진 검색 알고리즘을 이용해서 시퀀스를 검색하고
#   - insort()는 정렬된 시퀀스 안에 항목을 삽입한다

#   - bisect로 검색하기
#       - bisect(haystack, needle)은 정렬된 시퀀스인 haystack안에서 오름차순 정렬 상태를 유지한채로
#         needle을 추가할 수 있는 위치를 찾아낸다
#       - bisect(haystack, needle)의 결과값을 인덱스로 사용해서 haystack.insert(index, needle)을 호출 하면 된다
#   - insort
#       - 위에 나온 과정을 한방에 해준다
#   - bisect_left, bisect_right : 같은 값이 있을 경우 오른쪽에 넣을지 왼쪽에 넣을지 정한다

import bisect
import sys

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d} {2}{0:2d}'


def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        offset = position * '  |'
        print(ROW_FMT.format(needle, position, offset))


if __name__ == '__main__':
    if sys.argv[0] == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect

print('DEMO: ', bisect_fn.__name__)
print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
demo(bisect_fn)


#   - bisect를 사용하면 수치형 값으로 테이블을 참조할 수 있으므로 시험 점수를 등급문자로 변환할 수 있다
def grade(score, breakpoints=[60, 70, 80, 90], grades='FDBCA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]


print(
    [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]
)

#   - insort 사용방법
#       - 정렬은 값비싼 연산이므로 시퀀스를 일단 정렬한 후에는 정렬 상태를 유지하는 것이 좋다 -> insort써라
#       - insort(seq,item)은 seq를 오름차순으로 유지한 채로 item을 seq에 삽입한다

import bisect
import random

SIZE = 7

random.seed(1729)

my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE * 2)
    bisect.insort(my_list, new_item)
    print('%2d ->' % new_item, my_list)
