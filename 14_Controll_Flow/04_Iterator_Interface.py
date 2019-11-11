"""
느긋한 구현
"""
"""
- Iterator인터페이스는 느긋하게 처리하도록 설계되어 있다
- next()는 한번에 한 항목만 생성한다
- 느긋한 계산법의 반대는 조급한 계산법(eager evaluation)이며, 둘 다 프로그래밍 언어 이론에서 실제 사용되는 용어이다
- 이전까지의 sentence는 느긋한 버전이 아니었다 __int__에서 텍스트 안에 있는 단어들의 리스트를 조급하게 생성해서
  self.words속성에 바인딩하기 때문이다. 그러므로 전체 텍스트를 처리해야 하며, 리스트는 거의 텍스트와 맞먹는 양의 메모리를 소비한다
"""
"""
- re.finditer() 함수는 re.findall()의 느긋한 버전으로, 리스트 대신 필요에 따라 re.MatchObject 객체를 생성하는
  제너레이터를 반환한다. 매칭되는 항목이 많으면 re.finditer()가 메모리를 많이 절약해준다
"""
import re
import reprlib

RE_WORD = re.compile('\w+')

class Sentence:
    def __int__(self,text):
        self.text = text

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        for match in RE_WORD.finditer(self.text):
            yield  match.group()