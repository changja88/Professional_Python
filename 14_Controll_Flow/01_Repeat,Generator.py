"""
반복형, 반복자, 제너레이터
"""
"""
- 파이썬은 리스프와 달리 매크로가 없으므로, 반복자 패턴을 추상화할 수 있게 yeild키워드가 추가 되었다
- yeild 키워드는 반복자로 작동하는 제너레이터를 생성할 수 있게 해준다
"""


import re
import reprlib

RE_WORD = re.compile('\w+')

class Sentence:
    def __init__(self,text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' %reprlib.repr(self.text)


s = Sentence('"The time has come," the Walus said,')
for word in s :
    print(word)

"""
파이썬 인터프리터가 x 객체를 반복해야 할 때는 언제나 iter(x)를 자동으로 호출한다
- 객체가 __iter__ 메서드를 구현하였는지 확인하고, 이 메서드를 호출해서 반복자를 가져온다
- __iter__메서드가 구현되어 있지 않지만 __getitem__이 구현되어 있다면, 파이썬은 인덱스에 0에서 시작해서 항목을 순서대로 가져온다
- 이 과정이 모두 실패하면 파이썬은 TypeError not iterable을 발생시킨다
- 모든 Sequence는 __getitem__을 구현하고 있기 때문에 반복이 가능하다
"""

"""
반복형과 반복자
- 반복형
    - iter()내장 함수가 반복자를 가녀올 수 있는 모든 객체와 반복자를 환하는 __iter__메서드를 구현하는 객체는 반복형이다
      0에서 시작하는 인덱스를 받는 __getitem__메서드를 구현하는 객체인 시퀀스도 마찬가지
- 반복자
    - 다음 항목을 반환하거나, 다음 항목이 없을 때 StopIteration예외를 발생시키는, 인수를 받지 않는 __next__를 구현하는 객체
      파이썬 반복자는 __iter__ 메서드도 구현 하므로 반복형이기도 하다
"""
s3 = Sentence('Pig and Pepper')
it = iter(s3)
print(next(it))
print(next(it))
print(next(it))
