"""
zip_longest
"""
import itertools

"""
zip -> 갯수가 같은 iterable 객체에 대해서만 실행이 가능하다
zip_longest -> 갯수가 다른 iterable에서 zip이 가능하게해준다 fillvalue를 통해서
"""

print()
a = (1, 2, 3, 9, 9, 9)
b = (4, 5, 6)
c = itertools.zip_longest(a, b, fillvalue=0)  # 갯수가 짧은 쪽에 filvalue가 들어간다
for a in c:
    print(a)

print()
aa = (1, 2, 3)
bb = (4, 5, 6)
for test in zip(aa, bb):
    print(test)
