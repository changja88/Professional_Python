# 명령(Command Pattern)
# - 함수를 인수로 전달하는 기법을 사용하면 명령 디자인 패턴도 구현을 단순하게 만들수 있다
# - 명령 패턴의 목적은 연산을 실행하는 객체와 연산을 구현하는 개체를 분리 하는 것이다
#   기본 개념은 명령 객체를 수신자와 호출자 사이에 놓고, 명령은 execute()라는 단 하나의 메서드로 인터페이스를 구현한다
#   이런 방식을 사용하면 호출자는 수산자의 인터페이스를 알 필요가 없으며, 명령의 서브클래스를 통해 서로 다른 수신자를 추가 할 수 있다
#   디자인 패턴에서는 '커맨드 패턴은 콜백에 대한 객체지향식 대체물' 이라고 설명한다


class MacroCommand:
    """명령 리스트를 실행하는 명령"""

    def __init__(self, commands):
        print('__init__')
        self.commands = list(commands)

    def __call__(self, *args, **kwargs):
        print('__call__')
        for command in self.commands:
            command()


def a():
    print('A')


def b():
    print('B')


maccroCommand = MacroCommand((a, b))()
