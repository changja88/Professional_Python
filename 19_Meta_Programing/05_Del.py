"""
속성 제거 처리하기
"""
"""
- del 문을 이용해서 객체 속성을 제거할 수 있다
"""


class BlackNight:
    def __init__(self):
        self.members = ['an arm', 'another arm', 'a leg', 'another leg']
        self.phrases = ["'Tis but a scratch.",
                        "It's just a flesh wound.",
                        "I'm invincible!",
                        "All right, we'll call it a draw."]

    @property
    def member(self):
        print('next member is :')
        return self.members[0]

    @member.deleter
    def member(self):
        text = 'BLACK NIGHT (loses {})\n-- {}'
        print(text.format(self.members.pop(0), self.phrases.pop(0)))


knight = BlackNight()
print(knight.member)
del knight.member
del knight.member
del knight.member
del knight.member
"""
- 데커레이터 대신 고전적인 호출 구문을 사용할 때는 fdel 인수를사용해서 제거자 함수를 설정한다
member = property(member_getter, fdel=member_getter)
"""

