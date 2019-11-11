"""
제너레이터 함수
"""
"""
- 02_OldFashion_Iterator 를 보다 파이써닉 하게 만들기 위해서 제너레이터 함수를 사용한다
"""
import re
import reprlib

RE_WORD = re.compile('\w+')

class Sentence:
    def __int__(self,text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        """
        - 현재 단어(word)를 생성한다
        - 함수가 끝에 도달하면 값을 자동으로 반환하므로, 이 return문은 필요 없다. 그리고 제너레이터 함수는
          StopIteration도 발생시키지 않는다. 값을 모두 생산한 후 그냥 빠져나간다
        - 별도의 반복자 클래스가 필요 없다
        """
        for word in self.words:
            yield word
        return

