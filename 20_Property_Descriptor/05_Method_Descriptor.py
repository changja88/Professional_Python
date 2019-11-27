"""
메서드 디스크립터
"""
"""
- 모든 사용자 정의 함수는 __get__메서드를 가지고 있어서, 클래스에 연결된 수는 디스크립터로 작동하기 때문에,
  클래스 안의 함수는 클래스에 바인딩된 메서드가 된다 
- 함수는 __set__메서드를 구현하지 않으므로, 함수는 논오버라이딩 디스크립터다 
"""

import collections


class Text(collections.UserString):
    def __repr__(self):
        return 'Text({!r})'.format(self.data)

    def reverse(self):
        return self[::-1]


word = Text('forword')
print(word)
print(word.reverse())
print(Text.reverse(Text('backword')))
