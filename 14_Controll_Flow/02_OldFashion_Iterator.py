"""
고전적인 반복자
"""
"""
- 디자인 패넡의 청사진에 따라 고전적인 반복자 패턴을 구현한다
  이 방법은 파이썬의 관용적인 방법이 아니다
"""
import re
import reprlib

RE_WORDS = re.compile('\w+')

class Sentence:
    def __int__(self,text):
        self.text = text
        self.words = RE_WORDS.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self): # 이걸 구현하면 반복형이 된다
        return SentenceIterator(self.words)

class SentenceIterator:
    def __int__(self,words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index+=1
        return word

    def __iter__(self):
        return self
"""
- 위 예제, Sentence를 반복자로 만드는 것은 좋지 않은 생각이다
- 반복형과 반복자를 만드는데 있어서 흔히 발생하는 오류는 둘을 혼돈하기 떄문이다
- 반복형은 호출될 때마다 반복자를 새로 생성하는 __iter__메서드를 가지고 있다
- 반복자는 개별 항목을 반환하는 __next__메서드와 self를 반환하는 __iter__메서드를 가지고 있다
- 따라서, 반복자는 반복형이지만, 반복형은 반복자가 아니다

- Sentence 클래스 안에 __iter__, __next__도 구현해서 Sentence 객체를 반복형이자 반복자로 만들고 싶을 수도 있다
- 그러나 이건 잘못된 생각이다 -> 전형적인 안티패턴이다
- 반복자 패턴은 다음과 같은 용도에 사용해라
    - 집합 객체의 내부 표현을 노출시키지 않고 내용에 접근하는 경우
    - 집합 객체의 다중 반복을 지원하는 경우
    - 다양한 집합 구조체를 반복하기 위한 통일된 인터페이스를 제공하는 경우
"""
