"""
Itertools Library (526p 참고)
"""
import itertools

"""
필터링 제너레이터 함수
"""


def vowel(c):
    return c.lower() in 'aeiou'


word = 'Aardvark'
print(list(filter(vowel, word)))
print(list(itertools.filterfalse(vowel, word)))
print(list(itertools.dropwhile(vowel, word)))
print(list(itertools.takewhile(vowel, word)))
print(list(itertools.compress(word, (1, 0, 1, 1, 0, 1))))
print(list(itertools.islice(word, 4)))
print(list(itertools.islice(word, 4, 7)))
print(list(itertools.islice(word, 1, 7, 2)))

"""
매핑 제너레이터 함수
"""
print()
sample = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]
print(list(itertools.accumulate(sample)))
print(list(itertools.accumulate(sample, min)))
print(list(itertools.accumulate(sample, max)))
import operator

print(list(itertools.accumulate(sample, operator.mul)))
print(list(itertools.accumulate(range(1, 11), operator.mul)))
print()

print(list(enumerate('albatroz', 1)))
print(list(map(operator.mul, range(11), range(11))))
print(list(map(operator.mul, range(11), [2, 4, 8])))
print(list(map(lambda a, b: (a, b), range(11), [2, 4, 8])))

"""
반복형을 병합하는 제너레이터 함수
"""
print()
print(list(itertools.chain('ABC', range(2))))
print(list(itertools.chain(enumerate('ABC'))))  # Chain에 하나만 넣으면 유용하지 않다
print(list(itertools.chain.from_iterable(enumerate('ABC'))))
# 반복형에서 하나씩 가져와서 각 항목이 반복형이면 스퀀스 안에 연결한다
print(list(zip('ABC', range(5), [10, 20, 30, 40])))
print(list(itertools.zip_longest('ABC', range(5))))
print(list(itertools.zip_longest('ABC', range(5), fillvalue='?')))

"""
itertools.product()는 데카르트 곱을 느긋하게 계산 한다
"""
print()
print(list(itertools.product('ABC', range(2))))

suits = 'spades hearts diamods clubs'.split()
print(list(itertools.product('AK', suits)))

print(list(itertools.product('ABC')))
print(list(itertools.product('ABC', repeat=2)))

"""
입력된 항목 하나를 여러 개로 확장하는 제너레이터 함수
"""
print()
ct = itertools.count()
print(next(ct), next(ct), next(ct))

print(list(itertools.islice(itertools.count(1, .3), 3)))
# islice 를 사용하여 제한하면, count() 제너레이터에서 리스트를 생성 할 수 있다

cy = itertools.cycle('ABC')
print(next(cy))

print(list(itertools.islice(cy, 7)))

rp = itertools.repeat(7)
print(next(rp), next(rp))

print(list(itertools.repeat(8, 4)))

print(list(map(operator.mul, range(11), itertools.repeat(5))))

print(list(itertools.combinations('ABC', 2)))
print(list(itertools.combinations_with_replacement('ABC', 2)))
print(list(itertools.permutations('ABC', 2)))

"""
재배치 제너레이터 함수
groupby -> (<키>,<그룹 제너레이터>)튜플을 생성한다
"""
print()
print(list(itertools.groupby('LLLLLAAGGG')))
for char, group in itertools.groupby('LLLLAAGGG'):
    print(char, '->', list(group))

print()
animals = ['duck', 'eagle', 'rat', 'giraffe', 'bear', 'bat', 'dolphine', 'skark', 'lion']
animals.sort(key=len)
print(animals)

print()
for length, group in itertools.groupby(animals, len):
    print(length, '->', list(group))

print()
for length, group in itertools.groupby(reversed(animals), len):
    print(length, '->', list(group))

"""
반복형을 리듀스하는 함수
- 아래 나온 모든 예제는 reduce()로 구현할 수 있지만, 
  자주 발생하는 특정 문제를 쉽게 처리하기 때문에 별도의 내장형 함수로 존재한다
- all(), any()는 단락 평가(short-circuit evaluation)함수로써 reduce()로는 최적화할 수 없다.
- 단락 평가를 하는 경우에는 결과가 확정되는 즉시 반복자 소비를 중단한다 
"""
print()
print(all([1, 2, 3]))  # 모든 항목이 참된 값이면 true 아니면 false
print(any([1, 2, 3]))  # 항목들 중 하나라도 참된 값이면 true 아니면 false
